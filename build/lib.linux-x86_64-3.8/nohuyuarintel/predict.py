"""Analysis - predict-energies-combinations
Usage:
    predict.py <option> <option1> names
    predict.py <option> <option1> count   
    predict.py <option> <option1> result
    predict.py (-h | --help)
Arguments:
    <option>   defines the math / logical operation
    <option1>  energy category name / energy name
Options:
    -h --help                  Show this screen.
"""
from docopt import docopt
from nohuyuarintel.core.combinations import *


def main():
    arguments = docopt(__doc__)
    if arguments['<option>'] == 'combinations':
        if arguments['names']:
            get_names(arguments['<option1>'])
        elif arguments['count']:
            get_count(arguments['<option1>'])
        elif arguments['result']:
            get_result(arguments['<option1>'])

if __name__ == '__main__':
    main()
