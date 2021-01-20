# print function

name1 = input("Please enter name 1: ")
name2 = input("Please enter name 2: ")
name3 = input("Please enter name 3: ")

# First I store the names that we receive from the user as variables

print(name1 + ", " + name2 + ", " + name3)
print(name1 + ", " + name3 + ", " + name2)
print(name2 + ", " + name1 + ", " + name3)
print(name2 + ", " + name3 + ", " + name1)
print(name3 + ", " + name2 + ", " + name1)
print(name3 + ", " + name1 + ", " + name2)

# Then I just printed every possible combination, not the most efficient way but works
# for only 6 combinations 