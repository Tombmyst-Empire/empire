import argparse
import pathlib
import sys
from os.path import join

sys.path.insert(0, join(str(pathlib.Path(__file__).parent), 'src'))

from empire_p._init import init

_root = str(pathlib.Path(__file__).parent.parent.parent.resolve())

def nothing(): pass

commands_mapping = {
    'init': init,
    'update': nothing
}

parser = argparse.ArgumentParser('Empire Project Manager')
parser.add_argument('command', nargs='?', choices=list(commands_mapping.keys()))

args = parser.parse_args()

if not args.command:
    raise Exception('Missing argument to command line')

try:
    commands_mapping[args.command]()
    print('\nDone!')
except KeyboardInterrupt:
    print('Exiting...')
