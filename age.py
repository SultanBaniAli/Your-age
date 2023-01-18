import datetime
year = int(input(" type the Year: "))
month = int(input(" type the Month: "))
day = int(input(" type the Day: "))
birthdate = datetime.date(year,month,day)
date = datetime.datetime
present = date.now()

if(birthdate.month >= present.month):
    print(f"You are {present.year - birthdate.year -1} years old , {abs((12 - birthdate.month) + present.month)} month and {abs(birthdate.day - present.day )} day")
else:
    print(
        f"You are {present.year - birthdate.year} years old , {abs((12 - birthdate.month) + present.month)} month and {abs(birthdate.day - present.day)} day")

