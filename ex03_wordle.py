"""EX03 - Structured Wordle - very very close to Wordle."""
__author__ = "730489785"

WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
GREEN_BOX: str = "\U0001F7E9"


def contains_char(check_word: str, singl_char: str) -> bool:
    """Returns bool value of if single character found in secret word."""
    assert len(singl_char) == 1
    
    search_indx: int = 0
    while search_indx < len(check_word):
        if check_word[search_indx] == singl_char:
            return True
        else:
            search_indx += 1
            if search_indx == len(check_word):
                return False
    return True


def emojified(guess_string: str, secret_string: str) -> str:
    """Check for letter- matches and form emoji- set accordingly."""
    assert len(guess_string) == len(secret_string)
    full_emoj: str = ""

    indx_track: int = 0
    while indx_track < len(secret_string):
        if guess_string[indx_track] == secret_string[indx_track]:
            full_emoj += GREEN_BOX
            indx_track += 1
        else:
            if contains_char(secret_string, guess_string[indx_track]) is False:
                full_emoj += WHITE_BOX
                indx_track += 1
            else:
                full_emoj += YELLOW_BOX
                indx_track += 1
    
    return full_emoj


def input_guess(exp_length: int) -> str:
    """Given expected length, will ask user for input of expected-length."""
    guess_word: str = input(f"Enter a {exp_length} character word: ")
    while len(guess_word) != exp_length:
        guess_word = input(f"That wasn't {exp_length} chars! Try again: ")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    playing_round: int = 1  
    all_emoj: str = ""
    main_secret: str = "codes"
    guess_accepted: str = ""

    while playing_round <= 6 and guess_accepted != main_secret:
        print(f"=== Turn {playing_round}/6 ===")

        guess_accepted = input_guess(len(main_secret))

        all_emoj = emojified(guess_accepted, main_secret)
        print(all_emoj)

        playing_round += 1

    if guess_accepted != main_secret:
        print("X/6 - Sorry, try again tomorrow!")
    else:
        playing_round = playing_round - 1
        print(f"You won in {playing_round}/6 turns!")


if __name__ == "__main__":
    main()
    
