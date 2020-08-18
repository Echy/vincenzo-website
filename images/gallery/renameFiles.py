import os
import glob
import re

# Function to rename multiple files 
def main(): 
	index = 0
	toChange = []
	usedNumbers = []
	
	# checks if any file needs to be renamed 
	for filename in glob.glob("*.jpg"):
		if not re.search('^gallery_([0-9]{1,2})\.jpg$', filename):
			toChange.append(filename)
			print(" + " + filename + " needs to be renamed")
		else :
			# fills in used numbers
			usedNumbers.append(filename[8:-4])

	# exits if no change
	if not toChange:
		print("Nothing to change")
		return 0

	# now we rename what needs to be renamed
	for previousName in toChange :
		while str(index) in usedNumbers :
			print("Already used : ", index)
			index += 1

		newName = "gallery_" + str(index) + ".jpg"
		os.rename(previousName, newName)
		print(" >>> " + previousName + " renamed to " + newName)
		index += 1
	return 0

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
