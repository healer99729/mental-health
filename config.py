import torch


class BaseConfig:
    DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
