import os
from typing import Union

import hydra
from anypath.anypath import AnyPath
from hydra import initialize, compose
from hydra.core.hydra_config import HydraConfig
from hydra.utils import instantiate
from omegaconf import DictConfig

from colornet.machine_learning import Postprocessing
from colornet.run_manager.run_manager import MainManager

os.environ["HYDRA_FULL_ERROR"] = "1"

@hydra.main(version_base=None, config_path="configs", config_name="config")
def instantiate_runner(cfg: DictConfig) -> MainManager:
    logger = instantiate(cfg.logger)
    preprocessing = instantiate(cfg.preprocess)
    inference = instantiate(cfg.inference)
    postprocessing = Postprocessing(logger)

    runner = MainManager(
        logger=logger,
        preprocess=preprocessing,
        inference=inference,
        postprocess=postprocessing
    )

    runner.init_elements()

    return runner


def main(runner: MainManager, img_path: Union[AnyPath, str]):
    img = runner.run_one_cycle(img_path)

    runner.postprocess.save_output(img)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img_path = "input/3895858.jpg"

    initialize(version_base=None, config_path="configs")
    cfg = compose(config_name="config")

    runner = instantiate_runner(cfg)
    main(runner=runner, img_path=img_path)
