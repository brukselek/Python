#Boolean is a newly discovered data type
#It has two values: False and True (Remember Python is case sensitive so true and false arent correct)
#This chapter also introduces comparison operators, so: ==, !=, <, >, <=, >= which I understand from other languages
#They evaluate to True or False, for example
print(5 > 2)
print(2 == 2)
print(3 > 5)

#They also work with values of any data type, therefore
print()
print('AlaHasACat' == 'AlaHasACat') 
print('alahasacat' == 'AlaHasACat', "therefore it's actually case sensitive")
print(42 == 42.00)
#Whats interesting is that a 42 int value when compared to the 42.0 float value returns true

#We also have three boolean operators introduced: and, or, not
#The and and or operators are self explanatory binary ones.
#The not operator however is an unary operator. It simply evaluates to the opposite boolean value of the expression
print()
print(not True)
print(not not not not True)
