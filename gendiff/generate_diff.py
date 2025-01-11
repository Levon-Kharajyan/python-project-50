from gendiff.file_parser import parse_file
from gendiff.diff_creater import create_diff
from gendiff.formatters.stylish import format_stylish_diff
from gendiff.formatters.plain import format_plain_diff
from gendiff.formatters.json_ import get_json


def generate_diff(file_path_1, file_path_2, format):
    data_1 = parse_file(file_path_1)
    data_2 = parse_file(file_path_2)
    diff = create_diff(data_1, data_2)
    result = select_formatters(diff, format)
    return result


def select_formatters(data, format):
    if format == 'stylish':
        return format_stylish_diff(data)
    elif format == 'plain':
        return format_plain_diff(data)
    elif format == 'json':
        return get_json(data)
