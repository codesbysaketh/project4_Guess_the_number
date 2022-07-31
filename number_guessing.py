import random

# create a compare function to check the user input with respect to answer
def compare(num, ans):
    """ compares the user input number and gives feedback"""
    if num > ans:
        return "Too High, guess lower"
    elif num < ans:
        return "Too low, guess higher"
    else:
        return f"Correct! the answer is {answer}"


print("Welcome to number guessing game!!!")

# take user input
level = input("Choose a difficulty. Type 'easy' or 'hard' : ")

if level == 'easy':
    attempt = 10
    print("You have 10 attempts to guess the answer")
else:
    attempt = 5
    print("You have 5 attempts to guess the answer")

# generate a random number
answer = random.randint(1, 100)

# game loop
for game in range(attempt):
    user_input = int(input("Guess a number : "))
    print(compare(user_input, answer))
    attempt -= 1
    print(f"You have {attempt} attempts left to guess the number")


