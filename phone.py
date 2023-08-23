l=[]
while True:
    A=input()
    if A=='Q' or A=='q':
          break
    l.append(A)
if len(l)<5 or len(l)>5:
    print("INPUT LIMIT IS 5")
else:
    count=0
    for i in l:
        if i.isdigit() and len(i)==10:
            count+=1
    print(count)
    