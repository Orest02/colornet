import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig

from colornet.machine_learning import Postprocessing
from colornet.run_manager.run_manager import MainManager


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
