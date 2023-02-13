import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please type a number larger then 0 next time.")
else: 
    print("please type a number next time")
    quit()


random_number = random.randint(0, top_of_range)
print("random number", random_number)