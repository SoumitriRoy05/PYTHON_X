import calendar

def print_month_calendar():

    year = int(input("Enter the year: "))
    month = int(input("Enter the required 2024month: "))
    
    print(calendar.month(year, month))

print_month_calendar()