from classes.BetGenerator import BetGenerator
from classes.Strategies import FixedBettor, PercentageBettor, KellyCriterion, FixedMartingale
from classes.PlotGraph import PlotGraph
from classes.Stats import Stats

user_input = {
    'samples': 20, # Number of simulations
    'bet_count': 10000, # Number of bets per simulation
    'win_rate': 0.4865,  # range: 0.0000-1.0000
    'lose_rate': 0.5135,  # range: 1.0000-0.0000
    'payout_rate': 1.0000,  # range: 0.0000-2.0000 generally, but you choose. 1 means 100% of the bet.
    'initial_bankroll': 100, # How much money you have in each simulation
    'currency': '$', # Currency symbol
    'minimum_bet_value': 1, # None means no minimum bet
    'maximum_bet_value': 50000,  # None means no maximum bet value
    'stoploss': None, # None means no stop loss
    'stopgain': None, # None means no stop gain
    'bet_value': 1, # Isn't used in all strategies
    'bet_percentage': 0.0100,  # Isn't used in all strategies, range: 0.0000-1.0000
}

bet_results = BetGenerator(user_input).generate_random_bet_results()
data = (bet_results, user_input)

def main():
    return 0

if __name__ == '__main__':
    main()