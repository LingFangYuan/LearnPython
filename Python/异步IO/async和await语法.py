import asyncio
import threading


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 从Python3.5开始引入了新的语法async和await
# 1. 把@asyncio.coroutine替换为async
# 2. 把yield from 替换为await
