r=int(input())
c=int(input())
matrix=[[int(input())for j in range(c)]for i in range(r)]
large=0
max=0
for i in range(r):
    count=matrix[i].count(1)
    if count>max:
        large=i
        max=count
print(large+1)