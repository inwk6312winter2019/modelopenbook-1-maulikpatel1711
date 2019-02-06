def int_and_int_name(file_name):
	file=open(file_name)
	my_list1=[]
	my_list2=[]
	my_list3=[]

	for line in file:
		line=line.strip()
		for word in line.split():
			my_list1.append(word)
for i in range(len(my_list1)):
		if my_list1[i]=='interface':
			my_list2.append(my_list1[i+1])	
		elif my_list1[i]=='nameif' or (my_list1[i]=='no' and my_list1[i+1]=='nameif'):

			if my_list1[i]=='no' and my_list1[i+1]=='nameif':
my_list3.append('no name')
			elif my_list1[i-1]!='no' and my_list1[i]=='nameif':
				my_list3.append(my_list1[i+1])
def list_ifname_ip(file_name):
	file=open(file_name)
	my_list1=[]
	my_list2=[]
	my_list3=[]
	dict={}
	for line in file:
		line=line.strip()
		for word in line.split():
			my_list1.append(word)
	for i in range(len(my_list1)):
            if my_list1[i]=='interface':
			my_list2.append(my_list1[i+1]) 
            elif my_list1[i]=='nameif' or (my_list1[i]=='no' and my_list1[i+1]=='nameif'):
