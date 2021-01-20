#Roll the Dice
import random

doubles = 0
avg1 = 0
avg2 = 0
count = 1

while True:
    userData = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
    if (userData == 4) or (userData == 6) or (userData == 8) or (userData == 10) or (userData == 12) or (userData == 20):
        print("Thanks! Here we go ...")
        break
    else:
        print("Sorry, that is not a valid size.")

while True:
    dieOne = random.randint(1, userData)
    dieTwo = random.randint(1, userData)
    print("die number 1 is ", dieOne, "die number 2 is ", dieTwo, end=" ")
    print()
    if dieOne == dieTwo:
        doubles = doubles + 1
    avg1 = avg1 + dieOne
    avg2 = avg2 + dieTwo
    if dieOne == 1 and dieTwo == 1:
        break

    count += 1
    a = random.randint(1, dieOne)
    b = random.randint(1, dieTwo)

percent = round((doubles * 100) / count, 2)
avg1 = round(avg1 / count, 2)
avg2 = round(avg2 / count, 2)
print("You got snake eyes! Finally! On try number " + str(count) + "!")
print("Along the way you rolled doubles", doubles, "times (", percent, "% of all rolls were doubles)")
print("The average roll for die #1 was", avg1)
print("The average roll for die #2 was", avg2)






