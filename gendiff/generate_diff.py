import json


def convert_bool(content):
    if type(content) is bool:
        return str(content).lower()
    else:
        return content


def generate_diff(file1_path, file2_path):
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
    f1_keys = list(file1.keys())
    f2_keys = list(file2.keys())
    keys = sorted(list(set(f1_keys + f2_keys)))
    result = []
    for key in keys:
        if key in f1_keys and key in f2_keys:
            if file1[key] == file2[key]:
                result.append(f"    {key}: {convert_bool(file1[key])}")
            else:
                result.append(f"  - {key}: {convert_bool(file1[key])}")
                result.append(f"  + {key}: {convert_bool(file2[key])}")
        if key in f1_keys and key not in f2_keys:
            result.append(f"  - {key}: {convert_bool(file1[key])}")
        if key not in f1_keys and key in f2_keys:
            result.append(f"  + {key}: {convert_bool(file2[key])}")
    return '{\n' + '\n'.join(result) + '\n}'
