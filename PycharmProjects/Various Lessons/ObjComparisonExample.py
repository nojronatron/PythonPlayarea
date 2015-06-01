class demo(object):
    print("asdf")

objD1 = demo() # Make a new demo object
objD2 = demo() # Make another demo object

if (objD1 == objD2):
  print("true")
else:
  print("false") # Will be false this time

if (objD1 is objD2):
    print("IS the same")
else:
    print("IS NOT the same")

objD1 = objD2 # Have the objD1 variable point to the objD2 address

if (objD1 == objD2):
  print("true") # Will be true this time!
else:
  print("false")

if (objD1 is objD2):
    print("IS the same")
else:
    print("IS NOT the same")
