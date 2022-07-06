# importing modules - matplotlib to draw grid, os.path to determine whether route file exists

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import os.path

pos = []


def main(file):
	
	with open(file, 'r') as f:
		
		#take lines from route files, remove \n from each
		lines = f.readlines()
	
		lines = [x.strip() for x in lines]

		#if the function has already run through another route file, the pos coordinates
		#list will not be empty, so the following will run to the else statement. If the
		#route file is the first being run, it'll take the first two lines of the Route
		#file and append them to the coordinates list, as well as initialising the pos1
		#current position variable.

		if len(pos) == 0:
			start = [int(lines[0]), int(lines[1])]
			pos.append(start[:])
			pos1 = start[:]
		else:
			pos1 = pos[-1][:]
			print("Last position: {}".format(pos1))

		#This loop runs over the instructions in the route file, and so long as the current
		#position is within the grid, it will adjust the rolling position accordingly and 
		#append it to the list of coordinates.

		for i in range(2, len(lines)):
			if 0 < pos1[0] <= 12 and 0 < pos1[1] <= 12:
				if lines[i] == 'N':
					pos1[1] += 1
					pos.append(pos1[:])
				elif lines[i] == 'E':
					pos1[0] += 1
					pos.append(pos1[:])
				elif lines[i] == 'S':
					pos1[1] -= 1
					pos.append(pos1[:])
				elif lines[i] == 'W':
					pos1[0] -= 1
					pos.append(pos1[:])
				else:
					print("Error: Route file contains an uninterpretable instruction.")
			else:
				print("Error: The route is outside of the grid.")
				break

		#matplotlib takes a list of positions and a list of 'codes' consisting of a
		#'Path.MOVETO' for the first coordinate, then a 'Path.LINETO' for each
		#subsequent element.

		verts = pos[:]

		codes = [Path.MOVETO]

		for i in range(len(verts)-1):
   			codes.append(Path.LINETO)

		path = Path(verts, codes)

		fig, ax = plt.subplots()
		patch = patches.PathPatch(path, facecolor='1', lw=10)
		ax.add_patch(patch)
		ax.set_xlim(1, 12)
		ax.set_ylim(1, 12)
		ax.set_xticks(range(1,13))
		ax.set_yticks(range(1,13))
		ax.yaxis.grid(True)
		ax.xaxis.grid(True)

		#block=False is necessary to allow the code to continue running after opening
		#the grid window.

		plt.show(block=False)

		#producing formatted list of coordinates from pos list.

		gen = '\n'

		for i in range(len(pos)):
			gen += '(' + str(pos[i][0]) + ', ' + str(pos[i][1]) + ')\n'

		print("Coordinates: {}".format(gen))



while True:
	filename = input("type filename here: ")
	
	#checking if file exists in directory. If not returns to input.

	if os.path.isfile(filename):
		break
	else:
		print('File not found')

#running main function

main(filename)


while True:

	#running main function with any subsequent route file, including conditional
	#statement to allow 'STOP' to end program.
	
	filename = input("Enter the next route instructions file, or enter STOP to finish: ")

	if filename == 'STOP':
		break
	elif os.path.isfile(filename):
		main(filename)
	else:
		print('File not found')



