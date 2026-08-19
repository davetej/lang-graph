# Project Context

## Project purpose
A small LangGraph-based game workflow app built step by step from a simple graph into a production-style structure with class-based components and an API layer.

## Current state
- Initial graph concept is understood.
- The project is being structured from a simple graph into modular production layers.
- The next goal is to define the class architecture and then expose it through an API.

## Completed work
- Basic graph idea and flow were discussed.
- We identified the separation between state, routing, workflow, and service responsibilities.

## Important decisions
- Start with `State` as the workflow contract.
- Keep graph nodes simple and stateless aside from the state they return.
- Use a dedicated router class for conditional branching.
- Separate workflow assembly from app/service usage.

## Architecture / structure
- `state.py` — typed state schema
- `router.py` — routing logic
- `workflow.py` — graph build and node functions
- `service.py` — app-level orchestration
- `api.py` — FastAPI endpoints
- `main.py` — app startup

## Configuration / environment changes
None yet.

## Known issues
None at this stage.

## Next step
Define the class-by-class architecture and map the simple graph into a production structure before adding the API layer.

## Important constraints / requirements
- Keep the learning path incremental.
- Do not add complexity before the base flow is clear.
- Maintain a clean separation of responsibilities.
