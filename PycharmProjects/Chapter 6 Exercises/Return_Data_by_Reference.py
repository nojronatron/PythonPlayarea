# -- data code --
v1 = 10      # first argument
v2 = 5       # second argument
decAnswer = [None]  # result of processing in a list

# --processing code--
# Define the function

def AddValues(value1, value2, answer):  # answer receives the address this time!
      answer[0] = value1 + value2   # answer is a list object, so you use an index [0]!

# --presentation (I/0) code--
# Call the function

AddValues(v1, v2, decAnswer)
print("The Sum of the values "
      + str(v1) + " and " + str(v2) + " is: " + str(decAnswer[0]))
# This prints out -- "The Sum of the values 10 and 5 is: 15"
