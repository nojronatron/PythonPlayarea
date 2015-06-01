__author__ = 'Blue'

# Hero's Inventory 3.0 - use Lists instead of Tuples

# Create a list with some items and display with a for loop
inventory = ["sword", "armor", "shield", "healing potion"]
print("Your items:")
for item in inventory:
    print(item)

input("\nPress the Enter key to continue.")

# Get the length of the list
print("You have", len(inventory), "items in your possession.")

input("\nPress the Enter key to continue.")

# Test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# Display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# Display a Slice of the List
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("\nEnter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the Enter key to continue.")

# Concatenation is similar to Tuples but remember concatenation requires the same TYPEs.
# Concatenate two lists
chest = ["gold", "gems"]
print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the Enter key to continue.")

# Assignment by index
print("You trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now:")
print(inventory)

input("\nPress the Enter key to continue.")

# Assign by slice
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now:")
print(inventory)

input("\nPress the Enter key to continue.")

# Delete a List element
print("In a great battle, your shield is destroyed.")
del inventory[2]
print("Your inventory is now:")
print(inventory)

input("\nPress the Enter key to continue")
