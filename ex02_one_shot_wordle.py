"""EX02 - One Shot Wordle - A cuter step toward Wordle."""
__author__ = "730489785"


"""Accept user input"""
sec_word: str = "python"
sec_len: int = len(sec_word)

guess_word: str = input(f"What is your {sec_len}-letter guess? ")
while len(guess_word) != len(sec_word):
    guess_word = input(f"That was not {sec_len} letters! Try again: ")

"""Establish emoji variables and tracking variables"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

indx_track: int = 0 
full_emoj: str = ""

"""Check for letter- matches and form emoji- set accordingly"""
while indx_track < len(sec_word):
    if guess_word[indx_track] == sec_word[indx_track]:
        full_emoj = full_emoj + GREEN_BOX
        indx_track += 1 
    else:
        other_place: bool = False
        alt_indx: int = 0
        while other_place is False and alt_indx < len(sec_word):
            if sec_word[alt_indx] == guess_word[indx_track]:
                other_place = True
            else:
                alt_indx += 1   
        if other_place is True:
            full_emoj = full_emoj + YELLOW_BOX
            indx_track += 1
        else:
            full_emoj = full_emoj + WHITE_BOX
            indx_track += 1 

"""Print results"""
if guess_word == sec_word:
    print(full_emoj)
    print("Woo! You got it!")
else:
    print(full_emoj)
    print("Not quite. Play again soon!")

