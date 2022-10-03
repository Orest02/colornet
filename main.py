import os
from typing import Union

from anypath.anypath import AnyPath
from hydra import compose, initialize

from colornet.hydra.init_runner import instantiate_runner
from colornet.run_manager.run_manager import MainManager

os.environ["HYDRA_FULL_ERROR"] = "1"


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
