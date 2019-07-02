from conf import PROXIES, IPs, SERVER_LOCAL_PORT,SERVER_LOCAL_BIND_IP
from common import current_global_ip, is_ip
from log import info, success
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.netutil
import tornado.web


class Main(tornado.web.RequestHandler):
    async def get(self):
        info(self.request.headers)

        client_real_ip = self.get_argument("client", "").split(":")[0].strip() # 起始客户端提供IP
        proxy_ip = self.get_argument("proxy", None)  # 起始客户端提供代理IP

        x_real_ip = self.request.remote_ip  # 最后一级客户端IP
        x_forwarded_for = self.request.headers.get("X-Forwarded-For", "")
        x_forwarded_for_ip = x_forwarded_for.split(",")[0].strip()  # 第一个代理IP地址
        http_via = self.request.headers.get("Via")

        types = PROXIES.UNKNOW.value
        info(
            f"client_real_ip: {client_real_ip}\nremote_addr: {x_real_ip}\nvia: {http_via}\nx_forwarded_for: {x_forwarded_for}"
        )
        if is_ip(client_real_ip):  # 是否有给定真实地址
            if http_via:  # 是否有via
                if proxy_ip and is_ip(proxy_ip):  # 是否有指明代理
                    if x_forwarded_for_ip == client_real_ip and x_real_ip == proxy_ip:  # 透明代理
                        types = PROXIES.TRANSPARENT.value
                    elif x_real_ip == proxy_ip and x_forwarded_for_ip != client_real_ip:  # 匿名代理
                        types = PROXIES.ANONYMOUS.value
                    elif x_forwarded_for_ip != proxy_ip and x_forwarded_for_ip:  # 随机代理
                        types = PROXIES.DISTORTING.value
            else:
                if client_real_ip != x_real_ip:
                    types = PROXIES.ELITE.value  # 高匿代理
                else:
                    types = PROXIES.NONE.value  # 未使用代理
            self.write({"status": True, "msg": "ok", "types": types, "end_ip": x_real_ip})
        else:
            self.write(
                {
                    "status": False,
                    "msg": "check your client ip",
                    "types": types,
                    "end_ip": x_real_ip,
                }
            )


def make_app():
    settings = {"autoreload": True, "gzip": True}
    return tornado.web.Application([(r"/", Main)], **settings)


if __name__ == "__main__":
    sockets = tornado.netutil.bind_sockets(SERVER_LOCAL_PORT, SERVER_LOCAL_BIND_IP)
    app = tornado.httpserver.HTTPServer(make_app(), xheaders=True)
    app.add_sockets(sockets)
    success("server start!")
    tornado.ioloop.IOLoop.current().start()
