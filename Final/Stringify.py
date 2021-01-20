# Stringify

def stringify_digit(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    elif num == 2:
        return "2"
    elif num == 3:
        return "3"
    elif num == 4:
        return "4"
    elif num == 5:
        return "5"
    elif num == 6:
        return "6"
    elif num == 7:
        return "7"
    elif num == 8:
        return "8"
    elif num == 9:
        return "9"


def reverse(strung):
    return strung[::-1]


# print(reverse("Keli"))

def stringify(num):
    pos = False
    if num > 0:
        pos = True
    strang = "\""
    pt = 0
    if num < 0:
        num *= -1
    pt = 1
    while num > 0:
        i = num % 10
        num //= 10
        strang += str(i)
    if pt == 1:
        strang += "-"
        strang += "\""
        strang = reverse(strang)
    if "-" in strang and pos == True:
        return strang.replace('-', '')
    return strang


# num = int(input("Enter number: "))
#print(stringify(576))
