import classes.Strategies as strategies
from classes.Calculations import *


class Stats():
    def __init__(
            self, bet_results=None, user_input=None, bankroll_histories=None,
            bet_value_histories=None, sl_reached_count=None, sg_reached_count=None,
            broke_count=None, profitors_count=None, profits=None, loses=None, title=None):
        self.bet_results = bet_results
        self.user_input = user_input
        self.bankroll_histories = bankroll_histories
        self.bet_value_histories = bet_value_histories
        self.sl_reached_count = sl_reached_count
        self.sg_reached_count = sg_reached_count
        self.broke_count = broke_count
        self.profitors_count = profitors_count
        self.profits = profits
        self.loses = loses
        self.title = title
        
    @staticmethod
    def print_indicators_tutorial():
        print('\n'+'-'*120)
        print('''Expected Rate of Return:  A RoR of 3% means that you tend to win 3% of your stake in the long run.\n''')
        #print('''CDF Average from Binomial Distribution: ''')
        print('''Kelly criterion in percentage of capital: \n''')
        #print('''Risk of Ruin: \n''')
        print('''Percentage Broke: \n''')
        print('''Percentage Profited: \n''')
        print('''Percentage Survivors Who Profited: \n''')
        print('''Percentage Survivors Who NOT Profited: \n''')
        print('''ROI Percentage Average (Return On Investment Percentage Average): \n''')
        print('''Yield Percentage Average: \n''')
        print('''Final Bankroll Average: \n''')
        print('''Average Profit: \n''')
        print('''Average Loses: \n''')
        print('''Expected Profit: \n''')
        print('''Expected Loss: ''')
        print('-'*120)
        
    def __get_general_calculations(self):
        '''General Stats'''
        self.rate_of_return = calculate_expected_rate_of_return(self.user_input)
        self.cdf_average = calculate_cdf_average_from_binomial_distribution(
           self.user_input, self.bet_results)
        
    def __get_strategy_calculations(self):
        # risk_of_ruin = calcule_risk_of_ruin(
        #    strategies.strategies_list[0], user_input)
        self.broke_percentage = calculate_broke_percentage(self.user_input, self.broke_count)
        self.profited_percentage = calculate_profited_percentage(self.user_input, self.profitors_count)
        self.survived_profited_percentage = calculate_survived_profited_percentage(self.user_input, self.broke_count, self.profitors_count)
        self.survived_no_profited_percentage = calculate_survived_no_profited_percentage(self.user_input, self.broke_count, self.profitors_count)
        self.roi_percentage_average = calculate_roi_percentage_average(self.user_input, self.bankroll_histories)
        self.yield_percentage_average = calculate_yield_percentage_average(self.user_input, self.bankroll_histories, self.bet_value_histories)
        self.average_of_number_of_bets = calculate_average_of_number_of_bets(self.user_input, self.bet_value_histories)
        self.final_bankroll_average = calculate_final_bankroll_average(self.user_input, self.bankroll_histories)
        self.average_profit = calculate_average_profit(self.profits)
        self.average_loses = calculate_average_loses(self.loses)
        self.expected_profit = calculate_expected_profit(self.average_profit, self.profited_percentage)
        self.expected_loss = calculate_expected_loss(self.average_loses, self.profited_percentage)
        
    def print_general_stats(self):
        self.__get_general_calculations()
        print('\n'+'-'*120)
        print('*GENERAL STATISTICS*')
        print(f'Expected Rate of Return: {self.rate_of_return}%')
        #print(f'CDF Average from Binomial Distribution: {self.cdf_average}%')
        print('-'*120)
        
    def print_strategy_stats(self, kelly_percentage=None) -> None:
        self.__get_strategy_calculations()
        print('\n'+'-'*120)
        print(f'*{self.title.upper()}*')

        if kelly_percentage is not None:
            print(f'Kelly criterion in percentage of capital: {round(kelly_percentage*100,2)}%\n')

        # print(f'Risk of Ruin: {risk_of_ruin}%')
        print(f'Percentage Broke: {self.broke_percentage}% ({self.broke_count} of {self.user_input["samples"]})')
        print(f'Percentage Profited: {self.profited_percentage}% ({self.profitors_count} of {self.user_input["samples"]})')
        print(f'Percentage Survivors Who Profited: {self.survived_profited_percentage}% ({self.profitors_count} of {self.user_input["samples"] - self.broke_count})')
        print(f'Percentage Survivors Who NOT Profited: {self.survived_no_profited_percentage}% ({(self.user_input["samples"] - self.broke_count) - self.profitors_count} of {self.user_input["samples"] - self.broke_count})\n')
        
        print(f'ROI Percentage Average: {self.roi_percentage_average}%')
        print(f'Yield Percentage Average: {self.yield_percentage_average}%\n')

