import pyone
import ssl
import yaml

config = yaml.safe_load(open("config.yml"))
session = (
    str(config["frontend_username"]) + ":" + str(config["frontend_password"])
)
one = pyone.OneServer(
    "http://localhost:2633/RPC2", session=session, https_verify=False
)

for dsname, dstype in config["datastores"].items():
    template = {
        "NAME": str(dsname),
        "TM_MAD": "ceph",
        "TYPE": str(dstype),
        "DISK_TYPE": "RBD",
        "POOL_NAME": str(config["ceph_pool"]),
        "CEPH_HOST": str(config["monitor_fqdn"]),
        "CEPH_USER": str(config["ceph_username"]),
        "CEPH_SECRET": str(config["secret_uuid"]),
        "BRIDGE_LIST": "NONE",
    }
    if str(dstype) == "IMAGE_DS":
        template["DS_MAD"] = "ceph"
    one.datastore.allocate(template, 0)
