import pyone, ssl, yaml
config = yaml.safe_load(open("config.yml"))
session = str(config["adminname"])+":"+str(config["adminpassword"])
one = pyone.OneServer("http://localhost:2633/RPC2", session=session, https_verify=False)

for dsname, dstype in config["datastores"].items():
    template = {
        "NAME": str(dsname),
        "TM_MAD": "ceph",
        "TYPE": str(dstype),
        "DISK_TYPE": "RBD",
        "POOL_NAME": str(config["dspool"]),
        "CEPH_HOST": str(config["dshost"]),
        "CEPH_USER": str(config["dsuser"]),
        "CEPH_SECRET": str(config["dssecret"]),
        "BRIDGE_LIST": "NONE"
    }
    if str(dstype) == "IMAGE_DS":
        template["DS_MAD"]= "ceph"
    one.datastore.allocate(template, 0)
    # one.datastore.allocate(
    #     {
    #     "TEMPLATE": {
    #         "NAME": str(x),
    #         "TM_MAD": "ceph",
    #         "TYPE": str(y),
    #         "DISK_TYPE": "RBD",
    #         "POOL_NAME": str(config["dspool"]),
    #         "CEPH_HOST": str(config["dshost"]),
    #         "CEPH_USER": str(config["dsuser"]),
    #         "CEPH_SECRET": str(config["dssecret"]),
    #         "BRIDGE_LIST": ""
    #     }
    # }, 0)



#     import pyone, ssl, json
# config = json.load(open("config.json"))
# session = str(config["adminname"])+":"+str(config["adminpassword"])
# one = pyone.OneServer("http://localhost:2633/RPC2", session=session, https_verify=False)
# for x, y in config["datastores"].items():
#     one.datastore.allocate(
#         {
#         "TEMPLATE": {
#             "NAME": str(x),
#             "DS_MAD": "ceph",
#             "TM_MAD": "ceph",
#             "TYPE": str(y),
#             "DISK_TYPE": "RBD",
#             "POOL_NAME": str(config["dspool"]),
#             "CEPH_HOST": str(config["dshost"]),
#             "CEPH_USER": str(config["dsuser"]),
#             "CEPH_SECRET": str(config["dssecret"]),
#             "BRIDGE_LIST": ""
#         }
#     }, 0)