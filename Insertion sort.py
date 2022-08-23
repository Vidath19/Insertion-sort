list = []
n = input('Enter the numbers to be sorted')
len =0
num= n.split()
for i in num:
    list.append(int(i))
    len =len +1
for j in range(1,len):
    i =j
    while (i>0) and (list[i-1]>list[i]):
        key =list[i-1]
        list[i-1]=list[i]
        list[i]=key
        i =i -1
print(list)