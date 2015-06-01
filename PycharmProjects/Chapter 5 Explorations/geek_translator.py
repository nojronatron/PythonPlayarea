# -------------------
# Author: Jon Rumsey
# Title: Geek Translator
# Description: Demonstrates using Dictionaries (Name:Value pairs)
# Original: 8-May-2015
# Updated: (initial)
# -------------------

geek = {"404": "Clueless. From the web error message 404, meaning page not found.",
        "Googleing": "Searching the internet for background information on a noun.",
        "Keyboard Plaque": "The collection of debris found in computer keyboards.",
        "Link Rot": "The process by which web page links become obsolete.",
        "Percussive Maintenance": "The act of striking an electronic device to make it work",
        "Uninstalled": "Being fired. Especially popular during the dot-bomb era."}

print("\tGeek Translator")
print("Demonstrates using Dictionaries (Name:Value pairs)\n")
choice = None
while choice !="0":
    print(
        """
        Pick An Option:

        0 - Quit
        1 - Look UP a Geek Term
        2 - Add a Geek Term
        3 - Redefine a Geek Term
        4 - Delete a Geek Term
        5 - Show all dictionary keys and values
        """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # get a definition
    elif choice == "1":
        term = input("What term do you want me to translate? ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know", term)

    # add a term-definition pair
    elif choice == "2":
        term = input("What term do you want to add? ")
        if term not in geek:
            definition = input("\nWhat's the definition? ")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print("\nThat term already exists! Try redefining the term.")

    # Redefine an existing term
    elif choice == "3":
        term = input("What term do you want to redefine? ")
        if term in geek:
            definition = input("What's the new definition? ")
            geek[term] = definition
            print("\n", term, "has been redefined.")
        else:
            print("\nThat term doesn't exist! Try adding it.")

    # delete a term-definition pair
    elif choice == "4":
        term = input("What term do you want to delete? ")
        if term in geek:
            del geek[term]
            print("\nOkay, term", term, "deleted.")
        else:
            print("\nI cannot do that Dave.", term, "doesn't exist in the dictionary.")

    # display all dictionary key:value pairs
    elif choice == "5":
        print(geek.items())

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

input("\nPress the Enter key to exit.")

