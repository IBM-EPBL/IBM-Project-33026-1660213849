import json 
import wiotp.sdk.device
import time

myConfig = {
    "identity": {
        "orgId": "9o069i",
        "typeId": "manimd",
        "deviceId": "manimd12"
     },
     "auth": {
        "token": "manimd07"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    name = "mani"
    #in area location

    latitude=11.225894
    longitude=76.980855

    #out area location

    latitude = 11.226767
    longitude = 76.988299
    mydata = {'name': name, 'lat': latitude, 'lon': longitude}
    client.publishEvent("IoTSensor", "json", data=mydata, qos=0, onPublish=None)
    print("Data published to IBM IOT platform :", mydata)
    time.sleep(5)

client.disconnect()