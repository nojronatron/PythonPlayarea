__author__ = 'Blue'

# Chapter 4 page 91
# Shows how to use the range() function with a for loop to count

print("Counting:")
for i in range(10):
    print(i, end=" ")

print("\n\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nPress the Enter key to exit.\n")
