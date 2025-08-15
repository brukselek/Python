#Flowcharts usually represents decisions with a diamond block (like if statements)
print('Please input your name: ')
name = str(input())

if name == 'Alice': #Starting on the next line is a clause or a block
    print('Hello Alice!') #A block of code
else: #Starting on the next line we have an else clause or an else block
    print('Wait, youre not Alice!')

print('Please enter your password: ')
password = str(input())

if(password =='AliceHasACat'):
    print('Access granted!')
elif(password == '1234'):
    print('Oh come on hacker!')
else:
    print('Wrong password')
