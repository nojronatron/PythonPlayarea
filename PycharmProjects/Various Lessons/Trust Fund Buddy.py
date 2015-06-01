print("""

          Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs. since you're rich, ignore
pennies and use only dollar amounts.

""")

car = input("Lamborghini Tune-ups: ")
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Gifts: ")
food = input("Dining Out: ")
staff = input("Staff butlers, chef, driver, assistants...: ")
guru = input("Personal coach: ")
games = input("Computer games: ")

total = int(car) + int(rent) + int(jet) + int(gifts) + int(food) + int(staff) + int(guru) + int(games)

print("\nGrand Total:", total)

input("\n\nPress the Enter key to exit.")
