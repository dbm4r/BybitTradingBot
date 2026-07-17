from runtime.runtime_stop_token import RuntimeStopToken

print("========== RUNTIME STOP TOKEN ==========\n")

token = RuntimeStopToken()

print(token.running)

token.stop()

print(token.running)

token.reset()

print(token.running)