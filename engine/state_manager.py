from engine.engine_state import EngineState


class StateManager:

    def __init__(self):

        self.state = EngineState.STARTING

    def set_state(
        self,
        state
    ):

        if self.state != state:

            print(
                f"[STATE] "
                f"{self.state.value} -> {state.value}"
            )

        self.state = state

    def get_state(self):

        return self.state

    def is_state(
        self,
        state
    ):

        return self.state == state