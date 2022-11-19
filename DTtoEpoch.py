'''
DTtoEpoch.py
Bobby Price
n0mad-samurai
'''
'''
Convert a date-time to
Epoch milliseconds.

This is useful when searching
through database fields that
use the Epoch timestamp such
as Facebook threads_db2
'''
'''
Use the website:
https://currentmillis.com/
to confirm results.

This UTC date-time:
2014-01-26 23:44:15
converts to 1390779855000.0
but 1390779855380 is the same
date-time.'''
'''
Python 3.x
'''
# import methods from library
from datetime import datetime, timezone
import sys

# display instructions
print('This is the Date-Time to Epoch millisecond converter.')
print('Provide your date and time in UTC')
print('using this format: 2014-01-26 23:44:15')

# assign input to object
yourDateTime = (input('Enter your UTC date-time:\n'))

# strip data from user input
# assign data to another object
# catch errors with input
try:
    timeData = datetime.strptime(yourDateTime, '%Y-%m-%d %H:%M:%S')
except Exception as err:
    sys.exit('There is an error with your input -\n ' + str(err))

# display the results
# replace object date-time with Epoch in milliseconds
print('\nYour date-time input was:', yourDateTime, 'UTC')
# ensure the timezone is UTC for the Epoch display
print('The Unix Epoch is:', timeData.replace(tzinfo=timezone.utc).timestamp() * 1000)

