import random

'''
1 for snake
-1 for water
0 for gun
'''

# Computer randomly chooses Snake, Water, or Gun
computer = random.choice([-1, 0, 1])

# Take user's choice
youstr = input("Enter your choice (s/w/g): ")

# Convert user's choice into numbers
youDict = {"s": 1, "w": -1, "g": 0}

# Convert numbers back into words
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Get user's numeric choice
you = youDict[youstr]

# Display choices
print(f"You chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

# Check the result
if computer == you:
    print("It's a draw!")

elif computer == -1 and you == 1:
    print("You win!")

elif computer == -1 and you == 0:
    print("You lose!")

elif computer == 1 and you == -1:
    print("You lose!")

elif computer == 1 and you == 0:
    print("You win!")

elif computer == 0 and you == -1:
    print("You win!")

elif computer == 0 and you == 1:
    print("You lose!")

else:
    print("Something went wrong")