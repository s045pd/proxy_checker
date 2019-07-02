from enum import Enum, unique

SERVER_LOCAL_PORT = 12888  # 这个是服务代理端口
SERVER_LOCAL_BIND_IP = "127.0.0.1"

SERVER_NET_PORT = 80
TEST_TIMEOUT = 3
TEST_RETRY_TIMES = 3

@unique
class PROXIES(Enum):
    NONE = "NONE"
    TRANSPARENT = "TRANSPARENT"
    ANONYMOUS = "ANONYMOUS"
    DISTORTING = "DISTORTING"
    ELITE = "ELITE"
    UNKNOW = "UNKNOW"


class IPs(Enum):
    CLIENT = "A.B.C.D"
    SERVER = "A.B.C.D"