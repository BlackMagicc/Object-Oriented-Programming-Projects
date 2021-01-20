#Weight Loss Log with Sentinels

Weight = []
i = 1

while True:
    print("Enter your weight on day ", i, ":", end=" ")
    userWeights = float(input())
    if userWeights > 0:
        Weight.append(userWeights)
        i = i + 1
    if userWeights == -1:
        break

i = i - 1
summ = 0

for x in Weight:
    summ += x

print("Average Weight Over", i, "Days:", round(summ/i, 2))
print("Total Weight Loss Over", i, "Days:", round(Weight[0]-Weight[-1], 2))
