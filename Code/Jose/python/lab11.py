import string 

abc = string.ascii_lowercase    # abcdefghijklmnopqrstuvwxyz
user_string = input("Enter the string to be encrypted: ")
rotations = int(input("enter the amount of rotations to be used (1, 2, 3... ): "))
new_string = ""    # Creating empty string to be added onto later

for character in user_string:
    new_string += abc[(abc.find(character) + rotations)%26]    # Find specified character in string of characters and return the index, index int is changed depending on the amount of rotations.
print(new_string)                                              # Use the modulo operator to keep our rotations in range (0 - 25). If overboard, it restarts the rotation at index 0.
