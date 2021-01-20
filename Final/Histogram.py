# Histogram !

numbers = input("Enter a series of numbers seperated by spaces:\t").split()
ls = []
for i in numbers:
    try:
        num = int(i)
        if num < 0 or num > 10:
            print("* {} is out of bounds - rejecting".format(i))
        else:
            ls.append(num)
            print("* {} is valid - accepting".format(i))
    except:
        print("* {} is not a number".format(i))

largest = max(ls)
smallest = min(ls)
ranges = largest - smallest
freq = {}

for i in ls:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
mode = 0
m = 0

for i in freq:
    if freq[i] > mode:
        mode = freq[i]
        m = i

print("Largest number:\t{}".format(largest))
print("Smallest number:\t{}".format(smallest))
print("Range of values:\t{}".format(ranges))
print("Mode:\t{}".format(m))
print("Frequecy Histogram:")
for i in freq:
    print("{} {}".format(i, "#" * freq[i]))
