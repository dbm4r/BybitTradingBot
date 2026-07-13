from strategies.signal_type import SignalType

print(SignalType.OPEN_LONG)
print(SignalType.CLOSE_LONG)
print(SignalType.OPEN_SHORT)
print(SignalType.CLOSE_SHORT)
print(SignalType.HOLD)

print()

print(SignalType.OPEN_LONG.value)
print(SignalType.HOLD.value)