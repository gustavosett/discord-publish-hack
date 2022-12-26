import time, sys
from datetime import timedelta


def timer(delay: int):
    entry = delay
    for i in range(0, delay):
        entry -= 1
        sys.stdout.write(f"\r{timedelta(seconds=entry)} for the next bump...")
        sys.stdout.flush()
        time.sleep(1)