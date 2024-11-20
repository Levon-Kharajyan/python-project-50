from file_parser import parse_file


def create_diff(data_1, data_2):
    diff = []
    keys = sorted(data_1.keys() | data_2.keys())
    for key in keys:
        if key in data_1 and key not in data_2:
            node = {'key': key, 'action': 'deleted', 'value_old': data_1[key]}
        elif key not in data_1 and key in data_2:
            node = {'key': key, 'action': 'added', 'value_new': data_2[key]}
        elif data_1[key] == data_2[key]:
            node = {'key': key, 'action': 'unchanged', 'value_old': data_1[key]}
        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            child = create_diff(data_1[key], data_2[key])
            node = {'key': key, 'action': 'nested', 'children': child}
        else:
            node = {'key': key, 'action': 'changed', 'value_old': data_1[key], 'value_new': data_2[key]}
        diff.append(node)
    return diff