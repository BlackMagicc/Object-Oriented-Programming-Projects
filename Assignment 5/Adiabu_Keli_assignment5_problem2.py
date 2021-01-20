# Dynamic Gradebook

numStudents = int(input("How many students are in your class? "))

while numStudents <= 0:
    print("Invalid # of students, try again.")
    numStudents = int(input("How many students are in your class? "))

numTests = int(input("How many tests in this class? "))

while numTests < 0:
    print("Invalid # of tests, try again.")
    numTests = int(input("How many tests in this class? "))

print("Here we go!")

totalAvg = 0
totalTotal = 0
x = 0
y = 0

for i in range(numStudents):
    total = 0
    for j in range(numTests):
        total += float(input("Enter student {:d}\'s test {:d} score: ".format(i+1, j+1)))
        totalTotal += total
    avg = total / numTests
    print("Average score for student #{:d} is {:.2f}".format(i+1, avg))
    totalAvg += avg

classAvg = totalAvg / numStudents
print("Average score for all students is: {:.2f}".format(classAvg))
"""
        total = float(input("Enter student {:d}\'s test {:d} score:".format(x+1, y+1)))
        while total < 0:
            print("Invalid score, try again")
            total += float(input("Enter student {:d}\'s test {:d} score:".format(i+1, j+1)))
        totalTotal += total
"""

"""
x = 1
y = 1
for numStudents in range(1, numStudents + 1):
    print("**** Student {} ****".format(numStudents))
    totalScore = 0
    for i in range(1, numTests + 1):
        while True:
            count = int(input("Enter score for test #" + str(x) + ": "))  # our test score
            if count < 0:
                print("Invalid score. Try again.")
            if x == numTests:
                break
            x += 1
        testScore = int(input("Enter score for test #" + str(x) + ": "))
        totalScore += testScore
        y += 1
    print("")
    print("Average score for student #{} is {:.2f}".format(numStudents, totalScore / numTests))
    print("")
"""