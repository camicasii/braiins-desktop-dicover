import os
import platform
from tools import  braiins_Socket
import db_sqlite as db

def ping(ip):
    if platform.system() == "Windows":
         alive = os.system(f'ping {ip} -n 1 -w 1')
    else:
        alive = os.system(f'ping -c 1 -W 1 {ip}')
        # alive = os.system(f'ping -c 1 -i 1 {net_ip}')
    return alive



def ping_handler(ips:list):
    ip_red = []
    for ip in ips:
        # ping ip
        alive = ping(ip)

        if alive == 0:
            ip_red.append(ip)

    return ip_red

def ping_handler(ip:str):
    ip_red = []
    # ping ip
    alive = ping(ip)

    if alive == 0:
        ip_red.append(ip)

    return ip_red

def ip_handler(subnet:str):
    ip_range = list(range(1, 255))
    ips = []
    for i in ip_range:
        net = subnet.split(".")
        net[len(net) - 1] = i
        net_ip = ".".join(map(str, net))
        ips.append(net_ip)
    device = ping_handler(ips)
    return device


def ip_handler(ips:list):
    devices = ping_handler(ips)
    return devices

def ip_handler(subnet, ip_start,ip_end):

    subnet = ip_start.split(".")
    net_start =ip_start
    net_end = ip_end
    subnet.pop()
    subnet = ".".join(map(str, subnet))
    ips = list(map(lambda x: f'{subnet}.{x}', range(net_start, net_end + 1)))

    devices = ping_handler(ips)

    return devices


def ip_handler(ip_start,ip_end):
    net_start = ip_start.split(".")
    net_end = ip_end.split(".")
    subnet = ip_start.split(".")
    net_start=net_start[len(net_start) - 1]
    net_end = net_end[len(net_end) - 1]
    subnet.pop()
    subnet= ".".join(map(str, subnet))
    ips = list(map(lambda x: f'{subnet}.{x}', range(net_start, net_end +1)))

    devices=ping_handler(ips)

    return devices



def discover(subnet:str):
    ip_red = ip_handler(subnet)
    antminer= list(map(lambda x: braiins_Socket('fans', x), ip_red))
    return antminer

def discover(subnet:list):
    ip_red = ip_handler(subnet)
    antminer = list(map(lambda x: braiins_Socket('fans', x), ip_red))
    return antminer

def discover(ip_start,ip_end):
    ip_red = ip_handler(ip_start,ip_end)
    antminer = list(map(lambda x: braiins_Socket('fans', x), ip_red))
    return antminer
def show_devices():
    devices = db.db_select_all()
    return devices
