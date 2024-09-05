# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
##print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.
#name = input("enter name")
##print( name )
#print( name )




## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.
#name= input("enter name")
#print("!" + name + "!" + name +"!")
## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630
#fname=input("print first name")
#sname=input("print last name")
#address=input("print address")
#code=input("enter city and postal code")
#print("First name: " + fname)
#print("Second name: " + sname)
#print("Street address: " + address)
#print("City and postal code: " + code)

## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out
#w1= input("enter word 1")
#w2= input("enter word 2")
#w3= input("enter word 3")
#print(w1+"-"+w2+"-"+w3)
## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.
n=input("enter name")
p=input("enter a year")
print(n+" was a wonderful hero born in " + p + " who grew up capturing butterflies")
print("On a dimly lit morning " + n + " was shot by multiple forces who consisted of their opposition and enemies")
print("Though they were only born in" + p + " , " + n + " was a wonderful warrior and will always be remembered." )