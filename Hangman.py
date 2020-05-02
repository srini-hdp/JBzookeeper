import random

wordlist = ['python', 'java', 'kotlin', 'javascript']
pick = list(random.choice(wordlist))
tries = 0
print("H A N G M A N")
guessed_list = list('-' * len(pick))
wrong_list = list()

while tries < 8:
    print()
    print("".join(guessed_list))
    if guessed_list == pick:
        print('You guessed the word!')
        print('You survived!')
        break
    guess = input('Input a letter:')

    if len(guess) != 1:
        print('You should print a single letter')
        continue
    elif not guess.islower():
        print('It is not an ASCII lowercase letter')
        continue

    if guess in pick and guess not in guessed_list:
        i = 0
        while i < len(pick):
            if guess == pick[i]:
                guessed_list[i] = pick[i]
            i += 1
        continue
    elif guess in guessed_list or guess in wrong_list:
        print('You already typed this letter')
        continue
    else:
        print('No such letter in the word')
        wrong_list.append(guess)
        tries += 1
else:
    print('You are hanged!')
