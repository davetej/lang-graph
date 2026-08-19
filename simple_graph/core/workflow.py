from langgraph.graph import StateGraph,START,END

from core.state import State
from core.router import GameRouter

class GameWorkflow:

    def __init__(self):
        self.graph = StateGraph(State)

        self.graph.add_node('begin',self.start_game)
        self.graph.add_node('mind',self.chess)
        self.graph.add_node('hand',self.carrom)

        self.graph.add_edge(START,'begin')
        self.graph.add_conditional_edges('begin',GameRouter())
        self.graph.add_edge('mind',END)
        self.graph.add_edge('hand',END)

        self.app = self.graph.compile()

    def start_game(self, state: State):
        print('--- start game called ---')
        return {
            **state,
            "graph_info": state["graph_info"] + f" Received: {state['user_input']}."
    }

    def chess(self, state: State):
        print('--- Playing chess ---')
        return {
            **state,
            "selected_game": "chess",
            "graph_info": state["graph_info"] + " Chess selected."
        }

    def carrom(self, state: State):
        print('--- Playing carrom ---')
        return {
            **state,
            "selected_game": "carrom",
            "graph_info": state["graph_info"] + " Carrom selected."
        }

    def run(self,state:State):
        return self.app.invoke(state)