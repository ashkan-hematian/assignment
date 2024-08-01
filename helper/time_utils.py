import time
from typing import Dict, Any, Optional


class Time:
    start_time: float
    message = 'Execution time'

    def __init__(self, is_debugging: bool = True) -> None:
        self.isDebugging = is_debugging
        self.start()

    def start(self) -> None:
        self.start_time = time.perf_counter()

    def setMessage(self, message: str) -> None:
        self.message = message

    def print(self, *args: str) -> None:
        if len(args) == 0:
            message = self.message
        else:
            message = args[0]
        if self.isDebugging:
            print(message)

    def end(self) -> None:
        execution_time = time.perf_counter() - self.start_time
        minutes = execution_time // 60
        seconds = execution_time % 60

        self.print(f'{self.message}: {int(minutes)}:{int(seconds)}')
