'''Exercise 8.1. 
Read the documentation of the string methods 
at http: // docs. python. org/ 3/library/ stdtypes. html# string-methods .
You might want to experiment with some of them to make sure you understand how they work. 
strip and replace are particularly useful.
The documentation uses a syntax that might be confusing. 
For example, infind(sub[, start[, end]]), the brackets indicate optional arguments. 
So sub is required, butstart is optional, and if you include start, then end is optional.'''



flower = "Hibiscus"
flower_2 = "Chamomilla officinalis"
print(len(flower))
print(len(flower_2))

'''Exercise 8.3. 
A string slice can take a third index that specifies the “step size”; 
that is, the numberof spaces between successive characters. 
A step size of 2 means every other character; 3 means every third, etc.
80 Chapter 8. Strings
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
Use this idiom to write a one-line version of is_palindrome from Exercise 6.3.'''
def is_palindrome(word):
  while len(word)>0:
    if word[0] == word[-1]:
      word = word[1:-1]
    else:
      return False
  else:
    return True

print(is_palindrome("alla"))
print(is_palindrome("hello"))
'''Exercise 8.4. 
The following functions are all intended to check whether a string contains any lowercase letters, 
but at least some of them are wrong. For each function, describe what the function actually does 
(assuming that the parameter is a string).
#function is supposed to check whether its argument has ANY lowercase letters
#To test the function I will make different call'''
# 1 
# If any string whose first character is an uppercase letter and other letters are lowercase letters is passed as an argument, the function will return False which is incorrect.
def any_lowercase1(s):           # Declare a function is_lowercase with parameter (s)
                                
     for c in s:                 # using "for" loop through the letters (c) in string (s) 
          if c.islower():        # using if statement with the condition :
                                 # .islower() method (is True?) checking if the letters in the text are in lower case.
                                 # .islower() method returns the value True or False after checking the FIRST letter
                                 # the for loop will exit and return False in case the letter will be Uppercase               
                return True      # returns True in case the first letter will be lowercase 
                     
          else:                  # else statement condition: 
               return False      # return boolean False when  .islower() method returns False

# call the function any_lowercase1() passing the argument string to the function. The argument  is assignув to the function parameter (s) and print the result              
print(any_lowercase1("Tati"))  # s = "TaTi" the loop will go through 4 letters : "T","a", "T" and "i"
print(any_lowercase1("tAti"))  # s = "tAti" the loop will go through 4 letters : "t","A", "t" and "i"
print(any_lowercase1("taTi"))  # s = "taTi" the loop will go through 4 letters : "t","a", "T" and "i"
print(any_lowercase1("tatI"))  # s = "tatI" the loop will go through 4 letters : "t","a", "t" and "I"
print(any_lowercase1("tati"))  # s = "tati" the loop will go through 4 letters : "t","a", "t" and "i"
print(any_lowercase1("TATI"))  # s = "TATI" the loop will go through 4 letters : "T","A", "T" and "I"
# If any string whose first character is an uppercase letter and other letters are lowercase letters is passed as an argument, the function will return False which is incorrect.  
# 1,2,3,4,5 calls are incorrect (6th wants to appear to be correct😂'''
# 2
# Function returns True in ane case as the condition 'c'.islowercase == True< Which is wrong as in the string which is passed as an argument could be no lowercase letters as in the last call
def any_lowercase2(s):      
     for c in s:                # using "for" loop through the letters (c) in string (s) 
          if 'c'.islower():     # this function has a different condition in the if statement:
                                # .islower() method checking if the string ("c"), butnot the (c) is in lower case. 
                                # This condition is True  'c'.islowercase == True
               return 'True'    # function returns a srting "True" if the 'c'.islower() is True
          else:
               return 'False'
# call the function any_lowercase1() passing the argument string to the function. The argument  is assignув to the function parameter (s) and print the result  
print(any_lowercase2("Tati"))  # s = "TaTi" the loop will go through 4 letters : "T","a", "T" and "i"
print(any_lowercase2("tAti"))  # s = "tAti" the loop will go through 4 letters : "t","A", "t" and "i"
print(any_lowercase2("taTi"))  # s = "taTi" the loop will go through 4 letters : "t","a", "T" and "i"
print(any_lowercase2("tatI"))  # s = "tatI" the loop will go through 4 letters : "t","a", "t" and "I"
print(any_lowercase2("tati"))  # s = "tati" the loop will go through 4 letters : "t","a", "t" and "i"
print(any_lowercase2("TATI"))  # s = "TATI" the loop will go through 4 letters : "T","A", "T" and "I"   
# Function returns True in ane case as the condition 'c'.islowercase == True< Which is wrong as in the string which is passed as an argument could be no lowercase letters as in the last call
# 6th call gives incorrect result (1,2,3,4,5th wants to appear to be correct😂
# 3
#If any string whose last letter is an uppercase letter and other letters are lowercase letters is passed as an argument, the function will return False which is incorrect.
def any_lowercase3(s):
    for c in s:                 # using "for" loop through the letters (c) in string (s) 
                                # this function has NO if statement
          flag = c.islower()    # declare a variable flag inside the for loop with the value of the result .islower() method (True or False)
                                #The value of variable flag will be reassiging every time through the for loop
                                #the last value will be the .islowercase method for the last letter
    return flag                 # function returns  variable flag, which is boolean True or False
