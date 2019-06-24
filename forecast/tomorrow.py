def tommorow(day):
    if day == 'Monday':
        return 'Tuesday'
    elif day == 'Tuesday':
        return "Wednesday"
    elif day == "Wednesday":
        return 'Thursday'
    elif day == 'Thursday':
        return 'Friday'
    elif  day == 'Friday':
        return 'Saturday'
    elif day == 'Saturday':
        return 'Sunday'
    else:
        return 'Monday'


if __name__ == '__main__':
    day = input()
    print(tommorow(day))