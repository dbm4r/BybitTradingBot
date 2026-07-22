

import random
from validation.monte_carlo_result import MonteCarloResult
class MonteCarloValidator:

    def __init__(
        self,
        iterations=1000,
    ):

        self.iterations = iterations

        self.results = []

    def validate(
        self,
        trades,
        initial_balance,
    ):

        self.clear()

        for iteration in range(
            self.iterations
        ):

            shuffled = random.sample(
                trades,
                len(trades),
            )

            equity = initial_balance

            equity_curve = [
                equity
            ]

            for trade in shuffled:

                equity += trade.net_profit

                equity_curve.append(
                    equity
                )

            result = MonteCarloResult(

                iteration=iteration + 1,

                roi=self.calculate_roi(
                    equity,
                    initial_balance,
                ),

                net_profit=equity - initial_balance,

                max_drawdown=self.calculate_drawdown(
                    equity_curve
                ),

                trades=len(shuffled),
            )

            self.results.append(
                result
            )

        return self.results
    def _calculate_statistics(self):

        rois = [
            result.roi
            for result in self.results
        ]

        drawdowns = [
            result.max_drawdown
            for result in self.results
        ]

    def clear(self):

        self.results.clear()

    def all_results(self):

        return self.results
    @staticmethod
    def calculate_roi(
        equity,
        initial_balance,
    ):

        return (
            (
                equity
                - initial_balance
            )
            /
            initial_balance
        ) * 100
    @staticmethod
    def calculate_drawdown(
        equity_curve,
    ):

        peak = equity_curve[0]

        max_drawdown = 0

        for equity in equity_curve:

            if equity > peak:

                peak = equity

            drawdown = (
                (peak - equity)
                / peak
            ) * 100

            max_drawdown = max(
                max_drawdown,
                drawdown,
            )

        return max_drawdown
    def best_result(self):

        if not self.results:
            return None

        return max(
            self.results,
            key=lambda result: result.roi,
        )
    def worst_result(self):

        if not self.results:
            return None

        return min(
            self.results,
            key=lambda result: result.roi,
        )
    def summary(self):

        if not self.results:
            return None

        rois = [
            result.roi
            for result in self.results
        ]

        drawdowns = [
            result.max_drawdown
            for result in self.results
        ]

        return {

            "iterations": len(self.results),

            "average_roi":
                sum(rois) / len(rois),

            "best_roi":
                max(rois),

            "worst_roi":
                min(rois),

            "average_drawdown":
                sum(drawdowns) / len(drawdowns),

            "worst_drawdown":
                max(drawdowns),
        }
    def print_report(
        self,
    ):

        summary = self.summary()

        if summary is None:

            print(
                "No Monte Carlo results available."
            )

            return

        print(
            "\n========== MONTE CARLO ==========\n"
        )

        print(
            f"Iterations         : "
            f"{summary['iterations']}"
        )

        print(
            f"Average ROI        : "
            f"{summary['average_roi']:.2f}%"
        )

        print(
            f"Best ROI           : "
            f"{summary['best_roi']:.2f}%"
        )

        print(
            f"Worst ROI          : "
            f"{summary['worst_roi']:.2f}%"
        )

        print(
            f"Average Drawdown   : "
            f"{summary['average_drawdown']:.2f}%"
        )

        print(
            f"Worst Drawdown     : "
            f"{summary['worst_drawdown']:.2f}%"
        )