from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.utils import to_absolute_path

@hydra.main(config_path=to_absolute_path("configs"), config_name="train", version_base="1.3")
def train(cfg):
    print("something...")

if __name__ == "__main__":
    train() # pylint: disable=all