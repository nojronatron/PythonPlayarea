# -------------------------------------------------#
# Title: Global Reach
# Author = Jon Rumsey
# Date: 23-May-2015
# Desc: Demonstrates global variables: Read, Change, and Shadow
# ChangeLog: Initial
# -------------------------------------------------#

# -- Data --# 
value = 10


# -- Processing --#
def read_global():
    print("From inside the local scope of read_global(), value is:", value)


def shadow_global():
    value = -10
    print("From inside the local scope of shadow_global(), value is:", value)


def change_global():
    global value
    value = -10
    print("From inside the local scope of change_global(), value is:", value)

# -- Presentation (I/O) --#
print("In the global scope, value is still:", value, "\n")

read_global()
print("Back in the global scope, value is still:", value, "\n")

shadow_global()
print("Back in the global scope, value is still:", value, "\n")

change_global()
print("Back in the global scope, value has now changed to:", value)

input("\n\nPress Enter key to exit.")
