testapp1
========

Run testapp1 in non compiled mode:

.. code-block:: sh

   python -c 'import testapp1.app'
   DEBUG:asyncio:Using selector: EpollSelector
  ======== Running on http://localhost:8080 ========
  (Press CTRL+C to quit)


Now test the old and the new asyncio syntax handlers

.. code-block:: sh

   curl -sS http://localhost:8080/old && curl -sS http://localhost:8080/new
  OLD SYNTAX
  NEW SYNTAX

Now, let's install testapp1 which will compile all code using cython:

.. code-block:: sh

   python setup.py install

  /home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/Cython/Distutils/old_build_ext.py:30: UserWarning: Cython.Distutils.old_build_ext does not properly han
  dle dependencies and is deprecated.
    "Cython.Distutils.old_build_ext does not properly handle dependencies "
  Compiling /home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/app.py because it changed.
  Compiling /home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/new_handlers.py because it changed.
  Compiling /home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/old_handlers.py because it changed.
  [1/3] Cythonizing /home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/app.py
  [2/3] Cythonizing /home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/new_handlers.py
  [3/3] Cythonizing /home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/old_handlers.py
  running install
  running bdist_egg
  running egg_info
  writing top-level names to testapp1.egg-info/top_level.txt
  writing testapp1.egg-info/PKG-INFO
  writing dependency_links to testapp1.egg-info/dependency_links.txt
  reading manifest file 'testapp1.egg-info/SOURCES.txt'
  writing manifest file 'testapp1.egg-info/SOURCES.txt'
  installing library code to build/bdist.linux-x86_64/egg
  running install_lib
  running build_py
  creating build
  creating build/lib.linux-x86_64-3.5
  creating build/lib.linux-x86_64-3.5/testapp1
  copying testapp1/__init__.py -> build/lib.linux-x86_64-3.5/testapp1
  running build_ext
  building 'testapp1.app' extension
  creating build/temp.linux-x86_64-3.5
  creating build/temp.linux-x86_64-3.5/home
  creating build/temp.linux-x86_64-3.5/home/vampas
  creating build/temp.linux-x86_64-3.5/home/vampas/projects
  creating build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack
  creating build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console
  creating build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas
  creating build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features
  creating build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp
  creating build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios
  creating build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1
  creating build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1
  gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/include/python3.5m -c /home/vampas/projects/Salt
  Stack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/app.c -o build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/app.o
  gcc -pthread -shared -L/home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/lib build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/app.o -
  o build/lib.linux-x86_64-3.5/testapp1/app.cpython-35m-x86_64-linux-gnu.so
  building 'testapp1.new_handlers' extension
  gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/include/python3.5m -c /home/vampas/projects/Salt
  Stack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/new_handlers.c -o build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1
  /new_handlers.o
  gcc -pthread -shared -L/home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/lib build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/new_han
  dlers.o -o build/lib.linux-x86_64-3.5/testapp1/new_handlers.cpython-35m-x86_64-linux-gnu.so
  building 'testapp1.old_handlers' extension
  gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/include/python3.5m -c /home/vampas/projects/Salt
  Stack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/old_handlers.c -o build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1
  /old_handlers.o
  gcc -pthread -shared -L/home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/lib build/temp.linux-x86_64-3.5/home/vampas/projects/SaltStack/console/raas/features/aiohttp/.scenarios/testapp-1/testapp1/old_han
  dlers.o -o build/lib.linux-x86_64-3.5/testapp1/old_handlers.cpython-35m-x86_64-linux-gnu.so
  creating build/bdist.linux-x86_64
  creating build/bdist.linux-x86_64/egg
  creating build/bdist.linux-x86_64/egg/testapp1
  copying build/lib.linux-x86_64-3.5/testapp1/app.cpython-35m-x86_64-linux-gnu.so -> build/bdist.linux-x86_64/egg/testapp1
  copying build/lib.linux-x86_64-3.5/testapp1/__init__.py -> build/bdist.linux-x86_64/egg/testapp1
  copying build/lib.linux-x86_64-3.5/testapp1/old_handlers.cpython-35m-x86_64-linux-gnu.so -> build/bdist.linux-x86_64/egg/testapp1
  copying build/lib.linux-x86_64-3.5/testapp1/new_handlers.cpython-35m-x86_64-linux-gnu.so -> build/bdist.linux-x86_64/egg/testapp1
  byte-compiling build/bdist.linux-x86_64/egg/testapp1/__init__.py to __init__.cpython-35.pyc
  creating stub loader for testapp1/app.cpython-35m-x86_64-linux-gnu.so
  creating stub loader for testapp1/new_handlers.cpython-35m-x86_64-linux-gnu.so
  creating stub loader for testapp1/old_handlers.cpython-35m-x86_64-linux-gnu.so
  byte-compiling build/bdist.linux-x86_64/egg/testapp1/app.py to app.cpython-35.pyc
  byte-compiling build/bdist.linux-x86_64/egg/testapp1/new_handlers.py to new_handlers.cpython-35.pyc
  byte-compiling build/bdist.linux-x86_64/egg/testapp1/old_handlers.py to old_handlers.cpython-35.pyc
  creating build/bdist.linux-x86_64/egg/EGG-INFO
  copying testapp1.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
  copying testapp1.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
  copying testapp1.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
  copying testapp1.egg-info/not-zip-safe -> build/bdist.linux-x86_64/egg/EGG-INFO
  copying testapp1.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
  writing build/bdist.linux-x86_64/egg/EGG-INFO/native_libs.txt
  creating 'dist/testapp1-0.0-py3.5-linux-x86_64.egg' and adding 'build/bdist.linux-x86_64/egg' to it
  removing 'build/bdist.linux-x86_64/egg' (and everything under it)
  Processing testapp1-0.0-py3.5-linux-x86_64.egg
  creating /home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/envs/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/testapp1-0.0-py3.5-linux-x86_64.egg
  Extracting testapp1-0.0-py3.5-linux-x86_64.egg to /home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/envs/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages
  Adding testapp1 0.0 to easy-install.pth file

  Installed /home/vampas/.dotfiles/.ext/pyenv/versions/3.5.2/envs/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/testapp1-0.0-py3.5-linux-x86_64.egg
  Processing dependencies for testapp1==0.0
  Finished processing dependencies for testapp1==0.0

