# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    secretWord_list = list(secretWord)
    i = 0
    for elem in secretWord_list:
        if elem in lettersGuessed:
            i+= 1

    if i == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    secretWord_list = list(secretWord)
    guess_so_far = '_' * len(secretWord)
    guess_so_far_list = list(guess_so_far)

    for index, elem in enumerate(secretWord_list):
        if elem in lettersGuessed:
            guess_so_far_list[index] = elem

    return ''.join(guess_so_far_list)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet_list = list(string.ascii_lowercase)
    remaining_chars = []
    for elem in alphabet_list:
        if elem not in lettersGuessed:
            remaining_chars.append(elem)
    return ' '.join(remaining_chars)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

def hangman(secretWord):
    lettersGuessed = []
    allLettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is',len(secretWord),'letters long')
    livesLeft = 8

    while livesLeft != 0:
        print('-------------')
        print('You have ' + str(livesLeft) + ' guesses left')
        print('Available Letters:', getAvailableLetters(allLettersGuessed))
        print('Please guess a letter:', end = " ")
        letter = input().lower()

        if letter in secretWord and letter not in lettersGuessed:
            lettersGuessed.append(letter)
            print('Good guess:',getGuessedWord(secretWord,lettersGuessed))
        elif letter not in secretWord and letter not in allLettersGuessed:
            print('Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed))
            livesLeft -= 1
        # elif letter in secretWord and letter in lettersGuessed:
        #     print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
        elif letter in allLettersGuessed:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))

        allLettersGuessed.append(letter)

        if isWordGuessed(secretWord,lettersGuessed) == True:
            print('-----------')
            print('Congratulations, you won!')
            break
        elif isWordGuessed(secretWord,lettersGuessed) == False and livesLeft == 0:
            print('-----------')
            print("Sorry, you ran out of guesses. The word was " + str(secretWord) + '.')


secretWord = 'baloon'
hangman(secretWord)
