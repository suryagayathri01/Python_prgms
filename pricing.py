n=int(input())
count=0
price=1
N=n
if(n==0):
    print(0)
    exit()
while(n>0):
    p=n%10
    n=n//10
    price*=p
print(price)
    