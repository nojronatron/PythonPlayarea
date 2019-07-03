import cProfile
import random
import pstats


# my first Python application using Visual Studio!

# function pseudocode:

# integer: findLargest (integer: array[])
#   integer: largest = array[0]
#   for i = 1 to <largest index>
#       if (array[i] > largest) Then largest = array[i]
#       next i
#   return largest


def findLargest(arr):
    largest = int(arr[0])
    i = int(1)
    lenArr = len(arr)
    while (i < lenArr):
        if (arr[i] > largest):
            largest = arr[i]
        i+=1
    return largest


# generate a user-definied list of random ints
userInput = int(input("Enter the size of the array: "))
myList = []
for num in range(0, userInput, 1):
    myList.append(random.randrange(0, userInput, 1))

#print('Starter randomly created list: ', list(myList))

# using cProfile.Profile() directly
pr = cProfile.Profile()
pr.enable()
largest = int(findLargest(myList))
pr.disable()
print('Largest num in array: ', largest)
input("Paused. Press <Enter> to see statistics... ")
# print('...using cProfile.Profile():')
# pr.print_stats()
# print()

# using cProfile.Rum('','') directly
print('...using cProfile.Run("", "")')
cProfile.run('findLargest(myList)', 'stats_findLargest') # writes statistics to physical file
p = pstats.Stats('stats_findLargest')                    # reads statistics file and outputs formatted data
p.strip_dirs().sort_stats(-1).print_stats()
