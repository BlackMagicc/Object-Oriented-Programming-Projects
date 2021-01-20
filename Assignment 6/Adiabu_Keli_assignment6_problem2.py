# List Functions

def listlen(listt):
    count = 0
    for i in listt:
        count += 1
    return count


def listmax(listt):
    maxx = listt[0]
    for i in listt:
        if maxx < i:
            maxx = i
    return maxx


def listcopy(listt):
    new_list = []
    for i in listt:
        new_list += [i]
    return new_list


def listappend(new_list, n):
    new_list += [n]
    return new_list


def listinsert(listt, num, digit):
    listt += [0]
    for i in range(listlen(listt)-1, num-1):
        listt[i] = listt[i-1]
        listt[num] = digit
        return listt


def listremove(listt, value):
    if listt:
        result = listremove(listt[1:], value)
        if listt[0] != value:
            result = [listt[0]] + result
        return result
    return []


def listreverse(listt):
    reversed_list = listt[::-1]
    return reversed_list


