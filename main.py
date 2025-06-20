from gui import run_gui
from config import load_config

if __name__ == "__main__":
    config = load_config("config.json")
    run_gui(config)
