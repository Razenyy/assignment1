''' Write a function named get_daily_temps that prompts the user for the average temperature for each day of the week and returns a dictionary containing the information the user entered.'''
def get_daily_temps():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temps = {}
    for day in days:
        temp = float(input(f"Enter average temperature for {day}: "))
        temps[day] = temp
    return temps

print(get_daily_temps())
