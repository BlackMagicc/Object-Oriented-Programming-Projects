# Pizza Party

budget = float(input("Enter budget for your party: "))
sliceCost = float(input("Cost per slice of pizza: "))
pieCost = float(input("Cost per whole pizza pie (8 slices): "))
partyLimit = float(input("How many people will be attending your party? "))

x = 1
personNum = 1
totalNumSlices = 0
numSlices = 0

while (x < partyLimit) or (x == partyLimit):
    numSlices = float(input("Enter number of slices for person #" + str(personNum) + ": "))
    if (numSlices < 1) or (numSlices > 7):
        print("Not a valid entry, try again!")
    else:
        personNum += 1
        x += 1
        totalNumSlices += numSlices


#print(totalNumSlices)
numPies = totalNumSlices // 8
leftover = totalNumSlices % 8
totalCost = (numPies * pieCost) + (leftover * sliceCost)

moneyLeft = budget - totalCost

if moneyLeft < 0:
    moneyLeft = abs(moneyLeft)
    print("Your order cannot be completed")
  #  print("You would need to purchase ")
    print("This would put you over budget by " + str(moneyLeft))
elif moneyLeft > 0:
    print("You should purchase " + str(int(numPies)) + " pies and " + str(int(leftover)) + " slices")
    print("Your total cost will be: " + str(totalCost))
    print("You will still have " + str(moneyLeft) + " left after your order")
elif moneyLeft == 0:
    print("You should purchase " + str(int(numPies)) + " pies and " + str(int(leftover)) + " slices")
    print("Your total cost will be: " + str(totalCost))
    print("You will have no money left after your order.")