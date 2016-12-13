import asyncio
import inspect
from aiohttp import web
from aiohttp_session import get_session


async def new_handler(request):
    session = await get_session(request)
    session['old_syntax'] = '1'
    await asyncio.sleep(0.01)
    return web.Response(body=b'NEW SYNTAX\r\n')
