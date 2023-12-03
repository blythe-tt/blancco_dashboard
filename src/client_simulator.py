import requests
from random import randint
from time import sleep

blancco_clients = {
        "00023546": {
            "wipe_progress":0,
            "ip_address":"192.168.0.100",
            "make":"LENOVO",
            "model":"x280"
            },
        "00029468": {
            "wipe_progress":0,
            "ip_address":"192.168.0.101",
            "make":"HP",
            "model":"EliteBook G5"
            },
        "00024568": {
            "wipe_progress":0,
            "ip_address":"192.168.0.102",
            "make":"Dell Inc.",
            "model":"Optiplex 7050",
            }
        }

all_done = False
while not all_done:
    for assetid,state in blancco_clients.items():
        state['wipe_progress'] += randint(8,20)
        if state['wipe_progress'] >= 100:
            state['wipe_progress'] = 100
        requests.get(f"http://localhost:5010/v1/blancco/{assetid}?make={state['make']}&model={state['model']}&wipe_progress={state['wipe_progress']}&ip_address={state['ip_address']}")
    sleep(1)