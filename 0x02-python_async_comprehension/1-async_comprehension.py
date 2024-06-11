#!/usr/bin/env python3
"""
Import async_generator, write a coroutine called async_comprehension that takes no arguments
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing,
    then return the 10 random numbers.
    """
    return [n async for n in async_generator()]