# call the function any_lowercase1() passing the argument string to the function. The argument  is assignув to the function parameter (s) and print the result  
print(any_lowercase3("Tati"))  # s = "TaTi" the loop will go through 4 letters : "T","a", "T" and "i"
print(any_lowercase3("tAti"))  # s = "tAti" the loop will go through 4 letters : "t","A", "t" and "i"
print(any_lowercase3("taTi"))  # s = "taTi" the loop will go through 4 letters : "t","a", "T" and "i"
print(any_lowercase3("tatI"))  # s = "tatI" the loop will go through 4 letters : "t","a", "t" and "I"
print(any_lowercase3("tati"))  # s = "tati" the loop will go through 4 letters : "t","a", "t" and "i"
print(any_lowercase3("TATI"))  # s = "TATI" the loop will go through 4 letters : "T","A", "T" and "I"
#If any string whose last letter is an uppercase letter and other letters are lowercase letters is passed as an argument, the function will return False which is incorrect.
# 4th call gives incorrect result (1,2,3,5.6th wants to appear to be correct😂)
# 4
#function is supposed to check whether its argument has ANY lowercase letters
#If any string whose ANY letter is an LOWERCASE is passed as an argument,
#the function will reassign the variable flag from False to True and return flag == True,  which is CORRECT.
def any_lowercase4(s):
     flag = False                    #declare variable flag with the value boolean False
     for c in s:
          flag = flag or c.islower() #reassigns the variable flag in case c.islower() == True
     return flag                     #returnes flag
# call the function any_lowercase1() passing the argument string to the function. The argument  is assignув to the function parameter (s) and print the result  
print(any_lowercase4("Tati"))  # s = "TaTi" the loop will go through 4 letters : "T","a", "T" and "i"
print(any_lowercase4("tAti"))  # s = "tAti" the loop will go through 4 letters : "t","A", "t" and "i"
print(any_lowercase4("taTi"))  # s = "taTi" the loop will go through 4 letters : "t","a", "T" and "i"
print(any_lowercase4("tatI"))  # s = "tatI" the loop will go through 4 letters : "t","a", "t" and "I"
print(any_lowercase4("tati"))  # s = "tati" the loop will go through 4 letters : "t","a", "t" and "i"
print(any_lowercase4("TATI"))  # s = "TATI" the loop will go through 4 letters : "T","A", "T" and "I"
#If any string whose ANY letter is an LOWERCASE is passed as an argument,
#the function will reassign the variable flag from False to True and return flag == True,  which is CORRECT.
# All calls are correct
# 5
#function is supposed to check whether its argument has ANY lowercase letters
#In this function if as the argument passed the string where any letter is Uppercase the function will return False (so no matter if there are any lowercase letters) Even if there only one Uppercase letter the function  will return False. The function will return True only if all letters are lowercase, which is incorrect
def any_lowercase5(s):
    for c in s:
          if not c.islower(): #condition with the if statement
                              # if not c.lower( == True), it also the same as if c.islowewr() == False
            return False      #the function will returns False (in case the c.islower()==True)
                              #in case c.islower == True it will return True '''😱 My poor brain 🤯😂'''
    return True
# call the function any_lowercase1() passing the argument string to the function. The argument  is assignув to the function parameter (s) and print the result       
print(any_lowercase5("Tati"))  # s = "TaTi" the loop will go through 4 letters : "T","a", "T" and "i"
print(any_lowercase5("tAti"))  # s = "tAti" the loop will go through 4 letters : "t","A", "t" and "i"
print(any_lowercase5("taTi"))  # s = "taTi" the loop will go through 4 letters : "t","a", "T" and "i"
print(any_lowercase5("tatI"))  # s = "tatI" the loop will go through 4 letters : "t","a", "t" and "I"
print(any_lowercase5("tati"))  # s = "tati" the loop will go through 4 letters : "t","a", "t" and "i"
print(any_lowercase5("TATI"))  # s = "TATI" the loop will go through 4 letters : "T","A", "T" and "I"
#In this function if as the argument passed the string where any letter is Uppercase the function will return False (so no matter if there are any lowercase letters) Even if there only one Uppercase letter the function  will return False. The function will return True only if all letters are lowercase as in the 5th call), which is incorrect

'''Exercise 8.5. 
A Caesar cypher is a weak form of encryption that involves “rotating” each letter by
a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around
to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7 is “jolly”
and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the ship computer
is called HAL, which is IBM rotated by -1.
Write a function called rotate_word that takes a string and an integer as parameters, and returns
a new string that contains the letters from the original string rotated by the given amount.
You might want to use the built-in function ord, which converts a character to a numeric code, and
8.13. Exercises 81
chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical
order, so for example:
>>> ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case
letters are different.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar
cypher with rotation 13. If you are not easily offended, find and decode some of them. Solution:
http: // thinkpython2. com/ code/ rotate. py .'''