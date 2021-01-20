# Numbers


# Part A
def horizontal_line(width, pattern):
    x = ""
    for i in range(width):
        x += pattern
    return x


def vertical_line(shift, height, pattern):
    space = ""
    ans = ""
    for i in range(shift):
        space += " "
    for i in range(height):
        ans += space + pattern + "\n"
    return ans


def two_vertical_lines(width, height, pattern):
    space = ""
    ans = ""
    for i in range(width):
        space += " "
    for i in range(height):
        ans += pattern + space + pattern + "\n"
    return ans


# Part B

def number_0(width, pattern):
    return " " + horizontal_line(width, pattern) + "\n" + two_vertical_lines(width, 3, pattern) + " " + horizontal_line(
        width, pattern) + "\n"


def number_1(width, pattern):
    return vertical_line(width, 5, pattern)


def number_2(width, pattern):
    return horizontal_line(width, pattern) + "\n" + vertical_line(width - 1, 1, pattern) + horizontal_line(width,
                                                                                                           pattern) + "\n" + vertical_line(
        0, 1, pattern) + horizontal_line(width, pattern)


def number_3(width, pattern):
    return horizontal_line(width, pattern) + "\n" + vertical_line(width - 1, 1, pattern) + horizontal_line(width,
                                                                                                           pattern) + "\n" + vertical_line(
        width - 1, 1, pattern) + horizontal_line(width, pattern)


def number_4(width, pattern):
    return two_vertical_lines(width, 2, pattern) + " " + horizontal_line(width, pattern) + "\n" + vertical_line(
        width + 1, 2, pattern)


def number_5(width, pattern):
    return horizontal_line(width, pattern) + "\n" + vertical_line(0, 1, pattern) + horizontal_line(width,
                                                                                                   pattern) + "\n" + vertical_line(
        width - 1, 1, pattern) + horizontal_line(width, pattern)


def number_6(width, pattern):
    return horizontal_line(width, pattern) + "\n" + vertical_line(0, 1, pattern) + horizontal_line(width,
                                                                                                   pattern) + "\n" + two_vertical_lines(
        width - 2, 1, pattern) + horizontal_line(width, pattern)


def number_7(width, pattern):
    return horizontal_line(width, pattern) + "\n" + vertical_line(width - 1, 4, pattern)


def number_8(width, pattern):
    return horizontal_line(width, pattern) + "\n" + two_vertical_lines(width - 2, 1, pattern) + horizontal_line(width,
                                                                                                                pattern) + "\n" + two_vertical_lines(
        width - 2, 1, pattern) + horizontal_line(width, pattern)


def number_9(width, pattern):
    return horizontal_line(width, pattern) + "\n" + two_vertical_lines(width - 2, 1, pattern) + horizontal_line(width,
                                                                                                                pattern) + "\n" + vertical_line(
        width - 1, 2, pattern)


# Part C

def print_number(num, width, pattern):
    ans = ""
    if num == 0:
        ans = number_0(width, pattern)
    elif num == 1:
        ans = number_1(width, pattern)
    elif num == 2:
        ans = number_2(width, pattern)
    elif num == 3:
        ans = number_3(width, pattern)
    elif num == 4:
        ans = number_4(width, pattern)
    elif num == 5:
        ans = number_5(width, pattern)
    elif num == 6:
        ans = number_6(width, pattern)
    elif num == 7:
        ans = number_7(width, pattern)
    elif num == 8:
        ans = number_8(width, pattern)
    elif num == 9:
        ans = number_9(width, pattern)
    return print(ans)


# Part D

def plus(width, pattern):
    add = ""
    space = width // 2
    for i in range(5):
        if i == 2:
            add = add + width * pattern + "\n"
        elif width % 2 == 0:
            add = add + ((space - 1) * " " + pattern + pattern + (space - 1) * " ") + "\n"
        else:
            add = add + (space * " " + pattern + space * " ") + "\n"
    return add


"""
    if width % 2 != 0:
        ans = vertical_line(width, 2, pattern) + "   " + horizontal_line(width, pattern) + "\n" + vertical_line(width, 2, pattern)
    else:
        ans = vertical_line(width-4, 2, pattern) + vertical_line(width-3, 2, pattern) + horizontal_line(width, pattern)
    return ans
"""


def minus(width, pattern):
    return horizontal_line(width, pattern)


# Part E

def check_answer(num, num2, ans, op):
    if op == '+':
        correct = num + num2
        if correct == ans:
            return True
        elif correct != ans:
            return False
    elif op == '-':
        correct = num - num2
        if correct == ans:
            return True
        elif correct != ans:
            return False
    elif op != '+' and op != '+':
        correct = num + num2
        if correct == ans:
            return True
        elif correct != ans:
            return False


# Part F


# print(check_answer(6, 12, 18, '-'))
