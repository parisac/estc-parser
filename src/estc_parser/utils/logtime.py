import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
handler = logging.StreamHandler()
log_format = "%(asctime)s %(levelname)8s | %(message)s"
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)


def timed(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug(
            "{}() - Total_Time: {}s".format(func.__name__, round(end - start, 2))
        )
        return result

    return wrapper
