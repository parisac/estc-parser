import click

from .parser import files2csv
from .utils.config import INPUT_PATH
from .utils.logtime import logger


def main():
    logger.info("Starting to process files:")
    files2csv(INPUT_PATH)


if __name__ == "__main__":
    main()
