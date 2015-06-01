# Car Salesman program
# Chapter 2 page 47

tax = 0.12
licensefee = 0.07
dealerprep = 500
destinationcharge = 700

print("So you're gonna buy a new car? Great!")
stickerprice = float(input("\nWhat is the sticker price?"))

tax *= stickerprice
licensefee *= stickerprice
totalprice = tax + licensefee + dealerprep + destinationcharge + stickerprice

print("\n\nOkay, so after adding tax, license, dealer prep and destination charges,")
print("\nthe total cost is: $",totalprice)

input("Press the Enter key to exit . . .")
