# 1. Palindrome 
def is_palindrome(word):
  word = word.lower()
  return word == word[::-1]

print(is_palindrome('Deleveled'))
# This should print True