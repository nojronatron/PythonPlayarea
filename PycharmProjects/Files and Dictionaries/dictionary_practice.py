# -------------------
# Author: Jonathan Rumsey
# Title: Dictionary Practice #1
# Description: Fiddling with Dictionaries
# Original: 1-Dec-2015
# Updated: <date>, <updater>
# -------------------

# Create a dictionary by populating with many key:value pairs
my_dictionary = {
    "A":"Alpha",
    "B":"Bravo",
    "C":"Charlie",
    "D":"Delta",
    "E":"Echo",
    "F":"Foxtrot",
    "G":"Golf"
}

print("Printing the dictionary directly results in a literal, unorganized list of K:V pairs:")
print(my_dictionary)

print("\nCycling through each entry merely returns the keys.")
print("Use 'slicing' brackets to extract each key:")
print("Key A has a value of:", my_dictionary["A"])

print("\nExtracting all pairs by calling each item in the KV pair dictionary:")
for item in my_dictionary:
    print("Item is:", item)

print("\nExtracting all pairs by ID'ing each key:")
for item in my_dictionary:
    print("KV pair:", my_dictionary[item])

print("\nExtract each pair but prefix with each Key:")
print("Key\tValue")
print("===\t=====")
for item in my_dictionary:
    print(item, "\t", my_dictionary[item], sep="")

print("\nNow try to find a Value based on an \"in\" term:")
my_term = "A"
if my_term in my_dictionary:
    print("Found \"", my_term, "\"in the dictionary! The value is: ", my_dictionary[my_term], ".", sep="")
else:
    print("Did NOT find it.")

print("\nAdding values to the dictionary is done with \"dictionary[key]=value\".")
print("The new KV pair is H:Hotel:")
another_key = "H"
another_value = "Hotel"
if another_key not in my_dictionary:
    my_dictionary[another_key] = another_value
else:
    print(another_key, "already exists in the dictionary.")

print("\nSelect a Value based on a Key using the get() method.")
print("Searching for", another_key, "in this example:")
print(my_dictionary.get(another_key, "Could not find the value."))

# End
input("\n\nPress the Enter key to exit.")