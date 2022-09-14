from dataclasses import dataclass
from typing import Tuple, Union

import PIL
import torch
from anypath.anypath import AnyPath
from torchvision import transforms


@dataclass
class Preprocessing:
    img_size: Tuple[int, int]

    def __post_init__(self) -> None:
        self.image: PIL.Image

        self.transforms: transforms = transforms.Compose(
            [
                transforms.Lambda(lambda image: PIL.ImageOps.grayscale(image)),
                transforms.Resize((256, 256), PIL.Image.BICUBIC),
                transforms.ToTensor(),
                transforms.Lambda(lambda x: x * 2. - 1.)
            ])

    def read_img(self, img_path: Union[AnyPath, str]) -> None:
        self.image = PIL.Image.open(img_path)

    def preprocess(self) -> torch.Tensor:
        return self.transforms(self.image)
