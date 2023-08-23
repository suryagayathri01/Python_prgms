'''def calc(a,b):
    while b:
        a,b=b,a%b
    return a
def find_gcd(num):
    gcd=num[0]
    for i in range(1,len(num)):
        while num[i]:
            gcd,num[i]=num[i],gcd%num[i]
    return gcd

def find_lcm(num):
    lcm=num[0]
    for i in range(1,len(num)):
        lcm=(lcm*num[i])//calc(lcm,num[i])
    return lcm
            

n=int(input())
nos=[int(input()).split()]
if 2<=n and n<=25:
    gcd_r=find_gcd(nos)
    lcm_r=find_lcm(nos)
    print(f"HCF={gcd_r} LCM={lcm_r}")
else:
    exit()
    '''

    
