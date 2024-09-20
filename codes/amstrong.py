num = int(input('enter a number: '))#153
bkp=num
c=0
while num>0:#15>0 - t
    num=num//10    #15//10=1
    c=c+1     #c=3
num=bkp      #153
s=0
while num>0:#153>0
    t=num%10 #153%10=3
    s=s+t**c
    num=num//10#0+3**3=27+5**3
print(s)
if s==bkp:
    print('amstrong')
else:
    print('not amstrong')
    
