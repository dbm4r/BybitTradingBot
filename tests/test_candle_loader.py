from scanner.candle_loader import CandleLoader


print("========== CANDLE LOADER ==========\n")


response = {
    "result": {
        "list": [
            [
                "1720000200000",
                "65000",
                "65200",
                "64800",
                "65100",
                "120.5",
                "7830000",
            ],
            [
                "1720000140000",
                "64800",
                "65100",
                "64700",
                "65000",
                "100.2",
                "6500000",
            ],
            [
                "1720000080000",
                "64500",
                "64900",
                "64400",
                "64800",
                "90.8",
                "5880000",
            ],
        ]
    }
}


series = CandleLoader.load(
    response=response,
    symbol="BTCUSDT",
    interval="1",
)


print("Symbol:")
print(series.symbol)

print()

print("Interval:")
print(series.interval)

print()

print("Candle Count:")
print(len(series.candles))

print()

for candle in series.candles:

    print("----------------")
    print("Timestamp:", candle.timestamp)
    print("Open:", candle.open)
    print("High:", candle.high)
    print("Low:", candle.low)
    print("Close:", candle.close)
    print("Volume:", candle.volume)
    print("Turnover:", candle.turnover)