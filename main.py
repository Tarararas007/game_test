import re
import random

words = ["hello", "word", "python", "game"]
selection_word = random.choice(words)
attempts = int(input("Enter the number of attempts: "))
guessed_word = ["*"] * len(selection_word)
count = 0

while True:import re
import random

words = ["hello", "word", "python", "game"]
selection_word = random.choice(words)
attempts = int(input("Enter the number of attempts: "))
guessed_word = ["*"] * len(selection_word)
count = 0

while True:
    if count == attempts:
        print("GAME OVER")
        break

    elem = input("Enter letter or word: ")

    if len(elem) == 1:
        if elem in selection_word:
            for i in range(len(selection_word)):
                if selection_word[i] == elem:
                    guessed_word[i] = elem

            print("".join(guessed_word))
            if "*" not in guessed_word:
                print("You won! The word was:", selection_word)
                break

        else:
            print("Invalid letter")
            count += 1
    else:
        if elem == selection_word:
            print("You won! The word was:", selection_word)
        else:
            print("Invalid word")
            count += 1

    if count == attempts:
        print("GAME OVER")
        break

    elem = input("Enter letter or word: ")

    if len(elem) == 1:
        if elem in selection_word:
            for i in range(len(selection_word)):
                if selection_word[i] == elem:
                    guessed_word[i] = elem

            print("".join(guessed_word))
            if "*" not in guessed_word:
                print("You won! The word was:", selection_word)
                break

        else:
            print("Invalid letter")
            count += 1
    else:
        if elem == selection_word:
            print("You won! The word was:", selection_word)
        else:
            print("Invalid word")
            count += 1
