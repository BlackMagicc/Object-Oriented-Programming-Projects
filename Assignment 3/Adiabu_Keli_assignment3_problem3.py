#Birthday Analyzer

startDate = input("Enter start date MMDDYYYY: ")
birthDate = input("Enter birth date MMDDYYYY: ")

months=["January", "February", "March", "April", "May", "June", "July", "Septber", "October", "November", "December"]

month1 = int(birthDate[0:2])
month2 = int(startDate[0:2])

day1 = int(birthDate[2:4])
day2 = int(startDate[2:4])

year1 = int(birthDate[-4:])
year2 = int(startDate[-4:])

a = ["st", "nd", "rd", "th"]
st = day1%10

if st == 0 or st > 4:
    st = 4

print("The contestant was born on %s %d%s, %d"%(months[month1-1], day1, a[st-1], year1))
if (year2 - year1 > 21) or ((year2 - year1) == 21 and month2>month1) or (year2-year1 == 21 and month1 == month2 and day2 >= day1):
    print("ELIGIBLE: The contestant will be 21 by the time the taping begins")
else:
    print("ELIGIBLE: The contestant won't be 21 by the time the taping begins")


