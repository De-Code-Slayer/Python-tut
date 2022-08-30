#  a palindrome is a word that reads the same both forward and backwards

def palindrome(word):
    if word == None or word == '':
        return False
    rev = "".join( reversed(word))
    if word == rev :
        return True
    return False

print(palindrome("111"))