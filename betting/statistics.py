def calculate_expected_rate_of_return(user_input):
    '''
    The expected return is the profit or loss an investor anticipates on an
    investment that has known or anticipated rates of return (RoR). It is
    calculated by multiplying potential outcomes by the chances of them
    occurring and then totaling these results.
    For example, if an investment has a 55% chance of gaining 87% and a 45%
    chance of losing 100%, the expected return is 2.85%
    (55% x 87% + 45% x -100% = 2.85%).

    A 'ror' of 3% means that you tend to win 3% of your stake in the long run.
    '''
    rate_of_return = round((user_input['win_rate']*user_input['payout_rate'] -
                            user_input['lose_rate']*1)*100, 2)
    # *1 because you lose your entire bet
    return rate_of_return