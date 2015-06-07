# BEFORE YOU START:

# This program only works with input files in ansi type of ASCII (.asc), without indicating the time (this will be done manually)




import sys
import math
# from __future__ import division, print_function, absolute_import

try:
	sys.argv[1]
except:
	print '\n' + 'REMEMBER TO CHOOSE THE FILE TO ANALYSE IN THE TERMINAL!!!' + '\n'


raw = open(sys.argv[1], "r").readlines()
out = open(str(sys.argv[1])[:-4] + "cleanplate.csv", "w") #This keeps the same name as the input file + "cleaplate" and gives the format .tsv


# The program will ask for the volume in the console
volume = raw_input('\n'+'Please introduce the volume in the wells (in microlitres)'+'\n') #to select the volume in each well, Lambert-Beer Law takes into account the pathlenght, and pathlength is determined by the volume in each well. 
volume = float(volume)


# The program will ask for the duration of the kynetic cycle in the console
intervals = raw_input('\n'+'Please introduce duration of the cycles (in minutes)'+'\n') # The time between measurements (in minutes) 
intervals = float(intervals)

time = 0

# Imports pi from library math
pie = math.pi

# Calculate the ratio you have to multiply the Absorbance by to obtain the equivalent OD in 1 cm pathlength. 
ratio = 10/((float(volume)*4)/(11*11*pie))

# Prints header for each column
out.write('Time (min)' + ';' + 'A1' + ';' + 'A2' + ';' + 'A3' + ';' + 'A4' + ';' + 'A5' + ';' + 'A6' + ';' + 'A7' + ';' + 'A8' \
	+ ';' + 'B1' + ';' + 'B2' + ';' + 'B3' + ';' + 'B4' + ';' + 'B5' + ';' + 'B6' + ';' + 'B7' + ';' + 'B8' +\
	';' + 'C1' + ';' + 'C2' + ';' + 'C3' + ';' + 'C4' + ';' + 'C5' + ';' + 'C6' + ';' + 'C7' + ';' + 'C8' + \
	';' + 'D1' + ';' + 'D2' + ';' + 'D3' + ';' + 'D4' +  ';' + 'D5' + ';' + 'D6' + ';' + 'D7' + ';' + 'D8' + \
	 ';' + 'E1' + ';' + 'E2' + ';' + 'E3' + ';' + 'E4' + ';' + 'E5' + ';' + 'E6' + ';' + 'E7' + ';' + 'E8' +\
	 ';' + 'F1' + ';' + 'F2' + ';' + 'F3' + ';' + 'F4' + ';' + 'F5' + ';' + 'F6' + ';' + 'F7' + ';' + 'F8' + '\n')

# For each moment, it creates a list with the Absorvance values in each well
for moment in raw:
	correctedlist = []
	measurements = moment.strip().split()

	# For each Absorbance, it corrects with the ratio and creates a new list with the corrected values. 
	for element in measurements:

		correctedelement = float(element) * ratio
		correctedlist.append(correctedelement)

	# Writes time and the corrected values in a format that excel understand (apparently, points are not good for decimals in .tsv)
	out.write(str("{0:.15f}".format(round(time,15)).replace('.', ',') + ';' ))
	for correctedelement in correctedlist:
		out.write(str("{0:.15f}".format(round(correctedelement,15)).replace('.', ',') + ';')) 
		# rouds the float to 15 decimals, converts it to a string, replaces points to commas (excel requires it for tsv) and writes it in the file. 
	out.write('\n')
	time = time + intervals # increases the time for the next set of values. 
	
