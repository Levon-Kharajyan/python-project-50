import json
from gendiff.file_extension import get_file_extension


def parse_file(file_path):
    if get_file_extension(file_path) == '.json':
        return json.load(open(file_path))
    else:
        return None