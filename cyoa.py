"""EX06 - CYOA - Choose your own Adventure."""
__author__ = "730489785"

points: int = 0
"""Let points be the number of rounds the player plays before caught."""
player: str
"""Let player be the name of the player."""

player_pos: int = 0
"""Total unit- position of player."""
player_walks: int = 0
"""Steps (1-5) chosen by player."""
horseman_pos: int = 0
"""Total unit- position of horseman."""
horseman_walks: int = 0
"""Steps (1-5) randomly generated for horseman."""

user_choice: str = ""


def main() -> None:
    """Entrypoint of the program."""
    greet()
    print("")
    print(f"Hello {player}.")
    print("Right now, you are positioned at the entrance of the graveyard.")
    print("The horseman is nowhere to be seen.")
    print("")

    print("Before the game begins, what would you like to do?")
    print(">To start the game, input 'Start'")
    print(">To end the game, input 'Quit'")
    print(">To be greeted again, input 'ReGreet'")
    print("")

    global user_choice
    user_choice = input(">>> Your choice: ")

    while user_choice != "Start" and user_choice != "Quit" and user_choice != "ReGreet":
        print("Please enter a valid input; inputs are case- sensitive")
        print(">To start the game, input 'Start'")
        print(">To end the game, input 'Quit'")
        print(">To be greeted again, input 'ReGreet'")
        print("")
        user_choice = input(">>> Your choice: ")

    if user_choice == "Quit":
        quit_procedure()

    if user_choice == "ReGreet":
        greet()

    global points
    if user_choice == "Start" or user_choice == "ReGreet":
        while points <= 10:
            print("-----------------------------------------------------------------------")
            print(f"{points} OUT OF 10 POINTS")
            print("How many steps would you like to take?")
            
            global player_walks
            player_walks = int(input(">>> Enter an integer between 1 and 5, inclusive: "))
            while int(player_walks) < 1 or int(player_walks) > 5:
                print("That was not an integer between 1 and 5, inclusive.")
                player_walks = input(">>> Enter an integer between 1 and 5, inclusive: ")

            global player_pos
            player_pos += int(player_walks)

            if horse_man_travels(player_pos) is False:
                print("")
                print(f"You are in position {player_pos} currently.")
                print("The horseman is in an unknown position.")
                print("You're safe for now.")
                points = round_tracker(points)
            else:
                print("")
                print("Oh no! The horseman has caught up to you!")
                print(f"The horseman was in position {horseman_pos}; You were also in position {player_pos}.")
                if points == 1:
                    print(f"You have lost the game with {points} point.")
                else:
                    print(f"You have lost the game with {points} points.")
                print("")
                print("Also, the horseman has a message for you:")
                print(f"\"Boo hoo you've been caught, {player}. TIME TO TURN YOU INTO PUMPKIN PIE\"")
                print("")
                quit()
        if points == 10:
            print("")
            print("You have successfully reached the end of the graveyard—— unharmed.")
            print(f"The horseman was in position {horseman_pos} while you ended in position {player_pos}.")
            print("Good play!")
            print("")


def greet() -> None:
    """Welcome message."""
    MOON_EMOJ: str = "\U0001F319"
    HORSE_EMOJ: str = "\U0001F434"
    print("")
    print(f"Welcome to Night{MOON_EMOJ}Mares{HORSE_EMOJ}!")
    print("")
    print("In this game, you are being chased by the headless horseman")
    print("through a graveyard. Your goal is not to get caught by him.")
    print("")
    print("Each round, you will be prompted to input the number of steps——")
    print("1 through 5, inclusive—— that you would like to take from your")
    print("last position. At the same time, the horseman travels an unknown,")
    print("random number of steps——0 through 7, inclusive—— from his last")
    print("position (0 because he can stop since he's less panicked and")
    print("7 cause he trots way faster than you can walk). ")  
    print("Your goal is not to end up in the same exact position as the")
    print("horseman. You have ten rounds to escape him. Good luck!")
    print("")
    global player 
    player = input(">>> Enter your name: ")


def quit_procedure() -> None:
    """End the game experience."""
    global points
    print("")
    print(f"Guess you're not going home today {player}.")
    print(f"and—— surprise, surprise—— you earned {points} point[s].")
    print("")
    print("...")
    print("")
    print("I'll give you a point if you answer this riddle correctly:")
    print("Q: Why did the headless horseman go into business for himself?")
    print("A: He wanted to get ______ in life")
    print("")
    riddle_answer: str = input(">>> Fill in the blank: ")
    if riddle_answer == "ahead" or riddle_answer == "a head" or riddle_answer == "Ahead" or riddle_answer == "A Head" or riddle_answer == "a Head" or riddle_answer == "aHead":
        points += 1 
        print("Correct!")
    else:
        print("No additional points for you!")
    
    print(f"You ended the game with {points} point")
    print("")
    quit() 


def horse_man_travels(position_of_player: int) -> bool:
    """Given the players position, compare to the horseman's position."""
    global horseman_walks
    from random import randrange
    horseman_walks = randrange(0, 7)
    global horseman_pos
    horseman_pos += horseman_walks

    if position_of_player != horseman_pos:
        """Player is safe"""
        return False
    else:
        """Player has lost"""
        return True


def round_tracker(played_round: int) -> int:
    """Given previous round, state next round."""
    global player
    print(f"Tread cautiously {player}")
    print("")
    to_proceed: str = (input(">>> Enter 'X' to claim point or 'Quit' to end game: "))
    while to_proceed != "X" and to_proceed != "Quit":
        to_proceed = input(">>> Invalid input—— Enter 'X' to claim point or 'Quit' to end game: ")
    if to_proceed == "Quit":
        quit_procedure()
    played_round += 1

    return played_round


if __name__ == "__main__":
    main()