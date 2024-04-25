import requests
import socket
import yaml

config = yaml.safe_load(open("config.yml"))
url = "https://" + str(config["monitor_fqdn"]) + ":8443/api/auth"
headers = {"Accept": "application/vnd.ceph.api.v1.0+json"}
data = {
    "username": config["dashboard_username"],
    "password": config["dashboard_password"],
}
response = requests.post(url, headers=headers, json=data, verify=False)
url = "https://" + str(config["monitor_fqdn"]) + ":8443/api/host"
headers = {
    "Accept": "application/vnd.ceph.api.v0.1+json",
    "Authorization": "Bearer " + response.json()["token"],
}
data = {
    "addr": str(config["storage_ip"]),
    "hostname": str(socket.gethostname()),
    "labels": ["osd", "rbd"],
    "status": "available",
}
response = requests.post(url, headers=headers, json=data, verify=False)
