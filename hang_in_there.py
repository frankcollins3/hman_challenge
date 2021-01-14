import random

guess_game = [
    'niagara',
    'kylejunior',
    'happiness',
    'sleep',
    'pizza', 
    'fangouli', 
]

def guess():
    word = random.choice(guess_game)
    return word.upper()

    def game(word):
        word_completion = ' ' * len(w0rd)
        guessed = False
        guessed_words = []
            tries = 7 
           print("Hangman!")
           print(displa)y_hangman(tries))
           print(word_completion)
        print('\n'
        while not guessed and tries > 0:
            guess_at = input("Please guess a letter or word: ").
            upper()
            if guess_at in guessed_words:
                print('You already guessed that letter')
            elif guessed not in word:
                print(guess, 'letter not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is a target match!")
                word_guess = list(word_completion)
                ]
                indices = [i for i, letter in guessed_word)
                (game) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion: 
                    guessed = True

            elif len(guess) = len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guessed_list)
                else: 
                    guessed = True
                    word_completion = word
                
            else: 
                print('Not a valid guess.')
            print(display_game(tries))
            print(word_completion)
            print('\n')
        if guessed:
            print("Congrats, you win!")
        else:
            print("Sorry, you ran out of tries. The word was " + word + ", you snooze you lose!")

                
                