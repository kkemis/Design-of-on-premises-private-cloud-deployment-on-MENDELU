import pyone, ssl, yaml, socket
config = yaml.safe_load(open("config.yml"))
session = str(config["adminname"])+":"+str(config["adminpassword"])
one = pyone.OneServer("http://"+config["endpoint"]+":2633/RPC2", session=session, https_verify=False)
one.host.allocate(str(socket.gethostname()),
                  "kvm",
                  "kvm",
                  0
                  )
datastorepool = one.datastorepool.info()
for datastore in datastorepool.DATASTORE:
    if datastore.NAME in config["datastores"]:
        bridges=datastore.TEMPLATE['BRIDGE_LIST']
        bridge = str(socket.gethostname())
        if bridges != "NONE":
            bridge = bridges + " " +bridge
        template = {
            "BRIDGE_LIST": bridge
        }
        one.datastore.update(datastore.ID, template, 1)
        # one.datastore.update(datastore.ID,
        #                      {
        #                          "TEMPLATE": {
        #                              "BRIDGE_LIST": str(datastore.TEMPLATE['BRIDGE_LIST'])+" "+str(socket.gethostname())
        #                          }
        #                      }, 1)
# datastorepool = one.datastorepool.info()
# d0 = datastorepool.DATASTORE[0]
# bridges = d0.TEMPLATE['BRIDGE_LIST']
# if bridges is None:
#     bridges = ""
# one.datastore.update(id,{
#     "TEMPLATE": {
#         "BRIDGE_LIST": bridges+" "+bridge
#     }
# }, 1)
