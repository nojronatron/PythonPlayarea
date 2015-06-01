__author__ = 'Blue'
# THis is a pseudo-code experiment
# but could turn into actual running code (we'll soon find out)

import random

# add-in some debug logging
enable_debug = 0

# Introduce the game to the user
print("\tWelcome to the reverse number guess game!")
print("\n\nIn this game, the computer will try to guess YOUR number.")
print("\nLet's get started...")

# Gather input from the user -- the number between 1 and 100 that the computer needs to guess
good_number_selected = 0
while not good_number_selected:
    users_number = int(input("\nEnter your number (between 1 and 100, inclusive) and I'll keep it secret while we play: "))
    if users_number < 1 or users_number > 100:
        good_number_selected = 0
        print("Please enter a number between 1 and 100 (inclusive).")
        continue
    else:
        good_number_selected = 1
        break

print("\n\nGreat! I'll not cheat, I promise.")

# Have the computer make a random guess of the user's number
cpu_guess = 0
new_guess = 0
upper_bound = 100
lower_bound = 1
cpu_guessed = 0
num_tries = 0

while num_tries < 10:
    cpu_guess = random.randint(lower_bound, upper_bound)
    num_tries += 1
    if enable_debug:
        print("\tDEBUG: CPU Guess:", cpu_guess, " and num_tries is now", num_tries)

    # If guess is right, confirm with the user
    if cpu_guess == users_number:
        if enable_debug:
            print("\tDEBUG: Entered GuessIsRight logic.")
        print("Your number is", cpu_guess)
        response = input("Right? (Y/N)")
        if response == "Y":
            print("Yes! Got it in only", num_tries, "attempts!")
            cpu_guessed = 1
            if enable_debug:
                print("\tDEBUG: Executing BREAK statement.")
            break

    # Ask the user if too high or too low
    print("\nTell me, is", cpu_guess, "your number,")
    response = input("or did I guess high or low? (high/low):")

    # If too high then have random generate a number between 0 and the last guess
    if response == "high":
        upper_bound = cpu_guess - 1
        if enable_debug:
            print("\tDEBUG: User entered high. cpu_guess is", cpu_guess, "users_number is", users_number)
            print("\tDEBUG: lower_bound remains:", lower_bound, "upper_bound NOW:", upper_bound)

    # If too low then have random generate a number between the last guess and 100
    elif response == "low":
        lower_bound = cpu_guess + 1
        if enable_debug:
            print("\tDEBUG: User entered low. cpu_guess is", cpu_guess, "users_number is", users_number)
            print("\tDEBUG: lower_bound NOW:", lower_bound, "upper_bound remains:", upper_bound)

# Go back and ask the user if too high or too low

# After 10 guesses, insist the user give-up the number
if not cpu_guessed:
    print("\n\nOkay, I've tried 10 times and I cannot guess your number.")
    input("Please, tell me what it is?")

input("\nThanks that was fun. Press the Enter key to exit.")