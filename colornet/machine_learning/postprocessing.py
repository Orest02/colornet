import io
import logging
import os
from dataclasses import dataclass
from typing import Union

import matplotlib.pyplot as plt
import numpy as np
import torch
from anypath.anypath import AnyPath
from PIL import Image

from colornet.logging import log_decorator
from colornet.machine_learning.utils import lab_to_rgb


@dataclass
class Postprocessing:
    logger: logging.Logger

    @log_decorator.log_decorator()
    def concat_images_to_rgb(self, img_gray: torch.Tensor, img_ab: torch.Tensor) -> np.ndarray:
        return lab_to_rgb(img_gray, img_ab.cpu())[0]

    @log_decorator.log_decorator()
    def save_output(self, img: np.ndarray, output_path: Union[AnyPath, str] = "output/output.png"):
        image = Image.fromarray((img * 255).astype('uint8')).convert('RGB')

        os.makedirs(os.path.split(output_path)[0], exist_ok=True)
        image.save(output_path)

    @log_decorator.log_decorator()
    def save_output_to_bytestream(self, img: np.ndarray) -> io.BytesIO:
        image = Image.fromarray((img * 255).astype('uint8')).convert('RGB')

        bytes_image: io.BytesIO = io.BytesIO()
        image.save(bytes_image, format='PNG')

        return bytes_image
