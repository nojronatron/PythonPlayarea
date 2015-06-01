__author__ = 'Blue'
# Three Year-Old Simulator
# Demonstrates the while loop
# Introduces the use of a Sentry Variable

print("\tWelcome to the 'Three-Year-Old Simulator'\n")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")

response = "" # Sentry variable. MUST have a value or program will throw an error.
while response != "Because.":
    response = input("Why?\n")

print("Oh. Okay.")

input("\n\nPress the Enter key to exit.")