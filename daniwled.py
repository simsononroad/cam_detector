import requests
from time import sleep
import json

wled_device_ip = "[your wled device ip]"
api_endpoint = f"http://{wled_device_ip}/json/state"

def wled(bright):
    json_data = {"on":True,"bri":bright,"transition":7,"mainseg":0,"seg":[{"id":0,"start":0,"stop":157,"grp":1,"spc":0,"of":0,"on":True,"frz":False,"bri":bright,"cct":127,"col":[[128,128,128],[0,0,0],[255,0,0]],"fx":0,"sx":0,"ix":105,"pal":2,"sel":True,"rev":False,"mi":False},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0}]}
    headers ={'content-type':'application/json'}
    r = requests.post(api_endpoint, data=json.dumps(json_data),headers=headers)

sleep(1)
wled(255)
sleep(1)