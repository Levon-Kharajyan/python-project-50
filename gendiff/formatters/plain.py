from gendiff.formatters.templates import (
    TEMPLATE_PLAIN_ADDED,
    TEMPLATE_PLAIN_REMOVED,
    TEMPLATE_PLAIN_UPDATE,
    TEMPLATE_PLAIN_PATH
)


def format_plain_diff(data):
    lines = [line for node in data for line in node_format(node, node['key'])]
    return '\n'.join(lines)


def node_format(data, path):
    line = []
    if data['action'] == 'added':
        line.append(
            TEMPLATE_PLAIN_ADDED.format(
                path,
                format_val(data['value_new'])
            )
        )
    elif data['action'] == 'deleted':
        line.append(
            TEMPLATE_PLAIN_REMOVED.format(path)
        )
    elif data['action'] == 'changed':
        line.append(
            TEMPLATE_PLAIN_UPDATE.format(
                path,
                format_val(data['value_old']),
                format_val(data['value_new'])
            )
        )
    elif data['action'] == 'nested':
        for child in data['children']:
            nested_path = TEMPLATE_PLAIN_PATH.format(path, child['key'])
            line.extend(node_format(child, nested_path))
    return line


def format_val(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    elif isinstance(data, str):
        return "'{}'".format(data)
    elif isinstance(data, int):
        return "{}".format(data)
