#decimal to binary then toggle it and again back to decimal
n=int(input())
b1=""
while(n>=1):
    temp=n%2
    if temp==1:
        temp=0
    elif temp==0:
        temp=1
    b1=str(temp)+b1
    n=n//2
leng=len(b1)-1
i=0
su=0
while i<len(b1):
    s=int(b1[i])*(2**leng)
    su+=s
    leng-=1
    i+=1
print(su)