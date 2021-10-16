import argparse

from common.test_runner import TestRunner


def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("hw", help="hw number", type=int)

    difficulty = parser.add_mutually_exclusive_group()
    difficulty.add_argument("--easy", action="store_true", help="run tests for easy version of hw (use by default)")
    difficulty.add_argument("--hard", action="store_true", help="run tests for hard version of hw")

    parser.add_argument("--src", help="path to the directory with your code")
    parser.add_argument("--main", help="name of your main hw file")

    return parser


def get_difficulty(args):
    return "hard" if args.hard else "easy"


if __name__ == '__main__':
    args = get_args_parser().parse_args()
    tester = TestRunner(args.hw, get_difficulty(args), args.src, args.main)
    tester.run()
