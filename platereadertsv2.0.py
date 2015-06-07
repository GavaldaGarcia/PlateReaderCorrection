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
out = open(str(sys.argv[1])[:-4] + "cleanplate.tsv", "w") #This keeps the same name as the input file + "cleaplate" and gives the format .tsv


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
out.write('Time (min)' + '\t' + 'A1' + '\t' + 'A2' + '\t' + 'A3' + '\t' + 'A4' + '\t' + 'A5' + '\t' + 'A6' + '\t' + 'A7' + '\t' + 'A8' \
	+ '\t' + 'B1' + '\t' + 'B2' + '\t' + 'B3' + '\t' + 'B4' + '\t' + 'B5' + '\t' + 'B6' + '\t' + 'B7' + '\t' + 'B8' +\
	'\t' + 'C1' + '\t' + 'C2' + '\t' + 'C3' + '\t' + 'C4' + '\t' + 'C5' + '\t' + 'C6' + '\t' + 'C7' + '\t' + 'C8' + \
	'\t' + 'D1' + '\t' + 'D2' + '\t' + 'D3' + '\t' + 'D4' +  '\t' + 'D5' + '\t' + 'D6' + '\t' + 'D7' + '\t' + 'D8' + \
	 '\t' + 'E1' + '\t' + 'E2' + '\t' + 'E3' + '\t' + 'E4' + '\t' + 'E5' + '\t' + 'E6' + '\t' + 'E7' + '\t' + 'E8' +\
	 '\t' + 'F1' + '\t' + 'F2' + '\t' + 'F3' + '\t' + 'F4' + '\t' + 'F5' + '\t' + 'F6' + '\t' + 'F7' + '\t' + 'F8' + '\n')

# For each moment, it creates a list with the Absorvance values in each well
for moment in raw:
	correctedlist = []
	measurements = moment.strip().split()

	# For each Absorbance, it corrects with the ratio and creates a new list with the corrected values. 
	for element in measurements:

		correctedelement = float(element) * ratio
		correctedlist.append(correctedelement)

	# Writes time and the corrected values in a format that excel understand (apparently, points are not good for decimals in .tsv)
	out.write(str("{0:.15f}".format(round(time,15)).replace('.', ',') + '\t' ))
	for correctedelement in correctedlist:
		out.write(str("{0:.15f}".format(round(correctedelement,15)).replace('.', ',') + '\t')) 
		# rouds the float to 15 decimals, converts it to a string, replaces points to commas (excel requires it for tsv) and writes it in the file. 
	out.write('\n')
	time = time + intervals # increases the time for the next set of values. 
	
