from core.workflow import GameWorkflow 

def main():
    workflow = GameWorkflow()
    state = {"graph_info": "", "selected_game": "", "round_no": 0}

    while True:
        user_input = input("Enter a message (or 'exit' to quit): ").strip()
        if user_input.lower() in {"exit", "quit", "q"}:
            break

        
        state["round_no"] += 1
        state["user_input"] = user_input
        state = workflow.run(state)
        print(state)

if __name__ == "__main__":
    main()