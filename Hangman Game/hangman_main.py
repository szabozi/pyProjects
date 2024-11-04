import random

# Open txt file with all the words as read-only and assign it to words list
# Each word has a \n (new line) at the end, ex.: 'accomplish\n'
with open('assets/words.txt', 'r') as f:
    words = f.readlines()

# Using 'random' we take 1 random word from words
# Using [:-1] we remove the '\n' from the selected word from the list
word = random.choice(words)[:-1]
print(word)

# Allowing the player 10 chances to solve the game
allowed_errors = 6

# We store the found letters in a list
guesses = []

# We store the all letters in a list
letters = []

# Creating an 'infinite' while loop, with the following options:
#   -if allowed_errors reaches 0 we break out of the loop
#   -if the random word has been solved then we change done = False to True and we continue outside the loop
done = False
while not done:
    # Here we change the letters from words into '_ _ _ _'
    # If a letter has been found we change the '_' with the letter
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print(" ")

    # Here we count the allowed_errors left and ask the user to input a new letter
    guess = input(f"\nErrors left: {allowed_errors} \nLetters used so far:{letters} \nNext Guess please: ")
    guesses.append(guess.lower())
    letters.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors = allowed_errors - 1
        if allowed_errors == 0:
            # Once allowed_error reaches 0 we break out of the entire while loop
            break

    # Once the word has been found we set done to True, so we could exit the while loop
    done = True

    # If the letter inputted by the user is not the selected word:
    #   -we remain in the while infinite loop, so done = False
    for letter in word:
        if letter.lower() not in guesses:
            done = False


if done:
    print(f"\nYou found the word! \nIt was: '{word}'!")
else:
    print(f"\nGame Over! \nThe word was: '{word}'!")
