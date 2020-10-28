from ncclient import manager
from router_info import router

config_template = open(
    "/Users/salborough/Documents/Work/Envs/networkingCodeSamples/Python/IOS-XE/ios_config.xml").read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="Sean edited here")

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.edit_config(netconf_config, target="candidate")

print(response)