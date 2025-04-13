''' Write a function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature for each day of the week, a temperature value, and the day of the week for the recorded temperature. The function should then add the temperature to the dictionary only if it does not already contain a temperature for that day. The function should return the resulting dictionary, whether it is updated or not.'''
def add_daily_temp(temp_dict, day, temp):
    if day not in temp_dict:
        temp_dict[day] = temp
    return temp_dict

# Example usage
temps = {}
add_daily_temp(temps, "Monday", 25)
print(temps)
