import random

wordlist = ['python', 'java', 'kotlin', 'javascript']
pick = random.choice(wordlist)

print("H A N G M A N")
print(f'Guess the word {pick[0:3]}{"-" * (len(pick) - 3)}: ')
guess = input()

if guess == pick:
    print('You survived!')
else:
    print('You are hanged!')
