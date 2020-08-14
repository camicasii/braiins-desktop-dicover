from nmap_tools import  scan_ips
from tools import braiins_Socket
import numpy as np
import pandas as pd
import sys

import asyncio

def save_csv(df:pd.DataFrame):
    df.to_csv('./ips.csv',index=False,header=True)

async  def discover_handler(subnet):
    try:
        ips_all=scan_ips(subnet)
        ips_devices=[]
        for ip in ips_all:
            device = braiins_Socket('fans', ip)
            if device:
                ips_devices.append(ip)

        ips_np =np.array(ips_devices)
        ips_df = pd.DataFrame(ips_np, columns=['ip'])
        save_csv(ips_df)
        return ips_df.to_json()
    except Exception as e:
        return False

def discover(subnet):
    devices=discover_handler(subnet)
    print(devices)



if __name__ == "__main__":
    discover(sys.argv[1])

