# Part One

word = input("Enter a word to test: ")
open_file = open("/Users/kelia/PycharmProjects/OOP/Assignment 7/movie_reviews.txt", "r")

read_reviews = open_file.read()
read_reviews = read_reviews.lower()

splitreviews = read_reviews.split("\n")

number_of_word = 0
word_score = 0

for eachreview in splitreviews:
    splitline = eachreview.split()
    for i in range(1, len(splitline)):
        if splitline[i] == word:
            number_of_word += 1
            word_score += int(splitline[0])

print("'", word, "' appears ", number_of_word, " times", sep='')

try:
    average = (word_score / number_of_word)

except:
    print("There is no average score for reviews containing the word '", word, "'", sep='')
    print("Cannot determine if this word is positive or negative")

else:
    print("The average score for reviews containing the word '", word, "' is ", average, sep='')
    if average >= 2.0:
        print("This is a positive word")
    else:
        print("This is a negative word")
