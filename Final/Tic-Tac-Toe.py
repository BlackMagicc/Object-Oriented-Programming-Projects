# Tic Tac Toe


def print_board():
    v = '|    |    |    |'
    h = ' ____ ____ ____ '
    for i in range(0, 10):
        if i % 3 == 0:
            print(h)
        else:
            print(v)

print(print_board())



