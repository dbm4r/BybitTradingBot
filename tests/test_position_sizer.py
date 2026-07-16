from risk.position_sizer import PositionSizer

print("========== POSITION SIZER ==========\n")

available_capital = 2500
risk_percent = 0.02

entry_price = 100
stop_price = 95

quantity = PositionSizer.fixed_risk(
    available_capital=available_capital,
    risk_percent=risk_percent,
    entry_price=entry_price,
    stop_price=stop_price,
)

risk_amount = available_capital * risk_percent

print(f"Available Capital : ${available_capital:,.2f}")
print(f"Risk Percent      : {risk_percent:.0%}")
print(f"Risk Amount       : ${risk_amount:,.2f}")
print(f"Entry Price       : {entry_price}")
print(f"Stop Price        : {stop_price}")
print(f"Quantity          : {quantity:.2f}")