import socket
import json
import os
import asyncio

def braiins_Socket(command, ip):
    server_address = (ip, 4028)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(server_address)
            message = f'{{"command":"{command}"}}'.encode()
            sock.sendall(message)
            buffer = b''
            while True:
                chunk = sock.recv(1024)
                if chunk == b'':
                    break
                buffer += chunk
            response_str = buffer.decode(encoding="utf8")
            response_str = response_str[:len(response_str) - 1]
            response_dic = json.loads(response_str)
            return response_dic

    except Exception as e:
        return False


def ip_handler(subnet):
    ip_end = list(range(1, ))
    ip_red = []
    for i in ip_end:
        net = subnet.split(".")
        net[len(net) - 1] = i
        net_ip = ".".join(map(str, net))
        # ping ip
        alive = os.system('ping -c 1 -W 1 ' + net_ip)
        if alive == 0:
            ip_red.append(".".join(map(str, net)))
    return ip_red


def discover(subnet:str):
    ip_red = ip_handler(subnet)
    antminer= list(map(lambda x: braiins_Socket('fans', x), ip_red))
    return antminer

def discover(subnet:list):
    ip_red = subnet
    antminer = list(map(lambda x: braiins_Socket('fans', x), ip_red))
    return antminer

def get_device_info(ip):
    commands = ('pools', 'summary', 'devdetails', 'devs', 'temps', 'fans')
    device = {}
    for command in commands:
        device[command.upper()] = braiins_Socket(command, ip)[command.upper()]
    return device

def get_all_info():
    ips = list(map(lambda x: f'192.168.0.{x}', range(30, 35)))
    all_device={}
    for ip in ips:
        all_device[ip]=get_device_info(ip)
    return all_device

def get_info_for_ip(ip):
    device={}
    try:
        device[ip]=get_device_info(ip)
        return device
    except Exception as e:
        return {'STATUS':'E',"msg":"ip not found"}
