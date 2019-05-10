import random


def hangman():
    word_list = ["python", "java", "computer", "hacker", "painter", "whiskey", "tequila"];
    random_number = random.radiant(0,6)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = [" ", "_____    ", "|  |  ", "| 0 ", "|   /|\  ", "|  /\  ", "|" ]
        remaining_letters = list(word)
        letter_board = ["__"] * len(word)
        win = False
        print('Welcome to Hangman')
        while worng_guesses < len(stages) - 1:
            print('\n')
            guess = input("Guess a letter")
            if guess in remaining_letters:
                character_index = remaining_letters.index(guess)
                letter_board[character_index]= guess
                remaining_letters[character_index]= '$'
            else: wrong_guesses + = 1
            print((''.join(letter_board)))
            print('\n'.join (stages[0:wrong_guesses + 1]))
            if '__' not in letter_board:
                print('You win! The word was:')
                print(''.join(letter_board))
                win = True
                break
            if not win:
                print('\n'.join(stages[0:wrong_guesses]))
                print('You lose!'The word was {}.format(word))
hangman()
