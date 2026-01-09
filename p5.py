a=int(input("enter a no "))
if(a<50):
    print("peak hot")
elif(a>=30)and(a<40):
    print("hot")
elif(a>20)and(a<30):
    print("sunny")
elif(a>10)and(a<20):
    print("winter")
elif(a>0)and(a<10):
    print("cool")
else:
    print("ice age")