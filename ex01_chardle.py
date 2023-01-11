"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730489785"
 

goal_word: str = input("Enter a 5- character word: ")
if len(goal_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()


print("Searching for " + single_character + " in " + goal_word)

pos_0 = (goal_word[0])
pos_1 = (goal_word[1])
pos_2 = (goal_word[2])
pos_3 = (goal_word[3])
pos_4 = (goal_word[4])

instance: int = 0

if pos_0 == single_character:
    print(single_character + " found at index 0")
    instance = instance + 1

if pos_1 == single_character:
    print(single_character + " found at index 1")
    instance = instance + 1

if pos_2 == single_character:
    print(single_character + " found at index 2")
    instance = instance + 1

if pos_3 == single_character:
    print(single_character + " found at index 3")
    instance = instance + 1
    
if pos_4 == single_character:
    print(single_character + " found at index 4")
    instance = instance + 1


if instance == 0:
    print("No instances of " + single_character + " found in " + goal_word)
else: 
    if instance == 1:
        print("1 instance of " + single_character + " found in " + goal_word)
    else:
        print(str(instance) + " instances of " + single_character + " found in " + goal_word)
