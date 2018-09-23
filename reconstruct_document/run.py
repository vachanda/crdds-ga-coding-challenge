import argparse
import sys
from pathlib import Path
from reconstruction import Reconstruction


def validate_input(args):
    """
    Validates the input to the function.
    :param args: The args parse object.
    :return: True if all the input criteria is met.
    """
    for arg in vars(args):
        path = Path(getattr(args, arg))

        if arg == "output":
            if not path.parent.exists():
                return False
            continue

        if not path.is_file():
            return False

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lexicon", help="Specify the path of the lexical file.", type=str)
    parser.add_argument("--document", help="Specify the path of the input document.", type=str)
    parser.add_argument("--output", help="Specify the path of the output document.", type=str)
    args = parser.parse_args()
    if args.lexicon is None or args.document is None or args.output is None:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if not validate_input(args):
        print("Please enter valid paths for the inputs.")
        parser.print_help(sys.stderr)
        sys.exit(1)

    doc_reconstructor = Reconstruction(args.document, args.output, args.lexicon)
    doc_reconstructor.re_construct()


if __name__ == "__main__":
    main()