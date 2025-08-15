import sys
print('Enter TB or GB for advertised unit: ')
unit = input('>')

#Calculate the amount that the advertised capacity lies
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':  #Expressions that are evaluated to true or false are called conditions
    discrepancy = 1000000000 / 1073741824
else:
    print('You must enter GB or TB')
    sys.exit()
print('Enter the advertised capacity: ')
advertisedCapacity = input('>')
advertisedCapacity = float(advertisedCapacity)

#Calculate the real capacity, round it to the nearest hundreth
#Then convert it into a string so we can concatenate it

realCapacity = str(round(advertisedCapacity * discrepancy, 2))

print('The advertised capacity is: ' + str(advertisedCapacity) + str(unit) + ' whilst the real one would be ' + realCapacity + str(unit))
