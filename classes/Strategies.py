from typing import Union, List
from abc import ABC, abstractmethod
from random import uniform
import math

from betting.PlotGraph import PlotGraph
from betting.Stats import Stats
from betting.statistical_calculations import *
from betting.utils import *


strategies_list = ['fixed_bettor', 'percentage_bettor', 'kelly_criterion',
                   'fixed_martingale', 'percentage_martingale', 'fixed_soros',
                   'percentage_soros', 'fixed_fibonacci', 'percentage_fibonacci',
                   'fixed_DAlembert']

class Strategies(ABC):
    def __init__(self, bet_results: List[List[bool]], user_input: dict, title: str):
        self.bet_results = bet_results
        self.user_input: dict = user_input
        self.title: str = title
        self.__bet_value = None