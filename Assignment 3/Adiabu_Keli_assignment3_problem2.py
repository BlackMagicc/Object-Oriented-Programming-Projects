#Alphabetical Order
import string

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string3 = input("Enter the third string: ")

print("Here are the strings in ascending alphabetical order: ")

"""
a = 'Banana'   lowercase has higher value
b = 'banana'

if a < b:
    print("yes")
"""
a = [string1, string2, string3]

a.sort(key=lambda word: word.upper())

for x in range(len(a)):
    print(a[x])






