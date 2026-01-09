#to find hifhest repeated values

a=[1,1,1,2,2,3,4,100,5,4,2,3,2,1,0,5,5,5,5,5,5,5,5,5,1]
c=[]
for i in a:
    c.append(a.count(i))
m=max(c)
r="not get"
for i in a:
    if a.count(i)==m:
        r=i
print(r)

  