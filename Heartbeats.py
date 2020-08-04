from urllib import parse, request

URL:str = "http://remote.besic.org/heartbeat/"

def sendHeartBeat(deviceID,deployment,lux,tmp,prs,hum):
    data:dict = {
        "DeviceID" : deviceID,
        "DeploymentID" : deployment,
        "LUX" : lux,
        "TMP" : tmp,
        "PRS" : prs,
        "HUM" : hum
    }

    encodeddata = parse.urlencode(data)
    encodeddata = encodeddata.encode('ascii')


    req = request.Request(URL+'relay',encodeddata)
    try:
        with request.urlopen(req) as res:
            print(res.read())
    except:
        print("err")
