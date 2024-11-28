import argparse


# Создаем константу, которую передадим в экземпляр парсера аргументов
DESCRIPTION = 'Compares two configuration files and shows a difference.'


def parse_argument():
    # Создаем экземпляр парсера аргументов
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    # Добавляем позиционные аргументы
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Добавляем опциональные (необязательные) аргументы
    parser.add_argument('-f', '--format', help='set format of output')
    # Парсим аргументы
    args = parser.parse_args()
    return args
