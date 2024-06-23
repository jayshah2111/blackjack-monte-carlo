from scipy.constants import golden_ratio

def nth_fibonacci_number(n):
    return int(((golden_ratio**n) - (1 - golden_ratio)**n)/(5**(1/2)))