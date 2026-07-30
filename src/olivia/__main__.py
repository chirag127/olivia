"""Entry point: `python -m olivia`."""

import argparse

from olivia import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="olivia",
        description="Olivia — a modular Python voice assistant for Windows.",
    )
    parser.add_argument("--version", action="version", version=f"olivia {__version__}")
    parser.parse_args()

    from olivia.core.assistant import run

    run()


if __name__ == "__main__":
    main()
