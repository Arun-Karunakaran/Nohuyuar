"""Module for combinations
Usage:
    combinations.py names <option>
    combinations.py count <option>    
    combinations.py result <option>
    combinations.py (-h | --help)
Arguments:
    <option>  energy category name / energy name
Options:
#    --vocab-size=<vocab-size>  Vocabulary size. [default: 10000]
    -h --help                  Show this screen.
"""

from docopt import docopt
from nohuyuarintel.parser import *
from nohuyuarintel.core.energies import *

__all__ = ['get_count','get_result']

planetnames = planets()
planets = planet(planetnames)
#zodiacnames = signs()
#zodiacplanets = signs(zodiacnames)

def get_names(option):
    """
    This Function is used for printing combinations
    
    Parameters
    ---------
    option : object
          objects of energy module

    Returns
    -------
    all_possible[0] : list of tuples
          All possible combinations of elements in the list are returned here
    
    Raises
    ------
    ValueError
          If the argument : object passed is not correct or not found
    """

    if option == 'planets':
        r = input("For nCr choose possibilities r as ->1 or 2 or 3 ... or all    ")
        if r == 'all':
            all_possible = planets.maxcombinations()
            print (all_possible[0][1:all_possible[1]])
        else:
            r = int(r)
            all_possible = planets.mincombinations(r)
            print (all_possible[0])
    else:
        raise ValueError("function takes 1 arg. Arg not correct / not found")

def get_count(option):
    """
    This Function is used for printing the count of combinations
    
    Parameters
    ---------
    option : object
          objects of energy module

    Returns
    -------
    all_possible[1] : int
          Count of combinations of elements in the list are returned
    
    Raises
    ------
    ValueError
          If the argument : object passed is not correct or not found
    """

    if option == 'planets':
        r = input("For nCr choose possibilities r as ->1 or 2 or 3 ... or all    ")
        if r == 'all':
            all_possible = planets.maxcombinations()
            print (all_possible[1] -1)
        else:
            r = int(r)
            all_possible = planets.mincombinations(r)
            print (all_possible[1])
    else:
        raise ValueError("function takes 1 arg. Arg not correct / not found")

def get_result(option):
    """
    This Function is used for printing both combinations and its count
    
    Parameters
    ---------
    option : object
          objects of energy module

    Returns
    -------
    all_possible : list of tuples, int
          both possible combinations of elements in the list and its count are returned
    
    Raises
    ------
    ValueError
          If the argument : object passed is not correct or not found
    """

    if option == 'planets':
        r = input("For nCr choose possibilities r as ->1 or 2 or 3 ... or all    ")
        if r == 'all':
            all_possible = planets.maxcombinations()
            print (all_possible[0][1:all_possible[1]],all_possible[1] -1)
        else:
            r = int(r)
            all_possible = planets.mincombinations(r)
            print (all_possible)
    else:
        raise ValueError("function takes 1 arg. Arg not correct / not found")

#def get_zodiacndplanetnames():
#def get_zodiacndplanetcount():
#def get_zodiacndplanetresult():

def main():
    arguments = docopt(__doc__)
    #print(arguments)
    if arguments['names']:
        get_names(arguments['<option>'])
    elif arguments['count']:
        get_count(arguments['<option>'])
    elif arguments['result']:
        get_result(arguments['<option>'])

if __name__ == '__main__':
    main()
