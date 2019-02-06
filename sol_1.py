f=open("running-config.cfg",'r')
f=f.read()
f=f.split("\n")
final_list = list()
interface_list = list()
intdict=dict()
vlancheck = 0
def listoftup():
	for value in f:
		if "interface" in value:
			value= value.split()
			interface_list.append(value[1])
		if "nameif" in value:
			value=value.split()
			if "no" in value[0]:
				interface_list.append("null")
				final_list.append(tuple(interface_list))
				del interface_list[:]
			else:
				interface_list.append(value[1])
				final_list.append(tuple(interface_list))
				del interface_list[:]
return final_list

#print(listoftup())
def list_ifname_ip():
	global vlancheck
	for value in f:
		if "interface" in value:
			value=value.split()
			interface_list.append(value[1])
		if "nameif" in value:
			value=value.split()
			if "no" in value[0]:
				interface_list.append("null")
			else:
				interface_list.append(value[1])
		if "vlan" in value:
			value=value.split()
			interface_list.append(value[1])
			vlancheck = 1
		if "ip address" in value:
			if vlancheck == 0:
				interface_list.append("null")
			value=value.split()
                        if "no" in value[0]:
				interface_list.append("null")
				interface_list.append("null")
				intdict[interface_list[0]]=interface_list[1:]
				del interface_list[:]
				vlancheck = 0
			else:
				interface_list.append(value[2])
				interface_list.append(value[3])
				intdict[interface_list[0]]=interface_list[1:]
				del interface_list[:]
				vlancheck = 0
	return intdict
print(list_ifname_ip())

