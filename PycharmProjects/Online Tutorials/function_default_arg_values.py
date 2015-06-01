# -------------------
# Author: <Author>
# Title: <Title>
# Description: <desc>
# Original: <date>
# Updated: <date>, <updater>
# -------------------

# source: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

ask_ok("Well, what do you say? ")
