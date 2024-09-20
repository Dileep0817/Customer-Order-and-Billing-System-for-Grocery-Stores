x=[1,2,[3,4],[5,6]]
s=0
for i in x:
    if type(i)==int:
        s=s+i
    elif type(i)==list:
        for j in i:
            s=s+j
print(s)
