__author__ = 'Blue'
# Hero's Inventory
# Demonstrates tuple creation

# Create an empty Tuple
inventory = ()

# Treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print the tuple
print("\nYou have:", (len(inventory)), "items in your inventory.")

# print each element in the tuple
print("\nYour items:")
for item in inventory:
    print(item)

# Test for membership with 'in'
if "healing potion" in inventory:
    print("\nYou will live to fight another day.")

# Display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
if index < 1:
    index = 1
    print("\nThat number is too low, so I'll assume you meant the first item in inventory.")
if index > len(inventory):
    index = len(inventory)
    print("\nThat number is too high, so I'll assume you meant the last item in inventory.")

print("At index", index, "is", inventory[index - 1])

# Concatenate two tuples (since they are immutable)
chest = ("gold", "gems")
print("\nYou find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the Enter key to exit.")
