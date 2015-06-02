# -------------------------------------------------#
# Title: Handling Multiple Exception Types
# Author = Jon Rumsey
# Date: 25-May-2015
# Desc: One way to trap for multiple exception types
#        is to list them in a single 'except' clause
#        as a comma-separated group enclosed in a
#        set of parentheses.
# ChangeLog: initial
# -------------------------------------------------#

# -- Data --# 
# -- Processing --#
# -- Presentation (I/O) --#

# handle multiple exception types
print()
for value in (None, "hi"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError as e:
        print("I can only convert a string of digits!")
        print("Value Error 'e' is -->", e)

# to except two types in one line do:
#    except (TypeError, ValueError):
else:
    print("\nThe ELSE clause fired.")
    print("\nPress the Enter key to quit.")