#!/usr/bin/env python3

from gendiff.argument_parser import parse_argument
from gendiff.generate_diff import generate_diff  # noqa: F401


def main():
    args = parse_argument()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
