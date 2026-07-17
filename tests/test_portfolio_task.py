from runtime.tasks.portfolio_task import PortfolioTask


print("========== PORTFOLIO TASK ==========\n")


class DummyPortfolio:

    def __init__(self):

        self.executed = False

    def process(
        self,
    ) -> None:

        self.executed = True

        print("Processing portfolio...")


portfolio = DummyPortfolio()

task = PortfolioTask(
    portfolio
)

task.run()

print()

print("Executed:")
print(portfolio.executed)