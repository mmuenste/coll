"""Configure Vlans and assign access switchports."""
from cli import *

# Define the switchport groups / interface numbers and according vlan
interface_group_vlan_10 = (10, [n for n in range(1, 11)])
interface_group_vlan_20 = (20, [n for n in range(11, 21)])
interface_group_vlan_30 = (30, [n for n in range(21, 31)])

interface_groups_vlans = [interface_group_vlan_10,
                          interface_group_vlan_20,
                          interface_group_vlan_30]

# prepare command to create Vlans and assign switchport to vlan
command = "configure terminal"
s = " ; "

for interface_group_vlan in interface_groups_vlans:
    command += "%svlan %s" % (s, interface_group_vlan[0])
    for interface in interface_group_vlan[1]:
        command += "%sinterface eth 1/%s%sswitchport" % (s, interface, s) +\
                   "%sswitchport mode access" % s +\
                   "%sswitchport access vlan %s" % (s, interface_group_vlan[0])

# execute command
cli(command)
