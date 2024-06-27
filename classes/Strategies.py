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
        
        for self.__sample_result in self.bet_results:
            bankroll_history = [self.user_input['initial_bankroll']]
            self.__bet_value = self.user_input['bet_value']
            bet_value_history = []
            self.__current_bankroll = self.user_input['initial_bankroll']
            self.sample_setup()
            for self.__bet_result_index, bet_result in enumerate(self.__sample_result):
                self.bet_value_calculator_non_fixed()
                self.__bet_value = round(self.__bet_value, 2)
                self.__bet(bet_result)
                
                broke = self.__broke_verify(broke)
                stoploss_reached = self.__stoploss_verify(stoploss_reached)
                stopgain_reached = self.__stopgain_verify(stopgain_reached)
                if broke or stoploss_reached or stopgain_reached:
                    self.__current_bankroll = bankroll_history[-1]
                    break
                
                bankroll_history.append(self.__current_bankroll)
                bet_value_history.append(self.__bet_value)

            if self.__profit_or_lose() > 0 and not (broke or stoploss_reached):
                profitors_count += 1
                profits.append(self.__profit_or_lose())
            else:
                loses.append(self.__profit_or_lose())
                
            if broke: broke_count += 1
            if stoploss_reached: sl_reached_count += 1
            if stopgain_reached: sg_reached_count += 1

            bankroll_histories.append(bankroll_history.copy())
            self.bet_value_histories.append(bet_value_history.copy())
        
        bet_count_histories = self.__get_bet_count_histories(bankroll_histories)

        stats: Stats = Stats(self.bet_results, self.user_input, bankroll_histories,
                             self.bet_value_histories, sl_reached_count, sg_reached_count,
                             broke_count, profitors_count, profits, loses, self.title)

        stats.print_strategy_stats()
        graph.config(bet_count_histories, bankroll_histories, self.title)
        return graph
