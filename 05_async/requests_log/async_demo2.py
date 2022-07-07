import asyncio
from types import coroutine


async def execute(x):
    print('Number:', x)

coroutine = execute(10)

task = asyncio.ensure_future(coroutine)
print('Task: ', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task', task)
print('After calling loop')