from typing import Generator
import asyncio


def async_generator():
    """
    Create an asynchronous generator that yields numbers from 0 to 10.
    """
    for i in range(11):
        asyncio.sleep(1)  # Simulate async delay for demonstration purposes. 0 seconds delay in this case.
        yield i
