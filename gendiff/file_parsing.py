import json
import yaml
import os


def parse_file(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == '.json':
        return json.load(open(file_path))
    else:
        return yaml.load(open(file_path))
