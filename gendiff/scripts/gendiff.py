#!/usr/bin/env python3

import argparse
from gendiff.generate_diff import generate_diff


# Создаем константу DESCRIPTION, которую передадим в экземпляр парсера аргументов
DESCRIPTION = 'Compares two configuration files and shows a difference.'


def main():
    # Создаем экземпляр парсера аргументов
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    # Добавляем позиционные аргументы
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Добавляем опциональные (необязательные) аргументы
    parser.add_argument('-f', '--format', help='set format of output')
    # Парсим аргументы
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    return diff


if __name__ == '__main__':
    main()