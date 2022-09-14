import numpy as np
import torch

from colornet.machine_learning.utils import lab_to_rgb


class Postprocessing:
    @staticmethod
    def concat_images_to_rgb(img_gray: torch.Tensor, img_ab: torch.Tensor) -> np.ndarray:
        return lab_to_rgb(img_gray, img_ab.cpu())
