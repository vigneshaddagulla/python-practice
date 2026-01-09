p=int(input("enter a no."))
for j in range(p,1,-1):
    a=" "

    for i in range(1,j):
        a=a+str(i)+" "
   
    print(((p-j)*" ")+ a)