# Transpose

def transpose(strlist):
    max_length = 0
    for i in strlist:
        if len(i) > max_length:
            max_length = len(i)
    transposed_list = []
    for i in range(0, max_length):
        x = ""
        for j in strlist:
            if i < len(j):
                x += j[i]
        transposed_list.append(x)
    return transposed_list


print(transpose(['transpose', '', 'list', 'of', 'strings']))
