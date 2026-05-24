from datetime import datetime

# This function gets the current live date (day, month, year) from the system.
def get_current_date():
    today = datetime.now()
    d1 = today.day
    m1 = today.month
    y1 = today.year
    return d1, m1, y1

# This function asks the user to input their birth date details.
def take_user_input():
    d2 = int(input("Please enter day: "))
    m2 = int(input("Please enter month: "))
    y2 = int(input("Please enter year: "))
    return d2, m2, y2

# This function calculates the difference between today's date and birth date, then prints the age.
def calculate_age(d1, m1, y1, d2, m2, y2):
    today = datetime(y1, m1, d1)
    birth = datetime(y2, m2, d2)
    
    # Subtracting dates to get the difference in days
    age_difference = today - birth
    years = age_difference.days // 365
    
    print(f"🎉 Your age is: {years} years")

# --- Main Program Execution ---
current_day, current_month, current_year = get_current_date()
birth_day, birth_month, birth_year = take_user_input()

# Calling the function to calculate and print the result
calculate_age(current_day, current_month, current_year, birth_day, birth_month, birth_year)
