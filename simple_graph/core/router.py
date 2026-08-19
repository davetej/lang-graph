import random
from typing import Literal

from core.state import State

class GameRouter:

    def __call__(self,state: State) -> Literal['mind','hand']:
        if random.random() > 0.5:
            return 'mind'
        return 'hand'

    