import sys
import re
import json
import copy
from random import randint
from datetime import datetime, timedelta
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI, status, Response, Request, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel, Field
from loguru import logger
from simple_salesforce import Salesforce, SalesforceResourceNotFound
from modules.credentials import GetCredentials

fname = "blancco_dashboard"

operation_modes = ["Boxing Desktops","Boxing Laptops","Palleting Desktops","Palleting Boxes"]

#<cyan>{function}</cyan>:<cyan>{line}</cyan>
LOG_FORMAT_COLOR = "<green>{time:YYYY-MM-DD HH:mm:ss:SSS}</green> [<level>{level: <8}</level>] <red>{extra[client_ip]}</red> {extra[request]} <level>{message}</level> {extra[reply]}"
LOG_FORMAT_LOGFMT = 'timestamp={time:YYYY-MM-DD_HH:mm:ss:SSS} level={level} function={function} line={line} client_ip={extra[client_ip]} request="{extra[request]}" message="{message}" reply="{extra[reply]}"'
logger.configure(extra={"client_ip": None,"request": None,"reply": None})  # Default values
logger.remove()
logger.add(
    f"logs/{fname}.log",
    level="INFO",
    colorize=True,
    rotation="00:00",
    format=LOG_FORMAT_COLOR,
)
logger.add(
    f"logs/{fname}_grafana.log",
    level="DEBUG",
    colorize=False,
    rotation="00:00",
    format=LOG_FORMAT_LOGFMT,
)
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

API_VER = "v1"
MESSAGE_LIMIT = 200

