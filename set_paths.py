from __future__ import annotations
import os
import argparse
import const

def dir_paths(paths_str: str) -> str:
    paths = paths_str.split(",")
    if not paths:
        raise ValueError("at least one path must be provided")
    else:
        for path in paths:
            if not os.path.isdir(path):
                raise ValueError(f"invalid path: {path}")
    return paths_str

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--paths",
        help="comma separated log directories",
        type=dir_paths,
        required=True
    )
    args = parser.parse_args()

    with open(const.paths_file, "w") as file:
        file.write(args.paths)
