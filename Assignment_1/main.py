def convertToMinutes(time):
    splitted_time = time.split(":")
    hour = int(splitted_time[0])
    if hour == 00:
        hour = 24
    minute = int(splitted_time[1])
    return hour, minute


def prepareMinuteArray(timeArray):
    minuteArray = []
    for time in timeArray:
        hour, minute = convertToMinutes(time)
        timeInMinutes = (hour * 60) + minute
        minuteArray += [timeInMinutes]
    return minuteArray


def findMinimumMinuteDifference(timePoints):
    minutesArray = sorted(prepareMinuteArray(timePoints))
    minimumTimeDifference = 1440
    for time in range(0, len(minutesArray)-1):
        diff = minutesArray[time+1]-minutesArray[time]
        if(diff < minimumTimeDifference):
            minimumTimeDifference = diff
    return minimumTimeDifference


findMinimumMinuteDifference(["00:00", "23:59", "00:00"])
