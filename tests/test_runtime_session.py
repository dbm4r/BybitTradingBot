from runtime.runtime_session import RuntimeSession

print("========== RUNTIME SESSION ==========\n")

session = RuntimeSession()

print("State:")
print(session.state.value)

print()

print("Started:")
print(session.started_at)

print()

print("Stopped:")
print(session.stopped_at)

print()

print("Reconnects:")
print(session.reconnect_count)

print()

print("Healthy:")
print(session.healthy)

print()

print("Metadata:")
print(session.metadata)