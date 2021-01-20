# Median

# this function takes in a value and a list, find first occurence of value in list and return that index
def my_index(l, value):
    for numbers in range(0, len(l)):
        if value == numbers:
            return i


# this function takes two list as input: first is list of all element, second is the list of indexes visited
def find_index_of_min(l, used_indices):
    # if all the indexes already visited or there are no element in the list then returns -1
    if len(l) == 0 or len(l) == len(used_indices):
        return -1
    # defining a variable that stores the index that has not been visited yet.
    min_index = -1
    # a minimum index is found or not is defined by this variable
    found = 0
    # this loop runs till it finds an index that is not in used_indices
    while found == 0:
        min_index += 1
        if min_index not in used_indices:
            found = 1
    # this loop finds minimum value index that has not been visited yet,i.e, not in used_indices
    for it in range(0, len(l)):
        if it not in used_indices:
            if l[min_index] > l[it]:
                min_index = it
    # we return the value of min_index
    return min_index


# this function is used to build a tuple of list of unique numbers and indexes which are sorted by thier values
def build_seen_and_unique(l):
    # defining two list one for unique, another for storing visited index
    unique = []
    seen = []
    # this loop runs for indexes between 0 to size of the list
    for i in range(0, len(l)):
        # we find the minimum index and append it to "seen" list
        minIndex = find_index_of_min(l, seen)
        seen.append(minIndex)
        # if value of that index is not present in unique list, then we add it to te list
        if l[minIndex] not in unique:
            unique.append(l[minIndex])
    # we return a tuple of unique and seen list
    return unique, seen


# this function takes in a list and returns its median
def find_median(l):
    # we call build_seen_and_unique passing the list to it
    # tup[0] contains a list all the unique element
    # tup[1] contains a list of index sorted by their values in list "l"
    tup = build_seen_and_unique(l)
    # if number of element is even then we return average of middle two element as median
    if len(l) % 2 == 0:
        return int((l[tup[1][int(len(l) / 2) - 1]] + l[tup[1][int(len(l) / 2)]]) / 2)
    # else if number of element is odd then we return the middle element as median
    else:
        return int(l[tup[1][int((len(l) + 1) / 2) - 1]])


# running two test cases given in the question
l = [100, 67, 68, 69, 72, 73, 73, 73, 73, 75, 76, 76, 77, 77, 82, 86, 87, 87, 90, 91, 66]
print(f"{l} : {find_median(l)}")
l = [91, 66, 66, 67, 68, 70, 72, 73, 73, 73, 73, 78, 78, 78, 83, 84, 86, 86, 88, 59]
print(f"{l} : {find_median(l)}")
