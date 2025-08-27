alphabet = "abcdefghijklmnopqrstuvwxyz"

# Asks for command
command = input("Enter command (press 'e' to encode, 'd' to decode, 'q' to quit): ")

# While statement is used here to create the loop until 'q' is pressed.
while command != 'q':
    if command == 'e':
        string = input("Enter text/message to encode: ")
        rotated = int(input("Enter rotation integer between 1-25: "))
        if rotated >= 1:
            if rotated <= 25:
                #ra stands for rotated alphabet, the rotated alphabet is made to be empty so that I add parts of the alphabet to the list
                ra = []
                # The append here is used to add the part of the alphabet list from the "rotated" to the end of "ra" the rotated alphabet
                for i in range(rotated, len(alphabet)):
                    ra.append(alphabet[i])
                for i in range(rotated):
                    ra.append(alphabet[i])
                stringisencoded = ''
                # Each letter entered gets encoded using the Caesar cipher rotated alphabet
                for letter in string:
                    if letter in alphabet:
                        # This line goes through each letter in the alphabet
                        for i in range(len(alphabet)):
                            if letter == alphabet[i]:
                                stringisencoded += ra[i]
                            else:
                                if letter != alphabet[i]:
                                    stringisencoded += ''
                    else:
                        if letter not in alphabet:
                            stringisencoded += letter
                # This is to check if the string is encoded
                if stringisencoded != '':
                    print("Encoded string:", stringisencoded)
                else:
                    print("Encoding process failed.")
            else:
                if rotated > 25:
                    print("Bad rotation. Enter a number between 1 and 25.")
        else:
            if rotated > 1:
                print("Bad rotation. Enter a number that is between 1 and 25.")
            
    elif command == 'd':
        stringisencoded = input("Enter a string to decode: ")
        word = input("Enter a word in the string: ")
        # The code = false is meant to check whether the correct rotation is found
        code = False
        rotated = 1
        # This section goes through the rotated alphabet to check all of the rotations for the correct one
        while rotated <= 25:
            ra = []
            for i in range(rotated, len(alphabet)):
                ra.append(alphabet[i])
            for i in range(rotated):
                ra.append(alphabet[i])
            stringisdecoded = ''
            # The for letter in stringisencoded decodes each letter.
            for letter in stringisencoded:
                if letter in ra:
                    for i in range(len(ra)):
                        if letter == ra[i]:
                            stringisdecoded += alphabet[i]
                        else:
                            if letter != ra[i]:
                                stringisdecoded += ''
                else:
                    if letter not in ra:
                        stringisdecoded += letter
            # This if statement checks if it is decoded and if it isnt it will print a message saying so
            if stringisdecoded != '':
                if word in stringisdecoded:
                    print("Rotation: " + str(rotated) + ", Decoded string: " + stringisdecoded)
                    code = True
                else:
                    print("Word cant be found in this rotation.")
            else:
                print("Decoding process failed.")
            rotated += 1
        if code == False:
            print("No correct rotations found.")

    else:
        print("Invalid command. Enter 'e', 'd', or 'q'.")
    
    # This asks the user for another command again at the end of the loop
    command = input("Enter command ('e' to encode, 'd' to decode, 'q' to quit): ")
    if command not in ['e', 'd', 'q']:
        print("Invalid command. Please enter 'e', 'd', or 'q'.")
        command = input("Enter command ('e' to encode, 'd' to decode, 'q' to quit): ")
print("Later!")
