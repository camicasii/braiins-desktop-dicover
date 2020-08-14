import socket
import json
import pandas as pd



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


def get_device_info(ip):
    try:
        commands = ('pools', 'summary', 'devdetails', 'devs', 'temps', 'fans')
        device = {}
        for command in commands:
            device[command.upper()] =  braiins_Socket(command, ip)[command.upper()]
        return device
    except Exception as e:
        #return {'STATUS':'E',"msg":"ip not found"}
        return False

def get_all_info_handler(ips:pd.DataFrame):
    all_device={}
    for ip in ips['ip']:
        response = get_device_info(ip)
        if response:
            all_device[ip]=response
    return all_device

def get_all_info():
    ips_df= pd.read_csv('./ips.csv')
    devices_info=get_all_info_handler(ips_df)
    return devices_info


def get_info_for_ip(ip):
    device={}
    try:
        device[ip]= get_device_info(ip)
        return device
    except Exception as e:
        return {'STATUS':'E',"msg":"ip not found"}

if __name__=="__main__":
    get_all_info()