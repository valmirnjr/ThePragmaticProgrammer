# Exercise 5
# <time> ::= <hour><complement> 
# <hour> ::= <number>[<number>]
# <complement> ::= [<separator><minutes>] <shift> | <separator><minutes> [<shift>]
# <shift> ::= <am><pm>

def getHour(time: str):
    firstDigit = time[0]
    secondDigit = time[1] if time[1].isdigit() else ""
    return firstDigit + secondDigit

def getMinutes(time):
    sepIndex = time.find(':')
    if sepIndex < 0:
        return "00"
        
    # Assuming there are always two digits representing minutes here
    return time[sepIndex+1:sepIndex+3]

def getShift(time):
    if time.find('am') >= 0:
        return 0
    if time.find('pm') >= 0:
        return 1
    return -1

def formatTime(time):
    """ Format a given time to the 24h format. """
    hour = getHour(time)
    minutes = getMinutes(time)
    shift = getShift(time)

    if shift == 1:
        hour = int(hour) + 12

    return f"{hour}:{minutes}h"

def main():
    formattedTime = formatTime("11:59pm")
    print(formattedTime)

if __name__ == "__main__":
    main()
