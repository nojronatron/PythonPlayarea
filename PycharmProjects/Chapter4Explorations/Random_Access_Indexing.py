__author__ = 'Blue'

# Random Access
# Demonstrates string indexing

import random
word = "index"
print("The word is: ", word, "\n")
print("Length of ", word, " is: ", len(word))

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

print("\n")

position = 0
for j in range(len(word)):
    print("word[", position, "]\t", word[position])
    position += 1

print("\n")

position = -len(word)
for k in range(len(word)):
    print("word[", position, "]\t", word[position])
    position += 1

input("\nPress the Enter key to exit.")
