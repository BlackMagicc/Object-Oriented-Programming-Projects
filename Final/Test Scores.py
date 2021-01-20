# Test Scores !

x = list(input("Enter scores: ").split())  # taking multiple inputs from user

temp = []  # empty list
sume = 0
score = 0
ls = []
for i in x:  # loop in entered list
    if i.isnumeric():  # validate data in list
        sume += int(i)  # addup valid score
        score += 1  # count number of scores
        ls.append(int(i))
        temp.append(int(i))  # valid score append to new list
        print("* Adding score: ", i)
    else:
        print("* Invalid score: ", i)

avg = sume / score
avg_count = 0
low_avg_count = 0

# print(ls)

for i in ls:
    if i >= avg:
        avg_count += 1
    if i < avg:
        low_avg_count += 1

print("\n")
print("Total scores: ", score)
print("Highest score: ", max(temp))
print("Lowest score: ", min(temp))
print("Average score: ", sume / score)
print("# of scores >= the average: ", avg_count)
print("# of scores < the average: ", low_avg_count)
