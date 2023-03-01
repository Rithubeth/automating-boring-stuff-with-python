from datetime import date
print("Enter the username:")
username = input()
print("Enter the year of birth:")
today = date.today()
year = today.year
age = int(input())
x = year - age
print("Hi", username,", you are", x , "years old.")
