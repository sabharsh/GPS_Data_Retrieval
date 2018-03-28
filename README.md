# GPS_Data_Retrieval

## Description

The purpose of this module is to retrieve, parse and format datafeed of a GPS sensor using  Pyboard. It was created to write the formatted data to a file and thus the primary function returns a formatted string. The data sheet used to parse the datafeed is:

https://cdn-learn.adafruit.com/downloads/pdf/adafruit-ultimate-gps.pdf

## Functions

 get_location(gps_uart) - This function retrieves, parses and returns all required data. The only argumnet needed is the uart bus which must be initialized in the calling function. The rrturned value is "<utc_time>, <latitude>, <longitude>, <num_satellites>, <altitude>, <heading>, <speed>".
 
 get_option_data(gps_uart, option) - This function retrieves raw data of a particular option from the GPS. Refer to the reference above for learn about the options. The returned value is "<raw_data>".
 
 
 

