from common import current_global_ip, error_log
from conf import IPs, SERVER_LOCAL_PORT,SERVER_NET_PORT,SERVER_LOCAL_BIND_IP,TEST_TIMEOUT,TEST_RETRY_TIMES
from log import success,info,warning
import requests
from pprint import pprint
from retry import retry


# IP = current_global_ip(IPs.CLIENT.value)


@error_log()
@retry(tries=TEST_RETRY_TIMES)
def checker(ip,port=80,protocol='http', is_sysyem_proxy=False):
    proxy_uri = f"{protocol}://{ip}:{port}"
    warning(f"Testing: {proxy_uri}")
    proxies = None if is_sysyem_proxy else {"http": proxy_uri, "https": proxy_uri}

    server_port = SERVER_NET_PORT if SERVER_LOCAL_BIND_IP in ['localhost','127.0.0.1'] else SERVER_LOCAL_PORT
    server_url =f"http://{IPs.SERVER.value}:{server_port}?client={IPs.CLIENT.value}&proxy={ip}"

    info(f"target: {server_url}")

    resp = requests.get(server_url,proxies=proxies,timeout=TEST_TIMEOUT)
    return {proxy_uri: resp.json()}


def main():
    proxy_list = [("119.41.236.180",8010),("118.97.187.170",44355)]
    datas = list(map(lambda item: checker(*item), proxy_list))
    pprint(datas)


if __name__ == "__main__":
    main()
