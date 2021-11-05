import random
number = random.randint(1, 100)

while True:
    entered_number = int(input("Please enter a number: "))
    
    if entered_number > number:
        print("Please decrease your number.")
    elif entered_number < number:
        print("Please increase your number.")
    else:
        print("Your guess is correct. ")
        break
        