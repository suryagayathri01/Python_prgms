def odd(n):
    return n%2==1
wo=list(filter(odd,range(10)))
print(wo)
d={'age':[4,8,2],'name':["dd","gg"]}
print(d.get("age",None))
print(d.values())
print(list[d.keys()])
print(d)