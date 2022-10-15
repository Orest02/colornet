## Update: 8th Jan, 2022
## this file is supposed to give you a general idea on how to
## use the pre-trained model for colorizing B&W images. This
## file still needs development.
import logging
import pathlib
from dataclasses import dataclass
from typing import Optional, TypeVar, Union

import torch
from anypath.anypath import AnyPath

from colornet.logging import log_decorator

from .models import MainModel, build_res_unet


@dataclass
class Predict:
    unet_path: str
    gan_path: str
    device: str
    logger: logging.Logger

    @log_decorator.log_decorator()
    def __post_init__(self):
        self.model: Optional[torch.nn.Module] = None
        self.device: torch.device = torch.device(
            self.device
            if self.device == "cpu" or getattr(torch, self.device).is_available()
            else "cpu"
        )

    @log_decorator.log_decorator()
    def init_model(self):
        self.model = build_res_unet(n_input=1, n_output=2, size=256)

    @log_decorator.log_decorator()
    def load_model(self):
        self.logger.info(f"Loading model from {self.unet_path}")
        self.model.load_state_dict(torch.load(self.unet_path, map_location=self.device))

        self.model = MainModel(net_G=self.model)
        self.model.load_state_dict(torch.load(self.gan_path, map_location=self.device))

        self.model.eval()

    @log_decorator.log_decorator()
    def forward(self, image: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            output = self.model.net_G(image.to(self.device))

        return output
