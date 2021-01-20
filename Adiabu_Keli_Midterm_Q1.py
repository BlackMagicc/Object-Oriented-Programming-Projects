# Factors

while True:
    num = int(input("Please enter an integer (>= 2): "))
    if num < 0:
        print("Finished!")
    break

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1
        print(i, "is a factor of", num)
print("")
if num > 0:
    print(num, "has", count, "factors")
if count == 2:
    print(num, "is a prime number!")