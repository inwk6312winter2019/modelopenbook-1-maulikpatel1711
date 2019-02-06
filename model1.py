f=open("running-config.cfg",'r')
f=f.read()
f=f.split("\n")
interface_list = list()
intdict=dict()
vlancheck = 0
def list_ifname_ip():
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
