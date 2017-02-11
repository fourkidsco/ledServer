import asyncio
from aiohttp import web
from optparse import OptionParser

def getQs(qs):
    qss=qs.split('&')
    qsdict={}

    for i in qss:
        ii = i.split('=')
        qsdict[ii[0]]=ii[1]
    return qsdict

async def handle(request):
    index = open("index.html", 'rb')
    print(request)
    content = index.read()
    return web.Response(body=content,content_type='text/html')

async def handle2(request):
    print(request)
    print('request type:')
    print(type(request))
    print('request headers:')
    print(request.headers)
    print('requests each item:')
    print(request.method)
    print(request.rel_url)
    print(request.rel_url.query_string)
    print(request.rel_url.query)

    print('ledcnt:')
    print(app['ledcnt'])
    return web.Response(text='{ok}',content_type='application/json')

async def put_ledcnt(request):
    print(request)
    print('request type:')
    print(type(request))
    print('request headers:')
    print(request.headers)
    print('requests each item:')
    print(request.method)
    print(request.rel_url)
    print(request.rel_url.query_string)
    print(request.rel_url.query)
    qs=request.rel_url.query_string
    qsdict=getQs(qs)
    app['ledcnt'] = qsdict['ledcnt']
    print('ledcnt:')
    print(app['ledcnt'])
    if app["game_is_running"] == False:
        asyncio.ensure_future(game_loop(app))
    returnString='{%s}' % (str(app['ledcnt']))
    return web.Response(text=returnString,content_type='application/json')


async def get_time(request):
    print(app['cnt'])

    returnString='{timeticks: %s}' % (str(app['cnt']))
    return web.Response(text=returnString,content_type='application/json')

async def wshandler(request):
    app = request.app
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    app["sockets"].append(ws)

    if app["game_is_running"] == False:
        asyncio.ensure_future(game_loop(app))
    while 1:
        print(app['ledcnt'])
        msg = await ws.receive()
        if msg.tp == web.MsgType.text:
            print("Got message %s" % msg.data)
            ws.send_str("Pressed key code: {}".format(msg.data))
        elif msg.tp == web.MsgType.close or\
             msg.tp == web.MsgType.error:
            break

    app["sockets"].remove(ws)
    print("Closed connection")

    return ws

async def game_loop(app):
    app["game_is_running"] == True
    while 1:
        for ws in app["sockets"]:
            ws.send_str("game loop says: tick" + str(app['cnt']))
        app['cnt'] += 1
        #if len(app["sockets"]) == 0:
        #    break
        print('main loop ledcnt: ' + str(app['ledcnt']))
        await asyncio.sleep(2)
    app["game_is_running"] == False


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-H', '--hostname',
                      action='store',
                      dest='httpHost',
                      default='localhost',
                      help='Hostname used for local http server (IP or hostname) [default: %default]')
    parser.add_option('-p', '--port',
                      action='store',
                      dest='httpPort',
                      default=8888,
                      help='Port for the local HTTP server [default: %default]')
    parser.add_option('-D', '--debug',
                      action='store',
                      dest='logLevel',
                      default='INFO',
                      help='DEBUG level, [ERROR|WARN|INFO|DEBUG] [default: %default]')
    
    (options, args) = parser.parse_args()
    
    httpHost = options.httpHost
    httpPort = int(options.httpPort)
    app = web.Application()

    
    app["sockets"] = []
    app["game_is_running"] = False
    app['cnt']=0
    app['ledcnt'] = 100
    
    app.router.add_route('GET', '/connect', wshandler)
    app.router.add_route('GET', '/', handle)
    app.router.add_route('GET', '/ledcnt', handle2)
    app.router.add_route('PUT', '/ledcnt', put_ledcnt)
    app.router.add_route('GET', '/time', get_time)
    
    web.run_app(app,host=httpHost,port=httpPort)
