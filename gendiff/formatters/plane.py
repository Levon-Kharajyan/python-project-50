from gendiff.formatters.json_yaml_encoder import encode_to_str


def format_plane_diff(data):
    line = []
    for element in data:
        if element['action'] == 'deleted':
            line.append(
                f"  - {element['key']}: {encode_to_str(element['value_old'])}")
        if element['action'] == 'added':
            line.append(
                f"  + {element['key']}: {encode_to_str(element['value_new'])}")
        if element['action'] == 'unchanged':
            line.append(
                f"    {element['key']}: {encode_to_str(element['value_old'])}")
        if element['action'] == 'changed':
            line.append(
                f"  - {element['key']}: {encode_to_str(element['value_old'])}")
            line.append(
                f"  + {element['key']}: {encode_to_str(element['value_new'])}")
    return '{\n' + '\n'.join(line) + '\n}'
