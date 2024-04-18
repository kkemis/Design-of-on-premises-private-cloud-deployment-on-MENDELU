import requests
import json
import os
import sys
import socket
# username = str(sys.argv[1])
# password = str(sys.argv[2])
# ip = str(sys.argv[3])
# monitor = str(sys.argv[4])
# hostname = str(sys.argv[5])
config = json.load(open("config.json"))
username = str(config["username"])
password = str(config["password"])
ip = str(config["ip"])
monitor = str(config["monitor"])
hostname = str(socket.gethostname())
# Get Token
url = "https://"+monitor+":8443/api/auth"
headers = {
    "Accept": "application/vnd.ceph.api.v1.0+json"
}
data = {
    "username": username,
    "password": password
}

response = requests.post(url, headers=headers, json=data, verify=False)

# print(response.json())
values = response.json()
token = values["token"]

url = "https://"+monitor+":8443/api/osd"
headers = {
    "Accept": "application/vnd.ceph.api.v1.0+json",
    "Authorization": "Bearer " + token
}
response = requests.get(url,headers=headers,verify=False)
# print(response.json())
# print(response.status_code)
# Add host
url = "https://"+monitor+":8443/api/host"
headers = {
    "Accept": "application/vnd.ceph.api.v0.1+json",
    "Authorization": "Bearer " + token
}
data = {
    "addr": ip,
    "hostname": hostname,
    "labels": [
        "osd",
        "rbd"
    ],
    "status": "available"
}
response = requests.post(url, headers=headers, json=data, verify=False)
# print(response.content) 