def replace_ip(file_name):
    file = open(file_name)
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    for line in file:
        line = line.strip()
        for word in line.split():
            a1.append(word)
    for i in range(len(a1)):
        if a1[1-i] != 'no' and a1[i] == 'ip' and a1[i+1] == 'address':
               a2.append(a1[i+2])
