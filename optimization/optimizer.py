from optimization.optimization_result import OptimizationResult


class Optimizer:

    def __init__(self):

        self.results = []

    def add_result(
        self,
        result: OptimizationResult
    ):

        self.results.append(result)

    def all_results(self):

        return self.results

    def clear(self):

        self.results.clear()
    def best_by_roi(self):

        return sorted(
            self.results,
            key=lambda result: result.roi,
            reverse=True
        )
    def print_report(self):

        print("\n========== OPTIMIZATION ==========\n")

        for result in self.best_by_roi():

            print(
                f"{result.strategy:<18}"
                f"ROI {result.roi:>8.2f}%   "
                f"Profit ${result.net_profit:>10.2f}   "
                f"Win {result.win_rate:>6.2f}%   "
                f"DD {result.max_drawdown:>7.2f}%   "
                f"{result.parameters}"
            )