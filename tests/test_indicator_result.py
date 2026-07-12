from models.indicator_result import IndicatorResult


result = IndicatorResult(
    name="EMA",
    output_name="EMA_20",
    values=[None, None, 100.2, 101.5],
    parameters={
        "period": 20
    }
)

print(result.name)
print(result.output_name)
print(result.values)
print(result.parameters)

print(result.first)
print(result.last)
print(result.count)
print(result.is_empty)