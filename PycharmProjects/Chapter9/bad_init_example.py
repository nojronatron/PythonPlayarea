# -------------------------------------------------#
# Title: <script name>
# Author = 'Orange'
# Date: <date created>
# Desc: <description of script>
# ChangeLog: (Who, When, What)
# -------------------------------------------------#

"""
class MyOtherClass:
    def __init__(self, names):
        self.players = []
        for name in names:
            player = MyNameClass(name)
            self.players.append(player)

    def other_foo(self, arg):
        print(self)
        print(arg)
"""


class MyBadInitClass:
    def ___init__(self, name):
        self.name = name

    def name_foo(self, arg):
        print(self)
        print(arg)
        print("My name is", self.name)


class MyNewClass:
    def new_foo(self, arg):
        print(self)
        print(arg)


my_new_object = MyNewClass()
my_new_object.new_foo("NewFoo")
my_bad_init_object = MyBadInitClass(name="Test Name")
my_bad_init_object.name_foo("name foo")
