import time

def start_game():
    """Starts the text-based adventure game."""
    print("Hello! Welcome to the game")
    
    # Input with a clear prompt and validation loop
    while True:
        choice = input("Do you want to start the game? Y/N: ").upper()
        if choice in ('Y', 'N'):
            break
        else:
            print("Invalid choice. Please enter Y or N.")

    if choice == 'Y':
        print("Let's Go!!")
    else:
        print("Let's play next time ☹")
        time.sleep(3)  # Reduced delay for better user experience
        return # Exit the game if the user chooses 'N'

    # Display path choices
    print("""\nIn which path you want to go
        A - Concrete road
        B - Road in middle of forest
        C - Swimming through the ocean""")

    # Main game loop for path choice
    while True:
        choice = input("Enter your choice: ").upper()
        
        if choice == 'A':
            # --- Path A: Concrete Road ---
            ch = input("\nThere is a building in the front. Would you want to enter it? Y/N: ").upper()
            if ch == 'Y':
                print("\nYou entered the building....")
                ch1 = input("Would you like to take the lift (type Y) or go from the stairs (type N)? ").upper()
                if ch1 == 'Y':
                    print("\nYou took the lift, and it stopped working and crashed. You died. 💀")
                    time.sleep(3)
                elif ch1 == 'N':
                    ch2 = input("\nYou reached the terrace. You saw a parachute. Would you like to take it? Y/N: ").upper()
                    if ch2 == 'Y':
                        print("\nYou took the parachute and landed on a playground.")
                        print("You went home empty handed. ")
                        time.sleep(3)
                    elif ch2 == 'N':
                        print("\nYou can't do anything. The building security guard caught you and handed you to the police. ")
                        print("You failed. 👮")
                        time.sleep(3)
                    else:
                        print("Invalid choice. Try again.")
                        continue
                else:
                    print("Invalid choice. Try again.")
                    continue
            elif ch == 'N':
                ch1 = input("\nYou passed the building, and now there is a restaurant. Would you like to go and have lunch? Y/N: ").upper()
                if ch1 == 'Y':
                    print("\nYou entered the restaurant....")
                    ch2 = input("You had lunch. Would you like to pay the bill (type Y) or run away (type N)? ").upper()
                    if ch2 == 'Y':
                        # Logical fix: Why would you get arrested for paying the bill? Assuming a 'no money' scenario.
                        print("\nYou paid the bill, but you had no money, so the manager called the police and you got arrested. 💸")
                        time.sleep(3)
                    elif ch2 == 'N':
                        print("\nYou ran away... but somehow the police found you, so you are arrested. 🚨")
                        time.sleep(3)
                    else:
                        print("Invalid choice. Try again.")
                        continue
                elif ch1 == 'N':
                    print("\nYou were just walking randomly and fell into a manhole... You died. 😵")
                    time.sleep(3)
                else:
                    print("Invalid choice. Try again.")
                    continue
            else:
                print("Invalid choice. Try again.")
                continue
            break # Exit loop after path completion

        elif choice == 'B':
            # --- Path B: Forest Road ---
            print("\nYou are lost in the forest...")
            ch = input("There is a cave in front. Would you like to enter it? Y/N: ").upper()
            if ch == 'Y':
                print("\nYou entered the cave. There was a giant inside... he wants to become your friend.")
                ch1 = input("Would you like to become his friend? Y/N: ").upper()
                if ch1 == 'Y':
                    print("\nYou both became friends, and he took you to his kingdom, made you the prince of the kingdom...")
                    print("You both live a happy life! 👑")
                    time.sleep(3)
                elif ch1 == 'N':
                    print("\nGiant became angry and ate you raw.... RIP. 🦴")
                    time.sleep(3)
                else:
                    print("Invalid choice. Try again.")
                    continue
            elif ch == 'N':
                print("\nYou ignored the cave and continued your journey.")
                ch1 = input("You see something buried underground. Would you like to dig and remove it? Y/N: ").upper()
                if ch1 == 'Y':
                    print("\nLucky you! It was a map, and it lead to something. ")
                    ch2 = input("Would you like to follow the map? Y/N: ").upper()
                    if ch2 == 'Y':
                        print("\nYou are following the map, and you ended up under a big tree, and there's a \"X\" mark.")
                        ch3 = input("Would you like to dig it? Y/N: ").upper()
                        if ch3 == 'Y':
                            print("\nYou found nothing...")
                            print("And you got lost in the forest and now you died due to starvation. 😩")
                            time.sleep(3)
                        elif ch3 == 'N':
                            print("\nAnd you got lost in the forest and now you died due to starvation. 😩")
                            time.sleep(3)
                        else:
                            print("Invalid choice. Try again.")
                            continue
                    elif ch2 == 'N':
                        print("\nYou didn't follow the map and went ahead...")
                        ch3 = input("You saw a \"X\" mark in the ground. Would you like to dig and see what's there? Y/N: ").upper()
                        if ch3 == 'Y':
                            print("\nYou found a **treasure worth billions**! You realized that the map was a distraction. 💰")
                            print("You are now a billionaire and living your life peacefully. 🏝️")
                            time.sleep(3)
                        elif ch3 == 'N':
                            print("\nYou went too deep in the forest.")
                            print("You got lost and now you died due to starvation. 😩")
                            time.sleep(3)
                        else:
                            print("Invalid choice. Try again.")
                            continue
                    else:
                        print("Invalid choice. Try again.")
                        continue
                elif ch1 == 'N':
                    print("\nYou continued your journey and came across a river.")
                    ch2 = input("Would you like to swim and cross the river? Y/N: ").upper()
                    if ch2 == 'Y':
                        print("\nYou jumped in the river, and there was a crocodile... and you know what happened next lol. 🐊")
                        time.sleep(3)
                    elif ch2 == 'N':
                        print("\nYou went ahead and found a bridge, and you crossed the river.")
                        ch3 = input("There are two ways. Would you like to go right or left? R/L: ").upper()
                        if ch3 == 'R':
                            print("\nYou chose the **right path** and you reached the city and safely went back home! 🎉")
                            time.sleep(3)
                        elif ch3 == 'L':
                            print("\nYou went along the left path...")
                            print("You saw a cave but you realize that it is the same cave you found at the beginning...")
                            print("And now you are in an **infinite loop**... Bye Have Fun. 🔄")
                            time.sleep(3)
                        else:
                            print("Invalid choice. Try again.")
                            continue
                    else:
                        print("Invalid choice. Try again.")
                        continue
                else:
                    print("Invalid choice. Try again.")
                    continue
            else:
                print("Invalid choice. Try again.")
                continue
            break # Exit loop after path completion
            
        elif choice == 'C':
            # --- Path C: Swimming through the ocean ---
            print("\nYou are swimming in the ocean. 🌊")
            ch1 = input("You found an island. Would like to go there? Y/N: ").upper()
            if ch1 == 'Y':
                print("\nYou are now walking in the island...")
                print("You find that the island is full of **cannibals** 💀")
                ch2 = input("Do you want to run away (type Y) or be friends with them (type N)? ").upper()
                if ch2 == 'Y':
                    print("\nYou are running, and there was a bear trap, and you stepped on it.")
                    print("They found you.... 🩸")
                    time.sleep(3)
                elif ch2 == 'N':
                    print("\nYou tried to be their friend, but you forgot that they don't understand your language...")
                    print("They thought you were teasing them, and they had tasty lunch 🍴")
                    time.sleep(3)
                else:
                    print("Invalid choice. Try again.")
                    continue
            elif ch1 == 'N':
                print("\nYou ignored the island and swam ahead.")
                print("You found 2 fisherman in a boat.")
                ch2 = input("Would you like to join them? Y/N: ").upper()
                if ch2 == 'Y':
                    print("\nThey were very good, and they took you with them, and you safely made it to the land.")
                    print("You are now at home chilling. 😎")
                    time.sleep(3)
                elif ch2 == 'N':
                    print("\nYou told them that you won't come with them.")
                    print("You are now swimming ahead, and you are in the middle of nowhere...")
                    print("You died.... 👻")
                    time.sleep(3)
                else:
                    print("Invalid choice. Try again.")
                    continue
            else:
                print("Invalid choice. Try again.")
                continue
            break # Exit loop after path completion
            
        else:
            print("\nSelect a correction option!! A, B, or C.")
            # The loop continues here if the choice is invalid

if __name__ == "__main__":
    start_game()