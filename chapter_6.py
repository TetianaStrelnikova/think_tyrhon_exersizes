#As an exercise, write a compare function that takes two values, x and y, and returns 1 if x > y, 0 if x == y, and -1 if x < y.
def compare(x, y):
  if x > y: return 1
  elif x == y: return 0
  elif x < y: return -1
#print(compare(3, 3))
#print(compare(1, 3))
#print(compare(5, 3))

#Use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments. Record each stage of the development process as you go.
import math
#Квадратный корень из числа можно получить с помощью функции sqrt() из модуля math
import cmath
# Для нахождения квадратного корня из комплексного числа: cmath.sqrt().
# Для отрицательных чисел мы должны использовать функцию sqrt() модуля cmath
def exponentiation(a,b): # using the exponentiation operator
  c = (a**2+b**2) 
  return c 

def hypotenuse_smart (a,b):
  hypotenuse_length  =  math.sqrt(exponentiation(a,b))
  return hypotenuse_length

#print(hypotenuse_smart (4,4)) 

#As an exercise, write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.
def is_between(x, y, z):
    if x <= y <= z: 
      return True
    else:
      return False
#print(is_between(2,5,8))
#print(is_between(2,2,0))

#Write a function named ack that evaluates the Ackermann function. Use your function to evaluate ack(3, 4), which should be 125. What happens for larger values of m and n?

def  ack(m,n):
  """Computes the Ackermann function A(m, n)
    n, m: non-negative integers
    """
 
  if m==0 : 
      return  (n + 1)
  elif  m > 0 and n == 0:
      return ack(m - 1,1)
    
  elif m > 0 and n > 0:
        return ack(m - 1,ack(m,n-1))

#print(ack(3,8))

#A palindrome is a word that is spelled the same backward and forward, like “noon” and  “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.
#The following are functions that take a string argument and return the first, last, and middle letters:
def first(word):
  return word[0]
#print(first("hello"))  
def last(word):
  return word[-1]
#print(last("hello"))  
def middle(word):
  return word[1:-1]
#print(middle("hello"))   
# Type these functions into a file named palindrome.py and test them out. What happens if you call middle with a string with two letters? One letter? What about the empty string, which is written '' and contains no letters?
#Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. Remember that you can use the built-in function len to check the length of a string.
def is_palindrome(word):
  if len(word)<= 1:
    return True
  elif first(word) != last(word):
    return False
  else : 
    return is_palindrome(middle(word))
#print(is_palindrome("anna"))

#A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.
def is_power(a,b):
  if  a%b==0:
    is_power(a/b,b)
    return True
  else:
    return False   
#print(is_power(121,11))
#print(is_power(90,3))

#The greatest common divisor (GCD) of a and b is the largest number that dividesboth of them with no remainder.
#One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b,r). As a base case, we can use gcd(a, 0) = a.
#Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
  
def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

print(gcd(436, 12))


#CHAPTER 7
'''As an exercise, rewrite the function print_n from Section 5.8
using iteration instead of recursion.'''

def print_n(s, n):
    if n <= 0:
      return  
    print(s)
    print_n(s, n-1)

def print_n_while(s,n):
  while n>0 :
    print(s)
    n = n-1
print_n_while("Hello",10) #Prints "Hello" 10 times




