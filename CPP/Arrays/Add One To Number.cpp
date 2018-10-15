//
// Created by Amit Kumar on 13/10/18.
//



t = list(map(str,a))
p = ''.join(t)
num = int(p)+1
num = str(num)
temp = []
for i in range(len(num)):
temp.append(int(num[i]))

return temp