import random

min_value = 1
max_value = 6
roll_again = "yes"
value1 = random.randint(min_value, max_value)
while roll_again == "yes" or roll_again == "y":
    print("Rolling the die..."),
    print("The value is....")
    if value1 == 1:
        print(encounter1)
    if value1 == 2:
        print(encounter2)
    if value1 == 3:
        print(encounter3)
    if value1 == 4:
        print(encounter4)
    if value1 == 5:
        print(encounter5)
    if value1 == 6:
        print(encounter6)
    print(value1)
    # roll_again = input("Press 'y' or 'yes' to roll the die again.")

encounter1 = "Your best ox has come down bad with tuberculosis. What do you do?"
#2 =
#3 = 
#4 = 
#5 = 
#6 =
