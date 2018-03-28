"""	
	Main Function:  get_location(gps_uart)
	Returned value: "<utc_time>, <latitude>, <longitude>, <num_satellites>, <altitude>, <heading>, <speed>"
	
	Note: GPS pins depend on the UART initialization in the calling function.
	Reference: https://cdn-learn.adafruit.com/downloads/pdf/adafruit-ultimate-gps.pdf
"""
from pyb import *

def get_location(gps_uart):
	"""This function retrieves, parses and returns all appropriate data"""
	## PARSING GPGGA OPTION
	gpgga_raw_data = get_option_data(gps_uart, "GPGGA")
	gpgga_data_list = gpgga_raw_data.split(",")
	# UTC Time
	utc_time = gpgga_data_list[1]
	utc_time = utc_time[0:2] + ":" + utc_time[2:4] + ":" + utc_time[4:6]
	# Position Indicator
	pos_indictor = gpgga_data_list[6] # 0->No fix, 1->GPS fix, 2->Differential GPS fix
	if(int(pos_indictor) == 0):
		return utc_time + ", No Fix" #NOTE: UNCOMMENT LINES
	# Coordinates
	latitude  = gpgga_data_list[2] + gpgga_data_list[3]
	seconds = (float(latitude[4:-1]) * 60) // 1
	latitude  = latitude[0:2] + "°" + latitude[2:4] + "'" + str(seconds) + '"' + latitude[-1:]
	longitude = gpgga_data_list[4] + gpgga_data_list[5]
	seconds = (float(longitude[5:-1]) * 60) // 1
	longitude = longitude[0:3] + "°" + longitude[3:5] + "'" + str(seconds) + '"' + longitude[-1:]
	# Number of Satellites and Altitude
	num_satellites = gpgga_data_list[7]
	altitude = gpgga_data_list[9] # meters
	# send_data = ",".join([utc_time, latitude, longitude, num_satellites, altitude]) #NOTE: UNCOMMENT WHEN TESTING GPGGA ONLY
	
	## PARSING GPVTG OPTION
	gpvtg_raw_data = get_option_data(gps_uart, "GPVTG") 
	gpvtg_data_list = gpvtg_raw_data.split(",")
	# Measured Heading and Horizontal Speed
	heading = gpvtg_data_list[1]
	speed = gpvtg_data_list[7] # kmph

	send_data = ", ".join([utc_time, latitude, longitude, num_satellites, altitude, heading, speed]) #NOTE: DO SOMETHING
	return send_data

def get_option_data(gps_uart, option):
	"""This function retrieves raw data of a particular option from the GPS and returns it"""
	while True:
		if(gps_uart.any() > 0 and gps_uart.read(1) == b'$'):
			delay(200)
			# print(str(gps_uart.read(5))[2:-1])
			if(str(gps_uart.read(5))[2:-1] == option):
				test_data_raw = str(gps_uart.read(66))[2:-1] # option has max of 66 characters
				return test_data_raw
