#Fibonacci Sequence

num1 = 0

while True:
    numm = int(input("Please enter a non-negative integer: "))
    if numm < 0:
        print("Sorry that is not valid!")
    else:
        break

num2 = 1
count = 0

if numm == 1:
   print(num1)

else:
   while count <= numm:
       print(num1, end=",")
       fib = num1 + num2
       num1 = num2
       num2 = fib
       count += 1