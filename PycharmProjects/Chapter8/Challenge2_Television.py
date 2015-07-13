# -------------------------------------------------#
# Title: Television Object Challenge Program
# Author = Jonathan Rumsey
# Date: 11-July-2015
# Desc: Write a program that simulates a television by creating it as an object.
#       The user should be able to enter a channel number and raise or lower the volume.
#       Make sure that the channel number and volume level stay within valid ranges.
# ChangeLog: 12-July-2015 - Corrected issues with property and methods (they now work).
#                           Added logic to vol & channel buttons to keep them sane.
#                           Corrected TV status print method so it works, showing correct info.
# -------------------------------------------------#


class Television(object):
    """A television set object"""
    def __init__(self, power="off", channel=3, volume=3):
        self.power = power
        self.channel = channel
        self.volume = volume
        print("A television appears. The power is")

    @property
    def press_power_button(self):
        """
        :return: power state (on or off)
        """
        if self.power == "off":
            self.power = "on"
        else:
            self.power = "off"
        new_power_state = self.power
        return new_power_state

    def change_volume(self, direction):
        """
        :param direction: plus or minus 1 unit
        :return: New volume level
        """
        if direction == "up":
            if self.volume <= 9:
                self.volume += 1
            else:
                print("Volume max is 10.")
        elif direction == "down":
            if self.volume >= 1:
                self.volume -= 1
            else:
                print("Volume minimum is 0.")
        else:
            print("Invalid entry. Please use 'up' or 'down'.")

    def change_channel(self, channel_num):
        """
        :param channel_num: [int] the channel number to change to
        :return: null
        """
        self.channel = channel_num

    def status(self):
        """
        :return: the power state of the television
        """
        print("\n")
        print("The television power is " + self.power + ", the channel is " + \
              str(self.channel) + ", and the volume is set to " + str(self.volume) + ".")
        print("\n")


def main():
    """Main routine"""
    choice = "None"
    my_television = Television()

    print("""
    You take a seat in your living room...
    You want to watch some television....
    You pick up the remote and.....""")
    print("\n")
    while choice != "0":
        print("""
        0 - Quit
        1 - Power On/Off
        2 - Change the Channel
        3 - Volume Up/Down
        4 - Get Status
        """)
        choice = input("Which button do you press?")
        print("\n")
        if choice == "0":
            print("Okay, goodbye.")

        elif choice == "1":
            # Power on/off the television
            power_state = my_television.press_power_button
            print("The television power is now", power_state)

        elif choice == "2":
            # Change channel
            channel_number = int((input("Enter the channel number")))
            if 1 <= channel_number <= 99:
                my_television.change_channel(channel_number)
            else:
                print(channel_number, "is outside the usable range of 1 - 99.")

        elif choice == "3":
            # Change volume
            up_or_down = (input("Press UP or DOWN channel button?")).lower().strip()
            if up_or_down == "up" or "down":
                my_television.change_volume(up_or_down)
            else:
                print(up_or_down, "is not a valid entry. Type 'up' or 'down' to change the volume.")

        elif choice == "4":
            # Get the status of the television
            my_television.status()

        else:
            print("Sorry, choice", choice, "is not valid.")


main()
input("\n\nPress the Enter key to exit.")