# Anagram !

def is_anagram(string1, string2):
    if sorted(string1.lower()) == sorted(string2.lower()):
        return True


string = "yes"
while string == "yes":
    string1 = input("Enter the first word: ")
    string2 = input("Enter the second word: ")
    if is_anagram(string1, string2):
        print("The two words ", string1, " and ", string2, " are anagrams")
    else:
        print("The two words ", string1, " and ", string2, " are not anagrams")
    string = input("Do you wish to check for more anagram words? (yes or no): ")
    if string == "no":
        break

