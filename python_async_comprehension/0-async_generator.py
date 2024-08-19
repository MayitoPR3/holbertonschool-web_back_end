"""
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

Yields:
i: yield a random number between 0 and 10

"""

import random
import asyncio


async def async_generator():
    """
    Create an asynchronous generator that yields numbers from 0 to 10.
    """
    for i in range(10):
        await asyncio.sleep(1)  # Simulate async delay for demonstration purposes. 0 seconds delay in this case.
        yield random(0, 10)
