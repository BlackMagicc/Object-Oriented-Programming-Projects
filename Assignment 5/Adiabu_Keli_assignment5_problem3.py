#Prime Numbers

startNum = int(input("Enter start number: "))
endNum = int(input("Enter end number: "))
count = 0

for i in range(startNum, endNum+1):
    if all(i % j for j in range(2, int(i**(1/2))+1)) and i > 0:
        print(i, end=" ")
        count += 1
        if count % 10 == 0:
            print("")
