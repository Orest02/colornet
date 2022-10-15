from hydra import initialize, compose
from hydra.core.global_hydra import GlobalHydra
from hydra.utils import instantiate

if __name__ == "__main__":
    GlobalHydra.instance().clear()
    initialize(version_base=None, config_path="../../configs")
    cfg = compose(config_name="config")

    app = instantiate(cfg.app)
    app.run()
