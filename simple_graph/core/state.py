from typing_extensions import TypedDict

class State(TypedDict):
    user_input: str
    graph_info: str
    selected_game: str
    round_no: int

