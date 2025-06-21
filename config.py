import json
import os

def load_config(path):
    default_config = {
        "recursive": True,
        "dry_run": False,
        "excluded_extensions": [],
        "output_directory": "",
        "log_file": "file_sorter_log.txt"
    }
    if not os.path.exists(path):
        return default_config
    with open(path, "r") as f:
        user_config = json.load(f)
    default_config.update(user_config)
    return default_config