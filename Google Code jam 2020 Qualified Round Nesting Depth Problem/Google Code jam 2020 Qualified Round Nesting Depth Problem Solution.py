from sys import stdin, stdout
t = int(stdin.readline().strip())


results = []


for i in range(t):
    string = stdin.readline().strip()
    lstring = list(string)
    nd = 0
    newl = []
    for x in lstring:
        for j in range(int(x)):
            newl.append('(')
        newl.append(x)
        for j in range(int(x)):
            newl.append(')')




    str_newl = ''.join(newl)


    while ')(' in str_newl:
        list_snewl = str_newl.split(')(')
        str_newl = ''.join(list_snewl)


    results.append(str_newl)
    
for index in range(len(results)):
    print('Case #{}: {}'.format(index + 1, results[index]))


