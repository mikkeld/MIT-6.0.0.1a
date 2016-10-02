import sys
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        del str[str.index(letter)]

    return str

getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])