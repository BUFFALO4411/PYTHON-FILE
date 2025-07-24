num = int(input("Enter te number:"))

if num <=1:
    print("Nither prime not composite")
elif num == 2:
    print("prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("Composite Number")
            break
        else:
            print("Prime Number")