And now, let's run the compiled version of testapp1:

.. code-block:: sh

   cd /tmp && python -c 'import testapp1.app'
   DEBUG:asyncio:Using selector: EpollSelector
  ======== Running on http://localhost:8080 ========
  (Press CTRL+C to quit)


Now test the old and the new asyncio syntax handlers:

.. code-block:: sh

   curl -sS http://localhost:8080/old && curl -sS http://localhost:8080/new

  <html>
    <head>
      <title>500 Internal Server Error</title>
    </head>
    <body>
      <h1>500 Internal Server Error</h1>
      Server got itself in trouble
    </body>
  </html>
  <html>
    <head>
      <title>500 Internal Server Error</title>
    </head>
    <body>
      <h1>500 Internal Server Error</h1>
      Server got itself in trouble
    </body>
  </html>

And the traceback on the server side:

.. code-block:: sh

  ERROR:aiohttp.web:Error handling request
  Traceback (most recent call last):
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/server.py", line 265, in start
      yield from self.handle_request(message, payload)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/web.py", line 96, in handle_request
      resp = yield from handler(request)
    File "/home/vampas/projects/SaltStack/console/asyncio/aiohttp-session/py35/aiohttp_session/__init__.py", line 130, in middleware
      raise RuntimeError("Expect response, not {!r}", type(response))
  RuntimeError: ('Expect response, not {!r}', <class 'generator'>)
  INFO:aiohttp.access:::1 - - [13/Dec/2016:13:42:37 +0000] "GET /old HTTP/1.1" 500 170 "-" "curl/7.51.0"
  ERROR:aiohttp.web:Error handling request
  Traceback (most recent call last):
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/server.py", line 265, in start
      yield from self.handle_request(message, payload)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/web.py", line 96, in handle_request
      resp = yield from handler(request)
    File "/home/vampas/projects/SaltStack/console/asyncio/aiohttp-session/py35/aiohttp_session/__init__.py", line 125, in middleware
      response = await handler(request)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/web_urldispatcher.py", line 113, in handler_wrapper
      result = yield from result
  TypeError: 'coroutine' object is not iterable
  INFO:aiohttp.access:::1 - - [13/Dec/2016:13:42:37 +0000] "GET /new HTTP/1.1" 500 170 "-" "curl/7.51.0"
  /home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/server.py:292: RuntimeWarning: coroutine 'new_handler' was never awaited
    yield from self.handle_error(500, message, None, exc)


testapp2
========

testapp2 just import the ``inspect`` module to try and trigger the cython asyncio patching.

Run testapp2 in non compiled mode:

.. code-block:: sh

   python -c 'import testapp2.app'
   DEBUG:asyncio:Using selector: EpollSelector
  ======== Running on http://localhost:8080 ========
  (Press CTRL+C to quit)


Now test the old and the new asyncio syntax handlers

.. code-block:: sh

   curl -sS http://localhost:8080/old && curl -sS http://localhost:8080/new
  OLD SYNTAX
  NEW SYNTAX

And now, let's run the compiled version of testapp2:

.. code-block:: sh

   cd /tmp && python -c 'import testapp2.app'
   DEBUG:asyncio:Using selector: EpollSelector
  ======== Running on http://localhost:8080 ========
  (Press CTRL+C to quit)


Now test the old and the new asyncio syntax handlers:

.. code-block:: sh

   curl -sS http://localhost:8080/old && curl -sS http://localhost:8080/new

  <html>
    <head>
      <title>500 Internal Server Error</title>
    </head>
    <body>
      <h1>500 Internal Server Error</h1>
      Server got itself in trouble
    </body>
  </html>
  <html>
    <head>
      <title>500 Internal Server Error</title>
    </head>
    <body>
      <h1>500 Internal Server Error</h1>
      Server got itself in trouble
    </body>
  </html>

