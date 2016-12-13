import asyncio
import logging
from testapp4 import old_handlers
from testapp4 import new_handlers
from aiohttp import web
import aiohttp_session

logging.basicConfig(level=logging.DEBUG)
loop = asyncio.get_event_loop()

app = web.Application(loop=loop)
aiohttp_session.setup(app, aiohttp_session.SimpleCookieStorage())
app.router.add_get('/new', new_handlers.new_handler)
app.router.add_get('/old', old_handlers.old_handler)
web.run_app(app, host='localhost', port=8080)
