import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import lpips

# 初始化 LPIPS 模型
lpips_model = lpips.LPIPS(net='alex')

def calculate_metrics(gt_folder, output_folder, log_file_path):
    # 打开日志文件
    with open(log_file_path, 'w') as log_file:
        log_file.write("Image Pair, PSNR, SSIM, LPIPS\n")  # 写入日志文件头

        # 获取文件夹中所有图片的文件名
        gt_images = sorted([f for f in os.listdir(gt_folder) if os.path.isfile(os.path.join(gt_folder, f))])
        output_images = sorted([f for f in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, f))])

        # 确保文件夹中的文件数量相等
        assert len(gt_images) == len(output_images), "The number of images in the two folders do not match."

        psnr_values = []
        ssim_values = []
        lpips_values = []

        for gt_image_name, output_image_name in zip(gt_images, output_images):
            # 加载图像
            gt_image = cv2.imread(os.path.join(gt_folder, gt_image_name))
            output_image = cv2.imread(os.path.join(output_folder, output_image_name))

            # 调整尺寸，使两张图片尺寸相同
            if gt_image.shape != output_image.shape:
                output_image = cv2.resize(output_image, (gt_image.shape[1], gt_image.shape[0]))

            # 计算 PSNR
            psnr_value = psnr(gt_image, output_image, data_range=gt_image.max() - gt_image.min())
            psnr_values.append(psnr_value)

            # 计算 SSIM
            ssim_value = ssim(gt_image, output_image, multichannel=True)
            ssim_values.append(ssim_value)

            # 计算 LPIPS
            gt_image_tensor = lpips.im2tensor(cv2.cvtColor(gt_image, cv2.COLOR_BGR2RGB))
            output_image_tensor = lpips.im2tensor(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
            lpips_value = lpips_model(gt_image_tensor, output_image_tensor)
            lpips_values.append(lpips_value.item())

            # 写入日志文件
            log_file.write(f"{gt_image_name} vs {output_image_name}, {psnr_value:.4f}, {ssim_value:.4f}, {lpips_value.item():.4f}\n")
            print(f"Processed {gt_image_name} and {output_image_name}: PSNR={psnr_value}, SSIM={ssim_value}, LPIPS={lpips_value.item()}")

        # 记录平均值
        log_file.write(f"\nAverage PSNR: {np.mean(psnr_values):.4f}\n")
        log_file.write(f"Average SSIM: {np.mean(ssim_values):.4f}\n")
        log_file.write(f"Average LPIPS: {np.mean(lpips_values):.4f}\n")

# 示例调用
gt_folder = './gt'
output_folder = './output'
log_file_path = 'metrics_log.txt'
calculate_metrics(gt_folder, output_folder, log_file_path)
