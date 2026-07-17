from time import perf_counter

from runtime.runtime_sleep import RuntimeSleep


print("========== RUNTIME SLEEP ==========\n")

sleep = RuntimeSleep()

start = perf_counter()

sleep.wait(
    1.0
)

elapsed = perf_counter() - start

print(
    round(
        elapsed,
        2,
    )
)