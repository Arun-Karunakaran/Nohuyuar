"""Core Energy module

This script allows the user to derive results out of various energies 
It is understood that Energies are derived and studies from core 
planets, panchabootha systems, zodic signs and static houses etc.,

This module is a class module for the energy systems

This script requires:

This file can also be imported as a module and contains the following
functions:
    
    * count - rerurns the length of the list passed as parameter
    * maxcombinations - returns the maximumnumber of combinations and its count
    * mincombinations - returns the desired number of combinations and its count
    * maxcrosscombinator - returns the max cross combination results between different category of energy.
    * mincrosscombinator - returns the desired cross combination

Usage: This module must be imported to other modules for use
"""

import itertools


class planet:
    """
    This is a class that represent planets
    ...

    Attributes
    ---------
    None

    Methods
    ------
    count(self)
        returns length of the list
    maxcombinations(self)
        returns the maximum combination of planet names and its count
    mincombinations(self,r)
        returns the desired no of combination of planet names and its count
   """
 
    def __init__(self,names: list=None):
        self.names = names if names is not None else []
    
    def count(self):
        """
        returns the length of the list
        
        Parameters
        ---------
        None : default is names : list
             The list of planet names

        Returns
        -------
        length of the list
        """

        return len(self.names)

    def maxcombinations(self):
        """
        returns the maximum combination of planet names and its count

        Parameters
        ----------
        None : default is names : list
             The list of planet names

        Returns
        -------
        result : list of tuples
             All possible combinations of planets are returned
        """
        
        result = []
        for L in range(0,len(self.names)+1):
            name = itertools.combinations(self.names,L)
            result += list(name)
            count = len(result)
        return (result, count)

    def mincombinations(self,r: int):
        """
        returns the desired no of combination of planet names and its count

        Parameters
        ----------
        None : default is names : list
             The list of planet names

        Returns
        -------
        result : tuple, list of tuples
             desired no of combinations of planets are returned
        """

        result = []
        name = itertools.combinations(self.names,r)
        result += list(name)
        count = len(result)
        return (result, count)


class signs:
    """
    This is a class that represent Zodiac Signs
    ...

    Attributes
    ---------
    None

    Methods
    ------
    count(self)
        returns length of the list
    maxcrosscombinations(self)
        returns the maximum combination of a sign with planets and its count
    mincrosscombinations(self,r)
        returns the desired no of combination of a sign with planet names and its count
   """

    def __init__(self,names: list=None):
        self.names = names if names is not None else []

    def count(self):
        return len(self.names)

#    def 
