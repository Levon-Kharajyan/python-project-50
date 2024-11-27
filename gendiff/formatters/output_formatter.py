def encode_to_json(data):
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    else:
        return data


def format_output(data):
    line = []
    for element in data:
        if element['action'] == 'deleted':
            line.append(
                f"  - {element['key']}: {encode_to_json(element['value_old'])}")
        if element['action'] == 'added':
            line.append(
                f"  + {element['key']}: {encode_to_json(element['value_new'])}")
        if element['action'] == 'unchanged':
            line.append(
                f"    {element['key']}: {encode_to_json(element['value_old'])}")
        if element['action'] == 'changed':
            line.append(
                f"  - {element['key']}: {encode_to_json(element['value_old'])}")
            line.append(
                f"  + {element['key']}: {encode_to_json(element['value_new'])}")
    return '{\n' + '\n'.join(line) + '\n}'
