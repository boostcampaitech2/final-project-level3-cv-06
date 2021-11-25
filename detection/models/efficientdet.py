import torch
from effdet import DetBenchTrain, EfficientDet, get_efficientdet_config
from effdet.efficientdet import HeadNet


# https://github.com/rwightman/efficientdet-pytorch
def get_net():

    config = get_efficientdet_config('tf_efficientdet_d5')
    net = EfficientDet(config, pretrained_backbone=False)

    checkpoint = torch.load('../input/efficientdet/efficientdet_d5-ef44aea8.pth')
    net.load_state_dict(checkpoint)

    # 이 부분 수정 필요 
    config.num_classes = 39
    config.image_size = 512

    net.class_net = HeadNet(config, num_outputs=39, norm_kwargs=dict(eps=.001, momentum=.01))
    return DetBenchTrain(net, config)


class efficientdet():
    def __init__():
        pass
        
    def forward(self, x):
        return get_net(x)
