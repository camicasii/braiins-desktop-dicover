from tools import discover,get_all_info,get_info_for_ip
from flask import  Flask,json

import sys
sys.setrecursionlimit(10000)

app=Flask(__name__)

@app.route('/discover')
def get_discover():
    return 'discover'

@app.route('/all_info')
def get_all_info():
    response =get_all_info()
    return json.dumps(response)

@app.route('/info_ip/<string:ip>')
def get_info_ip(ip):
    return get_info_for_ip(ip)


if __name__ == "__main__":
    app.run(port=3001)