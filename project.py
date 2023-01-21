from datetime import *

# Enter birth dates and store
# into date class objects
name = input("Name: ")
d1, m1, y1 = [int(x) for x in input("date(DD/MM/YYYY) : ").split('-')]

b1 = date(y1, m1, d1)

# Input for second date
name1 = input("Name: ")
d2, m2, y2 = [int(x) for x in input("date(DD/MM/YYYY) : ").split('-')]

b2 = date(y2, m2, d2)

name2 = input("Name: ")
d3, m3, y3 = [int(x) for x in input("date(DD/MM/YYYY): ").split('-')]

b3 = date(y3, m3, d3)
date = date(2021, 1, 1)
# Check the dates

if b1 == b2 == b3:
    print("All them persons are of equal age")

elif b3 > b1 < b2 and b2 < b3:
    print(f"{name.capitalize()} is {date.year - b1.year - 1} and he/she was born {b1.strftime('%A')}")
    print(f"{name1.capitalize()} is {date.year - b2.year - 1} and he/she was born {b2.strftime('%A')}")
    print(f"{name2.capitalize()} is {date.year - b3.year - 1} and he/she was born {b3.strftime('%A')}")
    print(f"the oldest is {name.capitalize()}")
    print(f"the youngest is {name2.capitalize()}")
    print(" the total: 3")

elif b3 > b1 < b2 and b3 > b2:
    print(f"{name.capitalize()} is {date.year - b1.year - 1} and he/she was born {b1.strftime('%A')}")
    print(f"{name1.capitalize()} is {date.year - b2.year - 1} and he/she was born {b2.strftime('%A')}")
    print(f"{name2.capitalize()} is {date.year - b3.year - 1} and he/she was born {b3.strftime('%A')}")
    print(f"the oldest is {name.capitalize()}")
    print(f"the youngest is {name1.capitalize()}")
    print(" the total: 3")


elif b1 > b2 < b3 and b1 < b3:
    print(f"{name.capitalize()} is {date.year - b1.year - 1} and he/she was born {b1.strftime('%A')}")
    print(f"{name1.capitalize()} is {date.year - b2.year - 1} and he/she was born {b2.strftime('%A')}")
    print(f"{name2.capitalize()} is {date.year - b3.year - 1} and he/she was born {b3.strftime('%A')}")
    print(f"the oldest is {name1.capitalize()}")
    print(f"the youngest is {name2.capitalize()}")
    print(" the total: 3")

elif b1 > b2 < b3 and b3 < b1:
    print(f"{name.capitalize()} is {date.year - b1.year - 1} and he/she was born {b1.strftime('%A')}")
    print(f"{name1.capitalize()} is {date.year - b2.year - 1} and he/she was born {b2.strftime('%A')}")
    print(f"{name2.capitalize()} is {date.year - b3.year - 1} and he/she was born {b3.strftime('%A')}")
    print(f"the oldest is {name1.capitalize()}")
    print(f"the youngest is {name.capitalize()}")
    print(" the total: 3")


elif b2 > b3 < b1 and b1 < b2:
    print(f"{name.capitalize()} is {date.year - b1.year - 1} and he/she was born {b1.strftime('%A')}")
    print(f"{name1.capitalize()} is {date.year - b2.year - 1} and he/she was born {b2.strftime('%A')}")
    print(f"{name2.capitalize()} is {date.year - b3.year - 1} and he/she was born {b3.strftime('%A')}")
    print(f"the oldest is {name2.capitalize()}")
    print(f"the youngest is {name1.capitalize()}")
    print(" the total: 3")

elif b2 > b3 < b1 and b2 < b1:
    print(f"{name.capitalize()} is {date.year - b1.year - 1} and he/she was born {b1.strftime('%A')}")
    print(f"{name1.capitalize()} is {date.year - b2.year - 1} and he/she was born {b2.strftime('%A')}")
    print(f"{name2.capitalize()} is {date.year - b3.year - 1} and he/she was born {b3.strftime('%A')}")
    print(f"the oldest is {name2.capitalize()}")
    print(f"the youngest is {name.capitalize()}")
    print(" the total: 3")


else:
    print("it's invalid date")

# khalid, 1-2-1989
# Nouf, 2-9-2004
# Ali, 9-12-2009
