# a=[5,10,11,19,10]
# print(type(a))
# print("length of a:",len(a))
# print("maximum of a:",max(a))
# print("minimum of a:",min(a))
# print("sum of the list in  a:",sum(a))
# print(a[2])
# #a.pop()           #pop deletes last value in the list
# #a.pop()
# #b=a.pop()
# print(a)
# print(b) 


# e=[2,4,2,5,6,4,2,5,1,0]
# c=e.count(0)
# print(c)
# e.insert(1,40)
# print(e)
# e.append(606)
# print(e)
# e.extend([400,606,78])
# print(e)
  
#sort total sorts the list ,sorted is used to sort only one line........
#e.sort(reverse=False)#true= revers ai decendng hotha hai
# print(e)
# print(sorted(e,reverse=True))
# print(e)
# for i in range(len(e)):
#     print(e[i],end="")

# f=[9,1,4,3,10,5,7]
# max=f[0]
# for i in f:
#     
# if(max<i):
#         max=i
# print(max)

#length withut len() method

# l=0
# for i in f:
#     l=l+1
# print(l)

#sum withput sum()
# s=0
# for i in f:
#     s=s+i
# print(s)

f=[9,1,4,3,10,5,7]
# f[0],f[1]=f[1],f[0]
# print(f)
for i in range(len(f)):
    for j in range(len(f)-1):
        if(f[j]<f[j+1]):
            f[j],f[j+1]=f[j+1],f[j]
            print(f)