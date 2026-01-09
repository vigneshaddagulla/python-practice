#07/01
# a=[4,8,3,7,9,10,4,0]
# a.sort(reverse=True)
# print(a[-1])


a="amma"
# print(len(a))
l=(len(a)+1)*-1
r=""
for i in range(-1,l,-1):
    r=r+a[i]
print(r)
if a==r:
    print("palindrome")
else:
    print("not palindrome")