&nbsp;
# LLEN-SLAM
基于弱光增强的SLAM

## 💡 News 新闻


- **2024.08.19** The initial model was completed, and compared with different low-light models, the effect was only 20.9. Other models were tested simultaneously (avg:21.5), with a difference of 0.6 points.
- **2024.08.08** project startup 🎈


## ⚙ module 模型组件


## 🖼 Visual Comparison 视觉比较


## 🧾 Weights and Results 

| Folder (test datasets)                        | PSNR        | SSIM       | LPIPS      | GT Mean | Results                                                      | Weights Path             |
| --------------------------------------------- | ----------- | ---------- | ---------- | ------- | ------------------------------------------------------------ | ------------------------ |
| (LOLv1)<br />v1 w perc loss/ wo gt mean       | 20.9049     |  0.7718    | **   **    |         |   | LOLv1/perc.pth         |


## 🌑 1. Get Started 

- Python 3.7.0
- Pytorch 1.11.1

(1) Create Conda Environment

```bash
conda create --name LLEN python=3.7.0
conda activate LLEN
```

(2) Clone Repo

```bash
git clone git@github.com:
```

(3) Install Dependencies

```bash
cd 
pip install -r requirements.txt
```

### Data Preparation

You can refer to the following links to download the datasets. Note that we only use `low_blur` and `high_sharp_scaled` subsets of `LOL-Blur` dataset.

- [LOLv1](https://daooshee.github.io/BMVC2018website/)

<details open> <summary>datasets (click to expand)</summary>
  
```
├── datasets
	├── DICM
	├── LIME
	├── LOLdataset
		├── our485
			├──low
			├──high
		├── eval15
			├──low
			├──high

```
</details>

## 🌒 2. Testing 

## 🌒 3. Training  

```bash
# activate the enviroment
conda activate Retinexformer

# LOL-v1
python3 basicsr/train.py --opt Options/LOL_v1.yml

```