And the traceback on the server side:

.. code-block:: sh

  ERROR:aiohttp.web:Error handling request
  Traceback (most recent call last):
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/server.py", line 265, in start
      yield from self.handle_request(message, payload)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/web.py", line 96, in handle_request
      resp = yield from handler(request)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp_session/__init__.py", line 134, in middleware
      raise RuntimeError("Expect response, not {!r}", type(response))
  RuntimeError: ('Expect response, not {!r}', <class 'generator'>)
  INFO:aiohttp.access:::1 - - [13/Dec/2016:13:51:46 +0000] "GET /old HTTP/1.1" 500 170 "-" "curl/7.51.0"
  ERROR:aiohttp.web:Error handling request
  Traceback (most recent call last):
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/server.py", line 265, in start
      yield from self.handle_request(message, payload)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/web.py", line 96, in handle_request
      resp = yield from handler(request)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp_session/__init__.py", line 129, in middleware
      response = yield from handler(request)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/web_urldispatcher.py", line 113, in handler_wrapper
      result = yield from result
  TypeError: 'coroutine' object is not iterable
  INFO:aiohttp.access:::1 - - [13/Dec/2016:13:51:46 +0000] "GET /new HTTP/1.1" 500 170 "-" "curl/7.51.0"
  /home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/server.py:292: RuntimeWarning: coroutine 'new_handler' was never awaited
    yield from self.handle_error(500, message, None, exc)


testapp3
========

testapp3 just import the ``inspect`` module on the request handlers modules to try and trigger the cython asyncio patching.

Run testapp3 in non compiled mode:

.. code-block:: sh

   python -c 'import testapp3.app'
   DEBUG:asyncio:Using selector: EpollSelector
  ======== Running on http://localhost:8080 ========
  (Press CTRL+C to quit)


Now test the old and the new asyncio syntax handlers

.. code-block:: sh

   curl -sS http://localhost:8080/old && curl -sS http://localhost:8080/new
  OLD SYNTAX
  NEW SYNTAX

And now, let's run the compiled version of testapp3:

.. code-block:: sh

   cd /tmp && python -c 'import testapp3.app'
   DEBUG:asyncio:Using selector: EpollSelector
  ======== Running on http://localhost:8080 ========
  (Press CTRL+C to quit)


Now test the old and the new asyncio syntax handlers:

.. code-block:: sh

   curl -sS http://localhost:8080/old && curl -sS http://localhost:8080/new
   OLD SYNTAX

  <html>
    <head>
      <title>500 Internal Server Error</title>
    </head>
    <body>
      <h1>500 Internal Server Error</h1>
      Server got itself in trouble
    </body>
  </html>

And the traceback on the server side:

.. code-block:: sh

  INFO:aiohttp.access:::1 - - [13/Dec/2016:13:57:57 +0000] "GET /old HTTP/1.1" 200 12 "-" "curl/7.51.0"
  ERROR:aiohttp.web:Error handling request
  Traceback (most recent call last):
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/server.py", line 265, in start
      yield from self.handle_request(message, payload)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/web.py", line 96, in handle_request
      resp = yield from handler(request)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp_session/__init__.py", line 129, in middleware
      response = yield from handler(request)
    File "/home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/web_urldispatcher.py", line 113, in handler_wrapper
      result = yield from result
  TypeError: 'coroutine' object is not iterable
  INFO:aiohttp.access:::1 - - [13/Dec/2016:13:57:57 +0000] "GET /new HTTP/1.1" 500 170 "-" "curl/7.51.0"
  /home/vampas/.dotfiles/.ext/pyenv/versions/Raas-3.5.2-features-aiohttp/lib/python3.5/site-packages/aiohttp/server.py:292: RuntimeWarning: coroutine 'new_handler' was never awaited
    yield from self.handle_error(500, message, None, exc)


testapp4
========

testapp4 decorates the new ``async def`` syntax handler with ``@async.coroutine``:

Run testapp4 in non compiled mode:

.. code-block:: sh

   python -c 'import testapp4.app'
   DEBUG:asyncio:Using selector: EpollSelector
  ======== Running on http://localhost:8080 ========
  (Press CTRL+C to quit)


Now test the old and the new asyncio syntax handlers

.. code-block:: sh

   curl -sS http://localhost:8080/old && curl -sS http://localhost:8080/new
  OLD SYNTAX
  NEW SYNTAX

And now, let's run the compiled version of testapp4:

.. code-block:: sh

   cd /tmp && python -c 'import testapp4.app'
   DEBUG:asyncio:Using selector: EpollSelector
  ======== Running on http://localhost:8080 ========
  (Press CTRL+C to quit)


Now test the old and the new asyncio syntax handlers:

.. code-block:: sh

   curl -sS http://localhost:8080/old && curl -sS http://localhost:8080/new
  OLD SYNTAX
  NEW SYNTAX
