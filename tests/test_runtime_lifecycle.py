from runtime.runtime_lifecycle import RuntimeLifecycle
from runtime.runtime_session import RuntimeSession

print("========== RUNTIME LIFECYCLE ==========\n")

session = RuntimeSession()

lifecycle = RuntimeLifecycle(
    session
)

print(session.state.value)

lifecycle.initialize()
print(session.state.value)

lifecycle.synchronize()
print(session.state.value)

lifecycle.start()
print(session.state.value)
print(session.started_at)

lifecycle.pause()
print(session.state.value)

lifecycle.error()
print(session.state.value)

lifecycle.stop()
print(session.state.value)
print(session.stopped_at)