tags_metadata = [
    {
        "name": "API",
        "description": "Main API endpoints to be called from the warehouse app",
    },
    {
        "name": "Misc",
        "description": "Miscellaneous endpoints for dev use",
    }
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before start -> yeild -> after stop
    start_time = datetime.now()
    logger.warning(f'*** Started {fname} | {start_time.strftime("%a %d %b %Y %H:%M")} ***')

    app.blancco_clients = {
        "00038723": {
            "wipe_progress":0,
            "ip_address":"192.168.0.14",
            "make":"HP",
            "model":"HP ProDesk 400 G5 SFF",
            "serial":"CZC9299Q4R",
            "disks": [
                    {   
                        "make":"KINGSTON",
                        "model":"SA400S37480G",
                        "serial":"50026B7380446B51",
                        "capacity":"1 TB",
                        "wipe_progress":0
                    }
                ]
            },
        "00036419": {
            "wipe_progress":0,
            "ip_address":"192.168.0.15",
            "make":"Dell Inc.",
            "model":"Latitude E7450",
            "serial":"8DLKN32",
            "disks": [
                    {   
                        "make":"WDC",
                        "model":"WD5000AZRX-00A8LB0",
                        "serial":"WD-WCC1U3722227",
                        "capacity":"500 GB",
                        "wipe_progress":0
                    },
                    {   
                        "make":"SanDisk",
                        "model":"SDSSDP128G",
                        "serial":"133968403263",
                        "capacity":"128 GB",
                        "wipe_progress":0
                    }
                ]
            },
        "00034568": {
            "wipe_progress":0,
            "ip_address":"192.168.0.16",
            "make":"Dell Inc.",
            "model":"Optiplex 7050",
            "disks": []
            }
        }
    yield

    del(app.blancco_clients)

    end_time = datetime.now()
    uptime = end_time - start_time
    uptime_str = str(uptime).split('.')[0]
    logger.warning(f"*** Stopped {fname} | uptime: {uptime_str} ***")

app = FastAPI(
    title="Warehouse Service API",
    description="A REST api service to allow the warehouse app to interact with salesforce",
    version = API_VER,
    contact={
        "name": "Blythe Richardson",
        "email": "blythe@turingtrust.co.uk"
        },
    openapi_tags=tags_metadata,
    lifespan=lifespan,
    logger=logger
)

"""
    GET: Retrieve an existing resource (read-only)
    POST: Create a new resource
    PUT: Update an existing resource
    PATCH: Partially update an existing resource
    DELETE: Delete a resource

    200: OK
    201: Created
    202: Accepted but not complete
    204: No Content

    400: Bad Request
    403: Forbidden
    404: Not Found
    408: Request Timeout

    500: Internal Server Error (Generic)
    501: Not Implemented
    503: Service Unavailable
"""
@app.get(f"/{API_VER}/" + "blancco_dashboard",status_code=status.HTTP_200_OK, tags=['API'], description="Dashboard showing a list of active blancco clients.")
async def render_dashboard(response: Response,request: Request):
    html_body = '<!DOCTYPE html><html>'
    html_body+= '<head> \
    <meta charset="utf-8"> \
    <meta name="viewport" content="width=device-width, initial-scale=1"> \
    <title>Barcode Lookup</title> \
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css"> \
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,1,0"/> \
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"/> \
    </head>'
    #html_body += '<meta http-equiv="refresh" content="30"> <!-- Refresh every 10 seconds -->'
    html_body += '<body><div class="box"><div class="columns is-multiline">'
    for assetid,state in app.blancco_clients.items():
        if state['disks']:
            total_progress = 0
            for disk in state['disks']:
                disk['wipe_progress'] += randint(5,20)
                if disk['wipe_progress'] > 100:
                    disk['wipe_progress'] = 100
                total_progress += disk['wipe_progress']

            state['wipe_progress'] = total_progress/len(state['disks'])

        progress_color = "is-success" if state['wipe_progress'] == 100 else "is-warning"
        html_body += f"""<div class="column is-one-fifth">
                            <div class="box">
                              <article class="media">
                                <div class="media-left">
                                  <span class="icon is-large">
                                    <i class="fa-solid fa-computer fa-2x"></i>
                                  </span>
                                </div>
                                <div class="media-content">
                                  <div class="content">
                                    <p>
                                      <strong>{assetid}</strong> <small>{state['ip_address']}</small>
                                      <br>{state['make']}, {state['model']}
                                      <progress class="progress {progress_color} is-medium" value="{state['wipe_progress']}" max="100">{state['wipe_progress']}%</progress>
                                    </p>"""
        for disk in state['disks']:
            html_body+=f"""
                                <article class="media">
                                <div class="media-left">
                                  <span class="icon is-medium">
                                    <i class="fa-solid fa-hard-drive fa-2x"></i>
                                  </span>
                                </div>
                                <div class="media-content">
                                  <div class="content">
                                    <p>
                                      <small>{disk['make']} | {disk['model']}</small>
                                      <br>SN: {disk['serial']} | {disk['capacity']}</br>
                                      <progress class="progress {progress_color} is-small" value="{disk['wipe_progress']}" max="100">{disk['wipe_progress']}%</progress>
                                    </p>
                                  </div>
                                </div>
                              </article>
                                """
        html_body+="""</div>
                                </div>
                                </article>
                            </div>
                        </div>"""
    html_body+='</div></div></body>'
    return HTMLResponse(html_body,200)

@app.get(f"/{API_VER}/" + "blancco/{assetid}",status_code=status.HTTP_200_OK, tags=['API'], description="Submit current blancco wiping status of a device")
async def submit_blancco_client_state(assetid: str,make: str, model: str,wipe_progress: int,ip_address: str,response: Response,request: Request):
    app.blancco_clients[assetid] = {"make":make,"model":model,"wipe_progress":wipe_progress, "ip_address":ip_address}
    return "OK"

@app.get("/", tags=['Misc'], description="Basic redirection to the docs page")
def redirect_to_docs(request: Request,response: Response) -> RedirectResponse:
    response.status_code=status.HTTP_301_MOVED_PERMANENTLY
    return RedirectResponse(f"{request.base_url}docs#")

if __name__ == "__main__":
    uvicorn.run("blancco_dashboard:app", port=5010, host="0.0.0.0", reload=False, log_level="info")
