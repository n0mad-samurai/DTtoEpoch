'''
contime.py v0.20
Bobby Price
n0mad-samurai
'''
'''
Convert date time to and from
Unix epoch or iOS Absolute Time.

This is useful when searching
through database fields that
use integer or decimal timestamps.

Use the website:
https://currentmillis.com/
to confirm results.
'''
'''
Python 3.x
'''
# import methods from libraries
from datetime import datetime, timezone
import sys
import argparse

VERSION = 'v0.20 November 2022'

EPOCHIOSDIFF = 978307200

INSTRUCTIONS = '''
This is a date time converter that handles
Unix epoch or iOS Absolute Time formats.
Provide your UTC date and time with decimal seconds(up to 6 digits)
using this format: 2014-01-26 23:44:15.0
year-month-day hours:minutes:seconds.000000 or,
UTC epoch milliseconds (13 digits!) as: 1390779855380 or,
iOS Absolute Time (14 digits) as: 402373726.55571. 
Default is Unix epoch conversion. 
TimeType option 'i' is iOS Absolute Time conversion.
'''

# define the cli method

# create an object to capture cli argument definitions
parser = argparse.ArgumentParser(description=INSTRUCTIONS, epilog='You can use both options, -e and -t, in one process')

# cli arguments for verbose option, directory to search, save csv results, save tablular results
parser.add_argument('-ep', '--epoch', type=float, help="option: convert UTC Unix epoch milliseconds to UTC date-time format")
parser.add_argument('-dt', '--DateTime', type=str, nargs=2, help="option: convert UTC date-time with decimal seconds to UTC Unix epoch format")
parser.add_argument('-tt', '--TimeType', type=str, help="option: u = Unix epoch conversion, i = iOS Absolute Time conversion")

# assign selected arguments to an object list
args = parser.parse_args()

# check args list for options
# assign boolean results
if args.epoch:
    EPOCH = True
else:
    EPOCH = False

if args.DateTime:
    DT = True
else:
    DT = False
    
if args.TimeType:
    TYPE = True
else:
    TYPE = False
    
if DT is False and EPOCH is False:
    print('Use option -e or -t, or both. Option -h for help.')
    
if TYPE is False or args.TimeType == 'u':
    
    if EPOCH:
    
        # test user input
        # catch errors
        try:
            etMilli = args.epoch / 1000
            # display results
            print('Converted UTC epoch', args.epoch,'to UTC date time', datetime.utcfromtimestamp(etMilli).strftime('%Y-%m-%d %H:%M:%S.%f'))
        except Exception as err:
            sys.exit('There is an error with your input -\n ' + str(err))
            
    if DT:
        
        # strip data from user input
        # assign data to another object
        # catch errors        
        try:
            dt = ' '.join(args.DateTime)
            timeData = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
            # display the results
            print('Converted UTC date time', dt,'to UTC epoch', int(timeData.replace(tzinfo=timezone.utc).timestamp() * 1000))        
        except Exception as err:
            sys.exit('There is an error with your input -\n ' + str(err))        

if TYPE:
    
    if args.TimeType == 'i':
        
        if EPOCH:
            
            # iOS Absolute Time to Date Time conversion
            try:
                myEpoch = args.epoch + EPOCHIOSDIFF
                # display results
                print('Converted iOS Absolute Time', args.epoch,'to UTC date time', datetime.utcfromtimestamp(myEpoch).strftime('%Y-%m-%d %H:%M:%S.%f'))
            except Exception as err:
                sys.exit('There is an error with your input -\n ' + str(err))
                
        if DT:
           
            # strip data from user input
            # assign data to another object
            # catch errors        
            try:
                dt = ' '.join(args.DateTime)
                timeData = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
                # display the results
                print('Converted UTC date time', dt,'to iOS Absolute Time', (timeData.replace(tzinfo=timezone.utc).timestamp() - EPOCHIOSDIFF))        
            except Exception as err:
                sys.exit('There is an error with your input -\n ' + str(err))        
        

# alternate formula for epoch to date-time
# print('Converted date time', dt,'to epoch', int((timeData - datetime(1970, 1, 1)).total_seconds() * 1000))
# iOS epoch
# print ('Converted date time', dt, 'to iOS Absolute Time', int((timeData - datetime(2001, 1, 1)).total_seconds()))
# iOS Unix epoch differential is 978307200 seconds
# EPOCHIOSDIFF = 978307200
# myEpoch = args.epoch + EPOCHIOSDIFF
# print('Converted iOS Absolute Time', args.epoch,'to UTC date time', datetime.utcfromtimestamp(myEpoch).strftime('%Y-%m-%d %H:%M:%S.%f'))
