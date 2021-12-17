from __future__ import annotations
import os
import glob

def get_log_file_options(logs_directory: str) -> list:
    files = glob.glob(os.path.join(logs_directory, "metric-*.json"))
    files = sorted(files)
    # strip the last file
    files = files[:-1]
    return [
        {"label": os.path.split(file)[-1], "value": file} for file in files
    ]

def get_find_hashes_options() -> list:
    return [
        {"label": "chain_id_count", "value": "chain_id_count"},
        {"label": "hash_count", "value": "hash_count"},
    ]
