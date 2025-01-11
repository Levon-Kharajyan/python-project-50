from itertools import chain
from gendiff.formatters.templates import TEMPLATE_STYLISH


INDENT_CHAR = '    '
STEP = 1


def format_stylish_diff(data, depth=0):
    indent = INDENT_CHAR * depth
    lines = [line for node in data for line in format_node(node, depth)]
    result = chain('{', lines, [indent + '}'])
    return '\n'.join(result)


def format_node(data, depth):
    line = []
    if data['action'] == 'added':
        line.append(format_line(
            data['key'], data['value_new'], depth, '+ ')
        )
    elif data['action'] == 'deleted':
        line.append(format_line(
            data['key'], data['value_old'], depth, '- ')
        )
    elif data['action'] == 'changed':
        line.append(format_line(
            data['key'], data['value_old'], depth, '- ')
        )
        line.append(format_line(
            data['key'], data['value_new'], depth, '+ ')
        )
    elif data['action'] == 'unchanged':
        line.append(format_line(
            data['key'], data['value_old'], depth, '  ')
        )
    elif data['action'] == 'nested':
        nest_indent = INDENT_CHAR * (depth + STEP)
        nested_lines = [line for child in data['children'] for line in format_node(child, depth + STEP)]  # noqa: E501
        nested_block = '\n'.join(nested_lines)
        line.append(f'{nest_indent}{data["key"]}: {{\n{nested_block}\n{nest_indent}}}')  # noqa: E501
    return line


def format_line(key, value, depth, char):
    indent = INDENT_CHAR * depth
    line = []
    if isinstance(value, dict):
        line.append(TEMPLATE_STYLISH.format(
            indent, char, key, format_dict(value, depth + STEP))
        )
    else:
        line.append(TEMPLATE_STYLISH.format(
            indent, char, key, format_value(value))
        )
    return '\n'.join(line)


def format_dict(data, depth):
    indent = INDENT_CHAR * depth
    line = []
    for key, value in data.items():
        line.append(format_line(key, value, depth, '  '))
    result = chain('{', line, [indent + '}'])
    return '\n'.join(result)


def format_value(data):
    nested_dict = {}
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    elif isinstance(data, dict):
        for key in data:
            nested_dict[key] = format_value(data[key])
    else:
        return data
    return nested_dict
