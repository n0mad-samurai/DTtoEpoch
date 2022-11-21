# contime

This a the Unix epoch to date time
or date time to Unix epoch converter.

Provide your UTC date and time with decimal seconds(up to 6 digits)
using this format: 2014-01-26 23:44:15.0
year-month-day hours:minutes:seconds.000000
or epoch milliseconds (13 digits!) as: 1390779855380

This is useful when searching
through database fields that
use the epoch timestamp

Use the website:
https://currentmillis.com/
to confirm results.

usage: contime.py [-h] [-e EPOCH] [-t DATETIME [DATETIME ...]]

This a the Unix epoch to date time or date time to Unix epoch converter. Provide your UTC date and time with
decimal seconds(up to 6 digits) using this format: 2014-01-26 23:44:15.0 year-month-day
hours:minutes:seconds.000000 or epoch milliseconds (13 digits!) as: 1390779855380

options:
  -h, --help            show this help message and exit
  -e EPOCH, --epoch EPOCH
                        option: convert Unix epoch milliseconds to date-time format
  -t DATETIME [DATETIME ...], --DateTime DATETIME [DATETIME ...]
                        option: convert date-time with decimal seconds to Unix epoch format

You can use both options, -e and -t, in one process
