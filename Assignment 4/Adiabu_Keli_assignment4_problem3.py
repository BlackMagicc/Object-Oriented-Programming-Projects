# Arrows

col = int(input("How many columns:"))
while col <= 0:
    print("Invalid entry, try again!")
    col = int(input("How many columns:"))

direction = input("Please enter a direction: (l)eft or (r)ight").lower()  # user types l or r to indicate which
# direction to go
while direction not in "lr":  # force user to enter proper letter
    print("Invalid entry, try again!")
    direction = input("Please enter a direction: (l)eft or (r)ight").lower()

spaces = 0 if direction == "r" else (col - 1)

for i in range(col):
    print(" " * spaces + "*")
    spaces += 1 if direction == "r" else -1

spaces = 1 if direction == "l" else (col - 2)
for i in range(col - 1, 0, -1):
    print(" " * spaces + "*")
    spaces += -1 if direction == "r" else 1
