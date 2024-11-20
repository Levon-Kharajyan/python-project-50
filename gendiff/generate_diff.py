from file_parser import parse_file
from diff_creater import create_diff
from formatters.output_formatter import format_output

def generate_diff(file_path_1, file_path_2):
    data_1 = parse_file(file_path_1)
    data_2 = parse_file(file_path_2)
    diff = create_diff(data_1, data_2)
    result = format_output(diff)
    return result