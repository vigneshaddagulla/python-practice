a=""
p=int(input("enter a no."))
for i in range(1,p):
    a=a+str(i)+" "
    print((p-i-1)*" "+ a)