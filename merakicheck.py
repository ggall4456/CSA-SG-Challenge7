from pprint import pprint
from webexteamssdk import WebexTeamsAPI
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException
import requests
import os

meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'

meraki = MerakiSdkClient(meraki_api_key)

#Current versions, note that I changed the "." to "-" after reviewing the list data
msversion = '11-31'
mrversion = '26-6-1'
mxversion = '15-27'
mvversion = '4-0'

checklist = []  #empty list for devices not at current levels
MR_count = 0    #define counter for MR devices
MS_count = 0    #define counter for MS devices
MX_count = 0    #define counter for MX devices
MV_count = 0    #define counter for MV devices

# Get Devices
devices = meraki.devices.get_network_devices(mynetwork)

for i in devices:
    if i["model"][:2] == "MR" and mrversion in i["firmware"]:
        MR_count += 1
    elif i["model"][:2] == "MS" and msversion in i["firmware"]:
        MS_count += 1
    elif i["model"][:2] == "MX" and mxversion in i["firmware"]:
        MX_count += 1
    elif i["model"][:2] == "MV" and mvversion in i["firmware"]:
        MV_count += 1
    else:
        checklist.append(i)

print ("Total switches that meet standard: ", MS_count)
print ("Total APs that meet standard: ", MR_count)
print ("Total Security Appliances that meet standard: ", MX_count)
print ("Total Cameras that meet standard: ", MV_count)
print ("Devices that will need to be manually checked: ")

for j in checklist:
    print("Serial#: " + j["serial"]+ ", Model#: " + j["model"])

WebexRoomID = "Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli"

#api = WebexTeamsAPI(access_token=' put personnal Webex bearer Token here')
#try:
#    message = api.messages.create(WebexRoomID, text="Report Completed")
#    print("New message created, with ID:", message.id)
#    print(message.text)
#except ApiError as e:
#    print(e)
