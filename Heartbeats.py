from urllib import parse, request

URL:str = "http://remote.besic.org/heartbeat/"


def sendHeartBeat(deviceID,deployment,lux,tmp,prs,hum):
    """Sends measurements to server for remote monitoring

    Args:
        deviceID (str): Relay ID
        deployment (str): Associated Deployment
        lux (float): Light intenstiy value
        tmp (float): Temperature value in deg C
        prs (float): Pressure value in Pa
        hum (float): Humidity value in %
    """
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
            res.read()
    except:
        print("err")
