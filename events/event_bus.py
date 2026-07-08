class EventBus:

    def __init__(self):

        self.listeners = {}

    def subscribe(
        self,
        event_name,
        listener
    ):

        self.listeners.setdefault(
            event_name,
            []
        ).append(listener)

    def publish(
        self,
        event_name,
        data
    ):

        for listener in self.listeners.get(
            event_name,
            []
        ):

            listener(data)