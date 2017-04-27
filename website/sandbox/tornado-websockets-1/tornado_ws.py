import tornado.ioloop
import tornado.web
import tornado.websocket
from time import sleep
from random import random
from tornado.options import define, options, parse_command_line

define("port", default=8888, type=int)
from tornado import gen

@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        print "New connection"
        self.write_message("Welcome!")

    def on_message(self, message):
        print "New message {}".format(message)
        self.write_message(message)
        res = fetch_coroutine(message)
        print "Fetched {}".format(str(res))
        self.write_message(str(res))
        

    def on_close(self):
        print "Connection closed"


app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/ws/', WebSocketHandler),
])


if __name__ == '__main__':
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
