import argparse

klickbrick = argparse.ArgumentParser("klickbrick")

from .hello import hello_parser  # noqa: E402


def run():
    args = klickbrick.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
