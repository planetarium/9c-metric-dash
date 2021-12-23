from __future__ import annotations
import os
import glob
import const

def get_log_file_options() -> list:
    with open(const.paths_file, "r") as file:
        log_directory = file.read()

    files = glob.glob(os.path.join(log_directory, "metric-*.json"))
    files = sorted(files)
    # strip the last file
    files = files[:-1]
    return [
        {"label": os.path.split(file)[-1], "value": file} for file in files
    ]

def get_block_evaluation_duration_options() -> list:
    return [
        {"label": "index", "value": "index"},
        {"label": "tx_count", "value": "tx_count"},
    ]

def get_block_states_update_duration_options() -> list:
    return [
        {"label": "index", "value": "index"},
        {"label": "key_count", "value": "key_count"},
    ]

def get_find_hashes_options() -> list:
    return [
        {"label": "chain_id_count", "value": "chain_id_count"},
        {"label": "hash_count", "value": "hash_count"},
    ]
