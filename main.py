from tools import discover,get_all_info,get_info_for_ip
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import os



app=FastAPI()

@app.get('/discover')
def get_discover():
    return 'discover'


@app.get('/all_info')

async def get_all_info_():
    response = await  get_all_info()
    print(response)
    return response

@app.get('/info_ip/{ip}')
def get_info_ip(ip:str):
    return get_info_for_ip(ip)

if __name__=="__main__":
    os.system('uvicorn --port 3002 main:app')



