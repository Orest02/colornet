import numpy as np
import torch

from colornet.logging import log_decorator
from colornet.machine_learning.utils import lab_to_rgb


class Postprocessing:

    @log_decorator.log_decorator()
    @staticmethod
    def concat_images_to_rgb(img_gray: torch.Tensor, img_ab: torch.Tensor) -> np.ndarray:
        return lab_to_rgb(img_gray, img_ab.cpu())
