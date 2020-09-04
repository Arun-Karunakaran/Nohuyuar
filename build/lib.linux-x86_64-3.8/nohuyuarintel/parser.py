import configparser
import os
parser = configparser.ConfigParser()

config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'nhyr.ini')


def planets():
    parser.read(config_file)
    names=parser.get("energies:","planets")
    names=names.split(',')
    return names

def signs():
    parser.read(config_file)
    names=parser.get("energies:","signs")
    names=names.split(',')
    return names

