from nohuyuarintel.core.energies import *
from nohuyuarintel.parser import *


planetnames = planets()
planets = planet(planetnames)
#zodiacnames = signs()
#signs = signs(zodiacnames)

def get_namescount(option):
    if option == 'planets':
        c = planets.count()
        print(c)
    elif option == 'signs':
        c = signs.count()
        print(c)
    else:
        raise ValueError("function takes 1 arg. Arg not correct / not found")
