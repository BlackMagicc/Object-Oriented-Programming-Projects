# Numbers

def is_even(num):
    if num == 0:
        return False
    else:
        if num % 2 == 0:
            return True
    return False


def is_prime(num):
    ls = []
    for i in range(2, num):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            ls.append(i)
    return ls

print(is_prime(100))


def perfect_number(start, end):
    ls = []
    for i in range(start, end + 1):
        sum1 = 0
        for x in range(1, i):
            if i % x == 0:
                sum1 += x
                if sum1 == i:
                    # print(i)
                    ls.append(i)
    if 24 in ls: ls.remove(24)
    return ls


def abundantUtil(num):
    divisor = int(num / 2) + 1
    val = 0
    for x in range(1, divisor):
        if num % x == 0:
            val += x
    return val > num

def abundant(n):
    arr = []
    x = 1
    while True:
        if abundantUtil(x):
           n = n - 1
           arr.append(x)
           if n==0:
               break
        x = x + 1
    return arr

"""
def is_abundant(start, end):
    ls = []
    factor_sum = 0
    for i in range(1, end):
        for x in range(1, int(i)):
            if i % x == 0:
                factor_sum += x
        if i < factor_sum:  # num is abundant
            ls.append(i)
            factor_sum = 0
    return ls
"""


print("Main Menu"
      "\n"
      "\n"
      "1 - Find all prime numbers within a given range \n"
      "2 - Find all perfect numbers within a given range \n"
      "3 - Find all abundant numbers within a given range \n"
      "4 - Chart all even, odd, prime, perfect and abundant numbers within a given range \n"
      "5 - Quit"
      "\n"
      "\n")


i = 0
# print("Choice is: " + str(choice))
while True:
    choice = int(input("Your choice: "))
    while True:
        if choice not in range(1, 5):
            print("I don't understand that ...")
        else:
            break

    while True:
        start_num = int(input("Enter starting number (positive only): "))
        if start_num < 0:
            print("Invalid, try again")
        else:
            break

    while True:
        end_num = int(input("Enter ending number: "))
        if end_num <= start_num:
            print("Invalid, try again")
        else:
            break

    #  print("Choice is: " + str(choice))
  #  print(type(choice))
    if choice == 1:
        primes = is_prime(end_num)
        x = primes.index(start_num)
        y = primes.index(end_num)
     #   print(type(primes)1)
      #  x, y = primes[primes[start_num], primes[end_num]]
        print("All prime numbers between " + str(start_num) + " and " + str(end_num) +
              "\n"
              "##############"
              "\n"
              "" + str(primes[x, y]) +
              "\n"
              "##############")
    elif choice == 2:
        print("All perfect numbers between " + str(start_num) + " and " + str(end_num) +
              "\n"
              "##############"
              "\n"
              "" + str(perfect_number(start_num, end_num)) +
              "\n"
              "##############")
    elif choice == 3:
        print("All abundant numbers between " + str(start_num) + " and " + str(end_num) +
              "\n"
              "##############"
              "\n"
              "" + str(abundant(end_num - start_num)) +
              "\n"
              "##############")
    else:
        break
