from engine.state_manager import StateManager
from engine.engine_state import EngineState

state = StateManager()

state.set_state(
    EngineState.SYNCHRONIZING
)

state.set_state(
    EngineState.READY
)

state.set_state(
    EngineState.PLACING_ORDER
)

state.set_state(
    EngineState.WAITING_FOR_FILL
)

state.set_state(
    EngineState.IN_POSITION
)

state.set_state(
    EngineState.EXITING_POSITION
)

state.set_state(
    EngineState.STOPPED
)