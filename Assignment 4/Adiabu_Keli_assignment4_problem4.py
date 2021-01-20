# How much time has elapsed ?

while True:
    userData = int(input("Please enter the number of seconds elapsed: "))
    if userData < 0:  # SENTINEL
        print("Exiting program...")
        break
    userData = userData % (24 * 3600)
    hours = userData // 3600
    userData %= 3600
    minutes = userData // 60
    userData %= 60
    seconds = userData

    pHour = "hours"
    pSecond = "seconds"
    pMinute = "minutes"

    if hours == 1:
        pHour = "hour"
    if seconds == 1:
        pSecond = "second"
    if minutes == 1:
        pMinute = "minute"

    print(str(hours) + " " + pHour + ", " + str(minutes) + " " + pMinute + ", " + str(seconds) + " " + pSecond)

