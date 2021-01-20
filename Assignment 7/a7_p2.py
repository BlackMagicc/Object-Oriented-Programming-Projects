# Part Two

import time

open_file = open("/Users/kelia/PycharmProjects/OOP/Assignment 7/movie_reviews.txt", "r")
read_reviews = open_file.read()
read_reviews = read_reviews.lower()

split_reviews = read_reviews.split("\n")
words = {}
timebefore = time.time()

for eachreview in split_reviews:
    splitline = eachreview.split()
    for i in range(1, len(splitline)):
        if splitline[i] not in words:
            words[splitline[i]] = [int(splitline[0]), 1]
        else:
            words[splitline[i]][0] += int(splitline[0])
            words[splitline[i]][1] += 1

timeafter = time.time()
time = format(timeafter - timebefore, '.2f')

print("Initializing sentiment database")
print("Sentiment database initialization complete")
print("Total unique words analyzed:", len(words))
print("Analysis took", time, "seconds to complete")
print()

test = input("Please enter a phrase to test for sentiment analysis: ")

splittest = test.split(" ")

words_in_phrase = 0
total_average = 0
for item in splittest:
    if item not in words:
        print("* '", item, "' does not appear in any moview reviews", sep='')
    else:
        count = words[item][1]
        average = words[item][0] / count
        print("* '", item, "' appears ", count, " times with an average score of ", average, sep='')
        words_in_phrase += 1
        total_average += average

if words_in_phrase > 0:
    print("Average score for this phrase is:", total_average / words_in_phrase)
    if total_average / words_in_phrase >= 2.00:
        print("This is a POSITIVE phrase")
    else:
        print("This is a NEGATIVE phrase")

else:
    print("Not enough words to determine the sentiment.")
