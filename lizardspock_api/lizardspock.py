# Rock Paper Scissors Lisard Spock
#
# https://www.youtube.com/watch?v=R0pUbct9WgI
from collections import namedtuple
from typing import Dict, List, Union, NewType
import random

Results = namedtuple('Results', 'win lose tie')
results = Results('win', 'lose', 'tie')

ChoiceDict = NewType('ChoiceType', Dict[int, str])

choices: List[ChoiceDict] = \
            [
               {'id': 0, 'name': 'rock'},
               {'id': 1, 'name': 'paper'},
               {'id': 2, 'name': 'scissors'},
               {'id': 3, 'name': 'lizard'},
               {'id': 4, 'name': 'spock'}
            ]

def play(player, computer):
    if (computer + 1) % 5 == player:
        result = results.win
    elif (computer + 2) % 5 == player:
        result = results.win
    elif computer == player:
        result = results.tie
    else:
        result = results.lose

    return {'results': result, 'player': player, 'computer': computer }


def get_random_choice():
    upper = len(choices)
    random_c = random.randrange(1, upper)
    choice = [c for c in choices if c['id'] == random_c][0]
    return choice