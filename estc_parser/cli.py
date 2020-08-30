import click

from estc_parser.parser import files2csv
from estc_parser.utils.config import INPUT_PATH


def main():
    files2csv(INPUT_PATH)


if __name__ == "__main__":
    main()
