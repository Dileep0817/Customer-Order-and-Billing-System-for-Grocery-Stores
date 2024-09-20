s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

num=4
k=0
for i in range(0,len(s)):
    if i%num==0:
        print(s[k:i-1])
        k=i
else:
    print(s[i:])
