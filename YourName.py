#This code (politely) asks for my(your) name and does something with it, Youll have to find out :)

print('Please input your name(that is if youre not scared :) ') #ask for sb's name
myName = input()
print('Just kidding, kiddo!, I just wanted to meet you.')
print('hi! Dummy!, oh, thats not what you typed in? Oh, right, hi, ' + myName + '!')
print('May I ask your age?')
myAge = input()
print('I found out that the length of your name is: ')
print(len(myName)) #len function(so length)
print('Also, in a year youll be: ' + str(int(myAge) + 1) + ' years old!') #int, and str

#Python is case sensitive!
#When Python stops running it TERMINATES or exits, whatever!
#You can use #(hastags) to comment out a part of code if you say want it to stop running for a while(Python skips comments while compiling!
#Obviosly whatevers in parentheses of a function is an argument(duh)
#Calling print with no arguments just prints a blank line
#Input just reads whatever the user types so assigning a value to input() is like assigning an uknown value that the user types in. it evaluates into a string, hence why we had to first type cast to integer(integer cast it)

