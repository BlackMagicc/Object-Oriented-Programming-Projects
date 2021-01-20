from Project.my_functions import *
import random

# Arithmetic Game !

while True:
    max_prob = int(input("How many problems would you like to attempt? "))
    if max_prob < 0:
        print("Invalid number, try again")
    else:
        break

while True:
    wide = int(input("How wide do you want your digits to be? 5-10: "))
    if (wide < 5) or (wide > 10):
        print("Invalid width, try again")
    else:
        break

while True:
    character = input("What character would you like to use? ")
    if len(character) > 1:
        print("String too long, try again")
    else:
        print("Here we go!")
        break


def random_number(range_start, range_end, width, pattern):
    range_start = 0
    range_end = 9
    rand_num = random.randint(range_start, range_end)

    if rand_num == 0:
        display = number_0(width, pattern)
    elif rand_num == 1:
        display = number_1(width, pattern)
    elif rand_num == 2:
        display = number_2(width, pattern)
    elif rand_num == 3:
        display = number_3(width, pattern)
    elif rand_num == 4:
        display = number_4(width, pattern)
    elif rand_num == 5:
        display = number_5(width, pattern)
    elif rand_num == 6:
        display = number_6(width, pattern)
    elif rand_num == 7:
        display = number_7(width, pattern)
    elif rand_num == 8:
        display = number_8(width, pattern)
    elif rand_num == 9:
        display = number_9(width, pattern)

    return display


def random_operator(width, pattern):
    x = '-'
    y = '+'
    op = random.choice([x, y])

    if op == '-':
        return minus(width, pattern)
    else:
        return plus(width, pattern)


def quiz(width, pattern):
    return random_number(0, 9, width, pattern) + "\n \n" + random_operator(width, pattern) + "\n \n" + random_number(0,
                                                                                                                     9,
                                                                                                                     width,
                                                                                                                     pattern)


for i in range(max_prob):
    print("\n" + "What is . . . . . " + "\n")
    count = 0
    x = quiz(wide, character)
    print(x)
    ls = ""
    split = x.splitlines()
   # newsplit = split.split()
  #  print(newsplit)
    print(split)
    num = split[0: 20]
    num2 = [split[-1]]
    if plus(wide, character) in split or minus(wide, character) in split:
        print("You did it")
    print("num= " + str(num))
    print("num2= " + str(num2))

    if number_0(wide, character) in num:
        num = 0
    elif number_1(wide, character) in num:
        num = 1
    elif number_2(wide, character) in num:
        num = 2
    elif number_3(wide, character) in num:
        num = 3
    elif number_4(wide, character) in num:
        num = 4
    elif number_5(wide, character) in num:
        num = 5
    elif number_6(wide, character) in num:
        num = 6
    elif number_7(wide, character) in num:
        num = 7
    elif number_8(wide, character) in num:
        num = 8
    elif number_9(wide, character) in num:
        num = 9

    if number_0(wide, character) in num2:
        num2 = 0
    elif number_1(wide, character) in num2:
        num2 = 1
    elif number_2(wide, character) in num2:
        num2 = 2
    elif number_3(wide, character) in num2:
        num2 = 3
    elif number_4(wide, character) in num2:
        num2 = 4
    elif number_5(wide, character) in num2:
        num2 = 5
    elif number_6(wide, character) in num2:
        num2 = 6
    elif number_7(wide, character) in num2:
        num2 = 7
    elif number_8(wide, character) in num2:
        num2 = 8
    elif number_9(wide, character) in num2:
        num2 = 9
    print("num= " + str(num))
    print("num2= " + str(num2))
   # for j in x[0: character.find(character)]:

"""
        print(j, end=" ")
        if j.contains(number_0(wide, character)):
            num = 0
        if j.contains(number_1(wide, character)):
            num = 1
        if j.contains(number_2(wide, character)):
            num = 2
        if j.contains(number_3(wide, character)):
            num = 3
        if j.contains(number_4(wide, character)):
            num = 4
        if j.contains(number_5(wide, character)):
            num = 5
        if j.contains(number_6(wide, character)):
            num = 6
        if j.contains(number_7(wide, character)):
            num = 7
        if j.contains(number_8(wide, character)):
            num = 8
        if j.contains(number_9(wide, character)):
            num = 9
        print("j = " + j, end=" ")
        
    for n in reversed(x)[[x-1]: character.find(character)]:
        if n.contains(number_0(wide, character)):
            num2 = 0
        if n.contains(number_1(wide, character)):
            num2 = 1
        if n.contains(number_2(wide, character)):
            num2 = 2
        if n.contains(number_3(wide, character)):
            num2 = 3
        if n.contains(number_4(wide, character)):
            num2 = 4
        if n.contains(number_5(wide, character)):
            num2 = 5
        if n.contains(number_6(wide, character)):
            num2 = 6
        if n.contains(number_7(wide, character)):
            num2 = 7
        if n.contains(number_8(wide, character)):
            num2 = 8
        if n.contains(number_9(wide, character)):
            num2 = 9
            """
      #  print("n = " + n, end=" ")
        #print("num = " + num)
     #   print("num2 = " + num2)

    # print(quiz(wide, character))

   # user_ans = float(input("= "))
"""
    if check_answer(random_number(0, 9, wide, character), check_answer(random_number(0, 9, wide, character)), user_ans, character):
        count += 1
    else:
        print("Sorry, that's not correct.")

print("You got " + str(count) + " out of " + str(max_prob) + " correct!")
"""
# print(random_operator())
