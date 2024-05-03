import pyone
import ssl
import yaml
import socket

config = yaml.safe_load(open("config.yml"))
session = (
    str(config["frontend_username"]) + ":" + str(config["frontend_password"])
)
one = pyone.OneServer(
    "http://" + config["frontend_fqdn"] + ":2633/RPC2",
    session=session,
    https_verify=False,
)
one.host.allocate(str(socket.gethostname()), "kvm", "kvm", 0)
datastorepool = one.datastorepool.info()
for datastore in datastorepool.DATASTORE:
    if datastore.NAME in config["datastores"]:
        bridges = datastore.TEMPLATE["BRIDGE_LIST"]
        bridge = str(socket.gethostname())
        if bridges != "NONE" or "":
            bridge = bridges + " " + bridge
        template = {"BRIDGE_LIST": bridge}
        one.datastore.update(datastore.ID, template, 1)
