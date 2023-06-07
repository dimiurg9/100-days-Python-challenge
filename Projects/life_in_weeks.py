"""
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
https://waitbutwhy.com/2014/05/life-weeks.html
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live
 until 90 years old.
It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.
"""
DAYS_UN_YEAR = 365
WEEKS_IN_YEAR = 52
MONTH_IN_YEAR = 12
MAX_YEARS_CALCULATION = 90
WEEKS_IN_90_YEARS = 52 * MAX_YEARS_CALCULATION
MONTH_IN_90_YEARS = 12 * MAX_YEARS_CALCULATION
DAYS_IN_90_YEARS = 365 * MAX_YEARS_CALCULATION
current_age = int(input("What is your age? "))
days_left = DAYS_IN_90_YEARS - current_age * DAYS_UN_YEAR
weeks_left = WEEKS_IN_90_YEARS - current_age * WEEKS_IN_YEAR
month_left = MONTH_IN_90_YEARS - current_age * MONTH_IN_YEAR
print(f"you have {days_left} days, {weeks_left} weeks, and {month_left} month left.")






