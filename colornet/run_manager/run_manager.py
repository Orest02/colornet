import logging
from dataclasses import dataclass
from typing import Union

import numpy as np
from anypath.anypath import AnyPath

from colornet.machine_learning.inference import Predict
from colornet.machine_learning.postprocessing import Postprocessing
from colornet.machine_learning.preprocessing import Preprocessing


@dataclass
class MainManager:
    logger: logging.Logger
    preprocess: Preprocessing
    inference: Predict
    postprocess: Postprocessing

    def run_one_cycle(self, img_path: Union[AnyPath, str]) -> np.ndarray:
        self.preprocess.read_img(img_path)
        img_gray = self.preprocess.preprocess()

        img_coloured = self.inference.forward(img_gray)

        return Postprocessing.concat_images_to_rgb(img_gray, img_coloured)
