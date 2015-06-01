# Tipper app
# Asks user for bill total and supplies suggestions
# for an okay tip (15%) and a good tip (20%)

billtotal = float(input("Enter the total amount of the bill: "))

okaytip = billtotal * 0.15
print("\nAn okay tip would be $", okaytip)

goodtip = billtotal * 0.20
print("\nA good tip would be $", goodtip)


input("\n\nPress the Enter key to exit . . .")
