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