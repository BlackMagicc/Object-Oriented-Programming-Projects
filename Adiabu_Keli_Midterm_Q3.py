#Collatz Conjecture

num = -1
steps = 0
largestStep = 0
largestNum = num
secondLargest = 1
secLargestStep = 0

while num < 0:
    num = int(input("Please enter a positive integer: "))

while num > 0 and num != 1:

    steps += 1

    # Here we go!

    if num % 2 == 1:    # odd number
        num = num * 3 + 1
    elif num % 2 == 0:  # even number
        num = num // 2

    if largestNum < num:
        largestNum = num
        largestStep = steps

    if secondLargest < num < largestNum:
        secondLargest = num
        secLargestStep = steps

if num == 1:
    if steps != 0:
        print("It took", steps, "steps for the sequence to reach 1.")
    print("The largest number in the sequence was" + " " + str(largestNum) + " " + "(step = " + str(largestStep) + ").")
    print("The second largest number was" + " " + str(secondLargest) + " " + "(step = " + str(secLargestStep) + ").")

    # My favorite question is this one! Took me like 30 minutes , I definitely spent too long on this one