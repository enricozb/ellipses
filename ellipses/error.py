import traceback

from ellipses.logging import logger


class EllipsesError(Exception):
    pass


def print_on_error(f):
    def g(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except EllipsesError as e:
            print(e)
        except Exception:
            traceback.print_exc()
            logger.error(
                "This is a bug in ellipses, please report an issue at https://github.com/enricozb/ellipses"
            )

    return g
