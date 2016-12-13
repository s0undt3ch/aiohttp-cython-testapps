import asyncio
from aiohttp import web
from aiohttp_session import get_session


@asyncio.coroutine
def old_handler(request):
    session = yield from get_session(request)
    session['old_syntax'] = '1'
    yield from asyncio.sleep(0.01)
    return web.Response(body=b'OLD SYNTAX\r\n')
