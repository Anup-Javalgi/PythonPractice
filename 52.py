# Match-case statement(switch) : An alternative to using many elif statements
#                                executer some code if a value matches a 'case'
#                                Benefits : cleaner and syntax is more readable



######Using if-esle######
def day_of_week(day):
    if day == 1:
        return 'Sunday'
    elif day == 2:
        return 'Monday'
    elif day == 3:
        return 'Tuesday'
    elif day == 4:
        return 'Wednesday'
    elif day == 5:
        return 'Thursday'
    elif day == 6:
        return 'Friday'
    elif day == 7:
        return 'Saturday'
    else:
        return 'Not Valid!'
    
print(day_of_week(2))


######Using match-case######

def days_of_week(day):
    match day:
        case 1:
            return 'Sunday'
        case 2:
            return 'Monday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thursday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'
        case _:
            return 'Not Valid!'
        
print(days_of_week(10))



#######################

def days_of_weeks(day):
    match day:
        case 'saturday' | 'sunday':
            return True
        case 'monday'|'tuesday'|'wednesday'|'thursday'|'friday':
            return False
        case _:
            return 'Not Valid!'
        
print(days_of_weeks('saturday'))