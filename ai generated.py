import time

def adventure_game():
    print("Welcome to the Adventure Game!")
    time.sleep(2)
    print("You find yourself in a Cross Road to choose.")
    time.sleep(2)
    print("You have two paths in front of you: left or right.")

    choice = input("Which path will you choose? (left or right): ").lower()

    if choice == "left":
        print("You follow the left path and came across a Lake called 'WakaChonga'.")
        time.sleep(2)
        print("Welcome To WakaChonga Lake.")
        time.sleep(2)
        print("You can swim across to the Island or Wait for a Boat. What will you do?")
        choice = input("Swim or Wait ? (Swim or Wait): ").lower()

        if choice == "wait":
            print("The Boat shows up and Has taken you to An Island!")
            time.sleep(2)
            print("Welcome to Captain Treasure Island")
            time.sleep(2)
            print("You are on your way to the Captain's Treasure House")

            choice = input("Open a Door to get to the Treasure Room! (Red or Blue): ").lower()

            if choice == "red":
                print("You have opened the Door to Hades, 'Welcome To Hell' ")
                time.sleep(2)
                print("Game Over. Thanks for playing")
            elif choice == "blue":
                print("You have opened the Door to the Captain's Treasure Room WHAT TOOK YOU SO LONG ? ")
                time.sleep(2)
                print("Congratulations : YOU HAVE WON : DANKE ")
            else:
                print("Invalid choice. Game Over.")

        elif choice == "swim":
            print("You decided to swim and you have been bitten by Ruby the Aligator.")
            time.sleep(2)
            print("Game Over. Thanks for playing!")
        else:
            print("Invalid choice. Game Over.")

    elif choice == "right":
        print("You follow the right path and encounter a fierce dragon!")
        time.sleep(2)
        print("The dragon burned you to Crispy pie.")
        time.sleep(2)
        print("Game Over. Try another Time")

    else:
        print("Invalid choice. Game Over.")

if __name__ == "__main__":
    adventure_game()
