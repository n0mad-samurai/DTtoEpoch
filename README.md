# contime

usage: contime.py [-h] [-e EPOCH] [-t DATETIME [DATETIME ...]]

This is a date time converter that handles
Unix epoch or iOS Absolute Time formats.

Provide your UTC date and time with decimal seconds(up to 6 digits) using this format:
2014-01-26 23:44:15.0 year-month-day hours:minutes:seconds.000000 or,
UTC epoch milliseconds (13 digits!) as: 1390779855380 or,
iOS Absolute Time (14 digits) as: 402373726.55571. 
Default is Unix epoch conversion. 
TimeType option 'i' is iOS Absolute Time conversion.

options:

  -h, --help show this help message and exit

  -ep EPOCH, --epoch EPOCH, convert Unix EPOCH milliseconds to date-time format

  -dt DATETIME [DATETIME ...], --DateTime DATETIME [DATETIME ...], convert DATETIME with decimal seconds to Unix epoch format
  
  --tt TIMETYPE, --TimeType TIMETYPE, u = Unix epoch conversion, i = iOS Absolute Time conversion

You can use both options, -ep and -dt, in one process


Use the website:
https://currentmillis.com/
to confirm results.
