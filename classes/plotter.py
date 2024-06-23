import matplotlib.pyplot as plt
import matplotlib.style as style
from typing import Union, List

from classes.utils import *
style.use('bmh')

class PlotGraph:
    def __init__(self, user_input: dict) -> None:
        self.user_input = user_input