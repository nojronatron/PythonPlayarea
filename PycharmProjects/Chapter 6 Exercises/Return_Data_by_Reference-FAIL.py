# -- data code --
v1 = 10      # first argument
v2 = 5       # second argument
decAnswer = None  # result of processing

# --processing code--
# Define the function
def AddValues(value1, value2, answer):  # answer receives the value not the address!
        answer = value1 + value2

# --presentation (I/0) code--
# Call the function

AddValues(v1, v2, decAnswer)
print("The Sum of the values "
      + str(v1) + " and " + str(v2) + " is: " + str(decAnswer))
# This prints out -- "The Sum of the values 10 and 5 is: None." Doh!
