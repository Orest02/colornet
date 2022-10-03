import io
import logging
from dataclasses import dataclass
from typing import Union

import numpy as np
from anypath.anypath import AnyPath

from colornet.logging import log_decorator
from colornet.machine_learning.inference import Predict
from colornet.machine_learning.postprocessing import Postprocessing
from colornet.machine_learning.preprocessing import Preprocessing


@dataclass
class MainManager:
    logger: logging.Logger
    preprocess: Preprocessing
    inference: Predict
    postprocess: Postprocessing

    @log_decorator.log_decorator()
    def init_elements(self):
        self.inference.init_model()
        self.inference.load_model()

    @log_decorator.log_decorator()
    def run_one_cycle(self, img_path: Union[AnyPath, str, io.BytesIO]) -> np.ndarray:
        self.preprocess.read_img(img_path)
        img_gray = self.preprocess.preprocess()

        img_coloured = self.inference.forward(img_gray)

        return self.postprocess.concat_images_to_rgb(img_gray, img_coloured)
