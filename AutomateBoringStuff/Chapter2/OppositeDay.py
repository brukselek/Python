isOppositeDayToday = True

if isOppositeDayToday:
    sayItsOppositeDay = True
else:
    sayItsOppositeDay = False

#If it is Opposite day toggle sayItsOppositeDay
if isOppositeDayToday:
    sayItsOppositeDay = not sayItsOppositeDay

if sayItsOppositeDay:
    print('Today is opposite day')
else:
    print('Today is not opposite day')
