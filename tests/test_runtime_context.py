from runtime.runtime_context import RuntimeContext
from runtime.runtime_lifecycle import RuntimeLifecycle
from runtime.runtime_session import RuntimeSession
from runtime.runtime_settings import RuntimeSettings

print("========== RUNTIME CONTEXT ==========\n")

session = RuntimeSession()

lifecycle = RuntimeLifecycle(
    session
)

settings = RuntimeSettings()

context = RuntimeContext(
    session=session,
    lifecycle=lifecycle,
    settings=settings,
)

print(context.session.state.value)

print()

print(
    context.settings.heartbeat_interval
)

print()

print(
    context.lifecycle.session.state.value
)

print()

print(context.exchange)

print(context.scheduler)