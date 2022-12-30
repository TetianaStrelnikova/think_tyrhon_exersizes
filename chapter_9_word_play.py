"""
Exercise 9.1. 
Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).
"""

    
fin = open('words.txt','r')
for line in fin:
  word = line.strip()
  if len(word) > 20:
    print(word)
  
  
"""
Exercise 9.2. 
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do. In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility.
All right, I’ll stop now.
Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
Write a program that reads words.txt and prints only the words that have no “e”. Compute the
percentage of words in the list that have no “e”.
"""

def has_no_e(word):
    for letter in word:
        if letter == "e":
            return False
    return True

fin_2 = open('words.txt','r')
for line in fin_2:
  word = line.strip()
  if has_no_e(word):
    print(word)
"""
Exercise 9.3. 
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words? i e a o u 
"""
def avoids(word, forbidden):
  for letter in word:
        if letter in forbidden:
            return False
  return True

fin_3 = open('words.txt','r')
forbidden = input("enter forbidden letters:")
for line in fin_3:
  word = line.strip()
  if avoids(word,forbidden):
    print(word)

"""
Exercise 9.4. 
Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?
"""
def uses_only(word, str):
  for letter in word:
    if letter not in str:
      return False
  return True

fin_5 = open('words.txt','r')
for line in fin_5:
  word = line.strip()
  if uses_only(word,"acefhlo"):
     print(word)
  
"""
Exercise 9.5. 
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are there that use all the vowels aeiou? How about aeiouy?
"""
def uses_all(word, str):
  for letter in str:
    if letter not in word:
      return False
  return True
  
fin_4 = open('words.txt','r')
for line in fin_4:
  word = line.strip()
  
  if uses_all(word,"aeiou"):
     print(word)


"""
Exercise 9.6.
Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?
"""
def is_abecedarian(word):
  if list(word) != sorted(word):
    return False
  return True


fin_6 = open('words.txt','r')
for line in fin_6:
  word = line.strip()
  if is_abecedarian(word):
    print(word)