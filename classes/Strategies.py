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
    
    def simulate_strategy(self):
        graph: PlotGraph = PlotGraph(self.user_input)

        self.__current_bankroll: Union[int, float] = self.user_input['initial_bankroll']
        self.__sample_result: List[bool] = self.bet_results[0][0]
        self.__bet_result_index: int = 0
        sl_reached_count: int = 0
        sg_reached_count: int = 0
        broke_count: int = 0
        profitors_count: int = 0
        profits: List[Union[int, float]] = []
        loses: List[Union[int, float]] = []
        bet_count_histories: List[List[int]] = []
        bankroll_histories: List[List[Union[int, float]]] = []
        self.bet_value_histories: List[List[Union[int, float]]] = []
        broke: bool = False
        stoploss_reached: bool = False
        stopgain_reached: bool = False

        self.strategy_setup()
        self.bet_value_calculator_fixed()