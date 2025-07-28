#hagman game
import random
HANGMAN = (
 """
 -----
 |
 |
 |
 |
 |
 |
 |
 ------
""",
 """
 -----
 |      |
 |      0
 |
 |
 |
 |
 |
 ------
 """,
 """
 -----
 |      |
 |      0
 |     -+-
 |
 |
 |
 |
 ------
 """,
 """
 -----
 |      |
 |      0
 |     /-+-
 |
 |
 |
 |
 ------
 """,
 """
 -----
 |      |
 |      0
 |     /-+-/
 |
 |
 |
 |
 ------
 """,
 """
 -----
 |      |
 |      0
 |    /-+-/
 |      |
 |
 |
 |
 ------
 """,
 """
 -----
 |      |
 |      0
 |    /-+-/
 |      |
 |      |
 |
 |
 ------
 """,
 """
 -----
 |      |
 |      0
 |    /-+-/
 |      |
 |      |
 |    |   |
 |    |   |
 ------
 """)
MAX_WRONG = len(HANGMAN) -1

WORDS = ('OVERUSED','CLAM','GUAM','TAFFETA','PYTHON')
word = random.choice(WORDS) # word to be guessed
so_far = "-" * len(word) #one dahs for each letter to be guessed
wrong = 0   # number of wrong guesses player made
used = []   # letters already guessed
print('Welcome to Hangman.Good luck!')

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print('\n You ve used the following letter: ', used)
    print('\nSo far, the word is: ',so_far)

    guess = input('Enter the guess: ')
    guess = guess.upper() # change to upper case

    while guess in used:
      print('You already guessed the letter ', guess)
      guess = input('Enter your guess: ')
      guess = guess.upper()

    used.append(guess)

    if guess in word:
      print('Yes!', guess, 'is in the word')
      new =""
      for i in range(len(word)):
        if guess == word[i]:
          new += guess
        else:
          new += so_far[i]
      so_far = new

    else:
      print('Sorry', guess, 'is not in the word')
      wrong +=1

if wrong == MAX_WRONG:
  print(HANGMAN[wrong])
  print('You have been hanged')
else:
  print('You guessed it!')

print('The word was ', word)