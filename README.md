# DTtoEpoch

Python script to convert a date-time to Unix Epoch in milliseconds.

This is useful when searching through database fields that use the Epoch timestamp and your database browser does not convert
the timestamp.

Provide your date and time in UTC using this numerical format: 2014-01-26 23:44:15 - year-month-day hours:minutes:seconds (24 hour format)

Use the website: https://currentmillis.com/ to confirm results.

Note: This UTC date-time: 2014-01-26 23:44:15 converts to 1390779855000.0 but 1390779855380 is the same date-time.

I may improve this by adding an option to convert either way, date-time to Epoch or Epoch to date-time.
