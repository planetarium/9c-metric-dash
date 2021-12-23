# Nine Chronicles Metric Log Dash

## Description

A small [Flask] app to monitor [NineChronicles.Headless] activities.

## Requirements

Run

```bash
$ pip3 install -r requirements.txt
```

to install the dependencies.

## Usage

Use the included script `set_paths.py` as described below

```bash
$ python3 set_paths.py -p <comma_separated_log_directory_paths>
```

to save paths to the directory containing the relavent log files.
Then run with

```bash
$ flask run
```

to serve the app locally. Once served, the app can be accessed from
the following address.

```
http://localhost:5000/app/
```

[Flask]: https://flask.palletsprojects.com
[NineChronicles.Headless]: https://github.com/planetarium/NineChronicles.Headless
