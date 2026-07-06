import matplotlib.pyplot as plt


class ChartManager:

    @staticmethod
    def plot_close_price(df, symbol: str):

        plt.figure(figsize=(15, 7))

        plt.plot(df["timestamp"],df["close"],label="Close")
        plt.plot(df["timestamp"],df["SMA_20"],label="SMA 20")

        plt.title(f"{symbol} Historical Price")

        plt.xlabel("Date")

        plt.ylabel("Price (USDT)")

        plt.grid(alpha=0.3)

        plt.legend()

        plt.tight_layout()

        plt.savefig(f"charts/{symbol}_close.png")

        plt.show()