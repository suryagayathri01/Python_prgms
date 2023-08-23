s = "a2d10b5"
new=""
if len(s)%2==0:
    a=s[0::2]
    n=s[1::2]
    for i in range(len(n)):
        if (n[i].isdigit()):
            new=new+a[i]*int(n[i])
else:
    a=""
    n=""
    i=0
    ri=len(s)-1
    while i<=ri:
        if i==ri:
            new=new+s[i-1]*int(s[i])
            break
        if s[i].isdigit() and not s[i+1].isdigit():
            new=new+s[i-1]*int(s[i])
            i+=1
        elif s[i].isdigit() and s[i+1].isdigit():
            td=s[i]+s[i+1]
            new=new+s[i-1]*int(td)
            i+=2
        else:
            i+=1

print(str(new))