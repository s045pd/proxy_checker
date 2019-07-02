import copy
import os
import time
from contextlib import contextmanager

import socket
import ipaddress
from log import info, error, warning, success

import re

def is_ip(value):
    if re.match(
        "^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$",
        value,
    ):
        return True


def error_log(target="", default=None, raise_err=False, raise_exit=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                error(
                    f"[{target} {  func.__name__  if '__name__' in dir(func) else ''  }]: {e}"
                )
                if raise_exit:
                    exit()
                elif raise_err:
                    raise e
                return default

        return wrapper

    return decorator


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def current_global_ip(default_ip):
    net_ip = get_host_ip()
    ip = net_ip if ipaddress.IPv4Address(net_ip).is_global else default_ip
    if not ip:
        warning("please set default server ip.")
        exit()
    info(f"current ip: {ip}")
    return ip
