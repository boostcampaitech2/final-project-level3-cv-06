
## Pytorch Lightning
<a href="https://www.pytorchlightning.ai/">
  <img src="https://user-images.githubusercontent.com/51853700/147061484-ad7be02d-e786-4eeb-8520-d0a828f4ddc3.png" width=400 height=150></a>

## Content
```
.
├── API
│   ├── model.py
├── datasets
│   ├── dataModule.py
│   └── datasets.py
├── detection_utils
│   ├── datamodule.ipynb
│   ├── EDA.ipynb
│   ├── fill_path.ipynb
│   ├── get_pretrained.py
│   ├── pad_under_target.py
│   └── select_below_wh.py
├── inference.py
├── models
│   ├── efficientdet.py
│   ├── fasterrcnn_new_mAP.py
│   ├── fasterrcnn.py
│   ├── metrics.py
│   ├── models.py
│   ├── resnet.py
│   ├── save_fig.py
│   └── weights
└── train.py
```


## Object Detection Model
```
- 백본 : resnet50
- 모델 : faster-rcnn
```
## Inference Result & weights
```
- mAP : 0.92
- 실행시간
  GPU : under 0.2s/image
  CPU : under 2s/image
```
weight,config download

![image](https://user-images.githubusercontent.com/61641072/147064360-47fd7dd2-9ff4-4792-96bc-8e79d5f588cb.png)

## Confusion Matrix
<img src="https://user-images.githubusercontent.com/51853700/147060385-d7b3941c-f76d-4917-aab8-e88f3daff68c.png" width=600 height=400>

## Simple Start
Train
```
python train.py
```
Inference
```
detection/detection_utils/EDA.ipynb
```

## References
https://github.com/PyTorchLightning/pytorch-lightning  
S. Ren, K. He, R. Girshick, and J. Sun, "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks", 2016
