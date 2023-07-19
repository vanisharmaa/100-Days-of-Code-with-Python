
import random
import hangman_words
import hangman_art
from replit import clear

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear() # clears the output screen before encountering this line
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        # )
        if letter == guess:
            if display[position] != "_" :
              print("You've entered a letter that you've already guessed: " + guess)
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print("You guessed a letter that is not present in the word. A life of yours has been deducted.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
