from __future__ import annotations
import os
import argparse
import const

def dir_path(path: str) -> str:
    if os.path.isdir(path):
        return path
    else:
        raise ValueError("invalid path")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        help="path to log directory",
        type=dir_path,
        required=True
    )
    args = parser.parse_args()

    with open(const.path_file, "w") as file:
        file.write(args.path)
