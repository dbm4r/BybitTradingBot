from scanner.market_scanner import MarketScanner
from runtime.runtime_task import RuntimeTask


class ScannerTask(RuntimeTask):

    def __init__(
        self,
        scanner: MarketScanner,
    ):

        self.scanner = scanner

    def run(
        self,
    ) -> None:

        self.scanner.scan()