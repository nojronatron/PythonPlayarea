# -- data code --
v1 = None       # first argument
v2 = None       # second argument
lstData = None  # result of processing

# --processing code--
# Define the function
def addValues(value1=None, value2=None, value3=None):
    lstResults = None #Holds results list
    if (value3 == None):
        decAnswer = value1 + value2
        lstResults = [decAnswer, value1, value2]
    else:
        decAnswer = value1 + value2 + value3
        lstResults = [decAnswer, value1, value2, value3]
    return lstResults

# --presentation (I/0) code--
# Call the function
lstData = addValues(5, 10)
print(lstData)

lstData = addValues(5, 10, 15)
print(lstData)
