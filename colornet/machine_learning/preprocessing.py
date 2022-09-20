import logging
from dataclasses import dataclass
from typing import Tuple, Union

import PIL
import numpy as np
import torch
from anypath.anypath import AnyPath
from torchvision import transforms

from colornet.logging import log_decorator


@dataclass
class Preprocessing:
    img_size: Tuple[int, int]
    logger: logging.Logger

    @log_decorator.log_decorator()
    def __post_init__(self) -> None:
        self.image: PIL.Image.Image

        self.transforms: transforms = transforms.Compose(
            [
                transforms.Lambda(lambda image: PIL.ImageOps.grayscale(image)),
                transforms.Resize(tuple(self.img_size), PIL.Image.BICUBIC),
                transforms.ToTensor(),
                transforms.Lambda(lambda x: x * 2. - 1.)
            ])

    @log_decorator.log_decorator()
    def read_img(self, img_path: Union[AnyPath, str]) -> None:
        self.logger.info(f"Attempting to read image from {img_path}")
        self.image = PIL.Image.open(img_path)

        np_img = np.asarray(self.image)
        self.logger.info(f"Successfully read the image. Its size is {self.image.size} and extrema are {np_img.min()}:{np_img.max()}")

    @log_decorator.log_decorator()
    def preprocess(self) -> torch.Tensor:
        return self.transforms(self.image).unsqueeze(0)
