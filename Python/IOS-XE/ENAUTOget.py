from ncclient import manager
#import logging
import xmltodict

#logging.basicConfig(Level=logging.DEBUG)

#settings used to authenticate
router = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345"
}

#create a filter that can be used when wanting to do a <get> netconf call for a specific interface
int_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces-state>
</filter>
"""



#longer method that we dont need to do
#with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"])

#use hostkey_verify=False as this is a public sandbox and it creates self generated keys and so we waont be able to verify them
with manager.connect(**router, hostkey_verify=False) as m:
    netconf_response = m.get(int_filter)

python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
op = python_response["interfaces-state"]["interface"]
config = python_response["interfaces"]["interface"]

print(f"name: {config['name']['#test']}")
print(f"Packets In: {op['statistics']['in-unicast-pkts']}")


