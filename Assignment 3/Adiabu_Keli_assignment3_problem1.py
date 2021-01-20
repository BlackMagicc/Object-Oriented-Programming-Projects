# Valid Triangle Tester

xcord1 = float(input("Enter Point #1 - x position: "))
ycord1 = float(input("Enter Point #1 - y position: "))
xcord2 = float(input("Enter Point #2 - x position: "))
ycord2 = float(input("Enter Point #2 - y position: "))
xcord3 = float(input("Enter Point #3 - x position: "))
ycord3 = float(input("Enter Point #3 - y position: "))

distance1 = round((((xcord1 - xcord2)**2 + (ycord1 - ycord2)**2)**0.5), 2)
distance2 = round((((xcord2 - xcord3)**2 + (ycord2 - ycord3)**2)**0.5), 2)
distance3 = round((((xcord1 - xcord3)**2 + (ycord1 - ycord3)**2)**0.5), 2)

print("The length of each side of your test shape is: ")
print("Side 1: " + str(distance1))
print("Side 2: " + str(distance3))
print("Side 3: " + str(distance2))

x = False

if (distance1 + distance2) > distance3:
    if (distance2 + distance3) > distance1:
        if (distance3 + distance1) > distance2:
            x = True
            print("This is a valid triangle!")

if x:
    if (distance1 == distance2) and (distance1 == distance3):
        print("This is an equilateral triangle")
    elif (distance1 == distance2) or (distance1 == distance3):  # condition for isosceles
        if distance2 != distance3:
            print("This is an isosceless triangle")
    elif (distance2 == distance3) and (distance1 != distance2):
        print("This is an iscosceles triangle")
    elif (distance1 != distance2) and (distance1 != distance3) and (distance2 != distance3):
        print("This is a scalene triangle")
else:
    print("This is not a valid triangle")


