from ncclient import manager

#settings used to authenticate
router = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345"
}

#longer method that we dont need to do
#with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"])

#use hostkey_verify=False as this is a public sandbox and it creates self generated keys and so we waont be able to verify them
with manager.connect(**router, hostkey_verify=False) as m:
    print('hello world')