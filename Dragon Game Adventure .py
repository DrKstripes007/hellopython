print("Road Maze Game Adventure")
"""A simple Input Interactive Adventure Game"""

directions = input("Choose Directions at the Cross Road Left or Right: ")

if directions == "Left":
    print("Sorry the Dragon Has Burnt you to Cript")
elif directions == "Right":
    print("Welcome to Lake Wakachonga")
else:
    print("Input not recognise")

wait = input ("Welcome to Lake Wakachongo, type 'Wait' to wait for a boat or type 'Swim' to swim across: ")

if wait == "Wait":
    print("You have made it to the House in the Island")
elif wait == "Swim":
    print("You got eaten by Alligator")
else:
    print("I don't understand")


doors =input("Welcome to The House In the Island, Pick a Door, Red or Blue or Green: ")

if doors == "Blue":
    print("You have opened the door to Hades, YOU LOOSE")
elif doors == "Red":
    print("You have opened Door to Antartica, YOU LOOSE")
elif doors == "Green":
    print("'BLAST OFF' You have Won, You opened to Door to the Kitchen")


