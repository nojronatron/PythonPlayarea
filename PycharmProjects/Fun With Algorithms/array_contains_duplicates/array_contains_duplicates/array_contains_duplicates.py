import random
import cProfile
import pstats


# pseudocode

# Boolean: ContainsDuplicates(Integer: array[])
    # Loop over all of the array's items.
#   For i=0 To <largest index>
#       For j=0 To <largest index>
            # See if these two items are duplicates.
#           If (i != j) Then
#               If (array[i] == array[j]) Then Return True
#           End If
#       Next j
#   Next i
    # If we get to this point there are no duplicates
#   Return False
# End ContainsDuplicates

def ContainsDuplicates(arr):
    lenArr = len(arr)
    for i in range(0, lenArr, 1):
        for j in range(0, lenArr, 1):
            if (i != j):
                if (arr[i] == arr[j]):
                    return True
    return False

print("***** Fun with pseudocode and Python *****")
myArr = []
userNum = int(input('\nEnter the number of elements to add to an array: '))
rand = random
for i in range(0, userNum, 1):
    myArr.append(rand.randrange(0, userNum+1, 1))
# solution = "contains dupes" if (ContainsDuplicates(myArr)) else "is all unique integers"
# print("\nArray myArr ", solution, "!\n")

# get stats using cProfile.Run('','') directly
print('...using cProfile.Run("", "")')
cProfile.run('ContainsDuplicates(myArr)', 'stats_containsDupes')    # writes statistics to physical file
p = pstats.Stats('stats_containsDupes')                             # reads statistics file and outputs formatted data
p.strip_dirs().sort_stats(-1).print_stats()

userResponse = input("\n\nDo you want to see the array (y/n)? ")
if ("y" in userResponse):
    print("\n", myArr)
print()
