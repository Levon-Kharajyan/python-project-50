import os


def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension