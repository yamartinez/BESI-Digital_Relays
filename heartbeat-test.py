#!/usr/bin/python3
from urllib import parse, request

URL:str = "http://dev.remote.besic.org/heartbeat/relay"

data:dict = {
    "DeviceID" : "debugger-script",
    "DeploymentID" : "debug",
    "LUX" : 0.0,
    "TMP" : 0.0,
    "PRS" : 0.0,
    "HUM" : 0.0
}

encodeddata = parse.urlencode(data)
encodeddata = encodeddata.encode('ascii')

req = request.Request(URL, encodeddata)
with request.urlopen(req) as res:
    print(res.read())
