s=input()
star=0;hashh=0
if(2<=len(s) and len(s)<=20):
    for i in s:
        if i=="*":
            star+=1
        elif i=="#":
            hashh+=1
        else:
            print("Wrong Input")
            exit()
    print(star-hashh)
else:
    print("Wrong Input")