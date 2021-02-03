import random
count=0
num=random.randint(1,10)
while count<5:
    guess=int(input("請猜數字")
    count=count+1
    if num==guess:
        print("對")
        print("猜了"count,"次")
    elif guess>num:
        print("too big")
        print("猜了"count,"次")
     else:
         print("too smal")
         print("猜了"count,""次)