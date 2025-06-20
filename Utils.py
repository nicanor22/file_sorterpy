import os

def resolve_duplicate_filename(path):
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{base}({counter}){ext}"
        counter += 1
    return path

def log_action(message, log_file="file_sorter_log.txt"):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")
