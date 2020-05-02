import random

wordlist = ['python', 'java', 'kotlin', 'javascript']
pick = list(random.choice(wordlist))
tries = 8
print("H A N G M A N")
guessed_list = list('-' * len(pick))

for n in range(tries):
    print()
    print("".join(guessed_list))
    guess = input('Input a letter:')

    if guess in pick:
        i = 0
        while i < len(pick):
            if guess == pick[i]:
                guessed_list[i] = pick[i]
            i += 1
    else:
        print('No such letter in the word')

print("""
Thanks for playing!
We'll see how well you did in the next stage""")
