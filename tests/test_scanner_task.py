from runtime.tasks.scanner_task import ScannerTask


print("========== SCANNER TASK ==========\n")


class DummyScanner:

    def __init__(self):

        self.executed = False

    def scan(
        self,
    ) -> None:

        self.executed = True

        print("Scanning market...")


scanner = DummyScanner()

task = ScannerTask(
    scanner=scanner,
)

task.run()

print()

print("Executed:")
print(scanner.executed)