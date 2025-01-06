def encode_to_str(data):
    if isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    else:
        return data
