from runtime.runtime_settings import RuntimeSettings

print("========== RUNTIME SETTINGS ==========\n")

settings = RuntimeSettings()

print("Heartbeat:")
print(settings.heartbeat_interval)

print()

print("Scanner:")
print(settings.scanner_interval)

print()

print("Health Check:")
print(settings.health_check_interval)

print()

print("Reconnect Delay:")
print(settings.reconnect_delay)

print()

print("Max Reconnects:")
print(settings.max_reconnect_attempts)

print()

print("Shutdown Timeout:")
print(settings.shutdown_timeout)