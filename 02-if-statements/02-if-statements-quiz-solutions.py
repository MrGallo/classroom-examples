
# 1.
# ask for day of the week
# output weekend or weekday
day = input("Enter a day: ")

if day == "sunday" or day == "saturday":
    print("Weekend")
else:
    print("Weekday")


# 2. 
# ask user for password
# Access granted, if correct
# ACCESS DENIED, if incorrect
# if 12345 "12345? That's not very secure. Access VERY denied."
# correct password: 123456

password = input("Please enter your password: ")

if password == "123456":
    print("Access granted.")
elif password == "12345":
    print("12345? That's not very secure. Access VERY denied.")
else:
    print("ACCESS DENIED")
