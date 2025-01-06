from gendiff.file_parser import parse_file
from gendiff.diff_creater import create_diff
from gendiff.formatters.stylish import format_stylish_diff
from gendiff.formatters.plane import format_plane_diff


def generate_diff(file_path_1, file_path_2, format='stylish'):
    data_1 = parse_file(file_path_1)
    data_2 = parse_file(file_path_2)
    diff = create_diff(data_1, data_2)
    result = select_formatters(diff, format)
    return result


def select_formatters(data, format):
    if format == 'stylish':
        return format_stylish_diff(data)
    elif format == 'plane':
        return format_plane_diff(data)
