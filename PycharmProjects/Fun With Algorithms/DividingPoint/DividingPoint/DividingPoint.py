import random
import pstats
import cProfile


# pseudocode DividingPoint
#
# Integer: DividingPoint(Integer: array[])
#   Integer: number1 = array[0]
#   Integer: number2 = array[<last index of array>]
#   Integer: number3 = array[<last index of array> / 2]
#   if (<number1 is between number2 and number3>) Return number1
#   if (<number2 is between number1 and number3>) Return number2
#   Return number3
# End DividingPoint

def dividingPoint(arr):
    lenArr = int(len(arr))
    number1 = int(arr[0])
    number2 = int(arr[-1])
    number3 = int(arr[int(lenArr / 2)])
    if (number2 < number1 < number3):
        return number1
    if (number1 < number2 < number3):
        return number2
    return number3

rand = random
print("***** Fun with Algorithms: Dividing Point *****")
arrSize = int(input("Enter the array size to generate and test: "))
myArr = []
for item in range(0, int(arrSize), 1):
    myArr.append(rand.randrange(0, arrSize+1))
if('y' in input('print myArr (y/n)? ')):
    print("myArr = ", myArr)
cProfile.run('dividingPoint(myArr)', 'stats_divPoint') # writes statistics to physical file
p = pstats.Stats('stats_divPoint')                    # reads statistics file and outputs formatted data
print('\ncProfile.Run("", "") statistics...')
p.strip_dirs().sort_stats(-1).print_stats()
