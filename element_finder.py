import argparse
from Finder import ElementFinder
from globals import PARSER, PARSER_INPUT

DESCRIPTION = 'description'
ARGUMENTS = 'arguments'
NAMES = 'names'

def get_user_args():
    """
    Initialize and retreive user args from command

    Attributes
    ----------
    None

    Returns
    ----------
    None
    """
    parser = argparse.ArgumentParser(description=PARSER[DESCRIPTION])

    for argument in PARSER[ARGUMENTS]:
        names = argument.pop(NAMES, None)
        parser.add_argument(*names, **argument)

    parser.parse_args()
    args = parser.parse_args()
    return args


def start_find():
    """
    Start the find using element id and url from user's args

    Attributes
    ----------
    None

    Returns
    ----------
    None
    """
    finder_args = dict()
    custom_args = dict()
    args = get_user_args()
    if 'custom' in args:
        finder_args['custom'] = args.custom
    for argument in PARSER_INPUT:
        finder_args[argument] = getattr(args, argument)
    finder = ElementFinder(**finder_args)
    finder.start()

