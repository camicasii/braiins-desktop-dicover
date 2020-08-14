from tools import get_all_info, get_info_for_ip
from discover import discover_handler
from fastapi import FastAPI
import json
import os

app=FastAPI()

@app.get('/discover/{subnet}')
async  def get_discover(subnet:str):
    devices= await  discover_handler(subnet)

    if devices:
        return {'STATE':True,'devices':json.loads(devices)}
    else:
        return {'STATE': False}

@app.get('/all_info')
async def get_all_info_():
    response =   await get_all_info()
    return response

@app.get('/info_ip/{ip}')
def get_info_ip(ip:str):
    return get_info_for_ip(ip)

if __name__=="__main__":
    #python3 -m venv ./virtual_environments
    #pip freeze > requirements.txt
    #pip  install -r requirements.txt


    os.system('uvicorn --port 3002 main:app')



