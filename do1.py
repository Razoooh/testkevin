#!/usr/bin/python
import os
import sys

# Global variables

g_exampleVariable = "Global Example Variable"  # Only, if this is necessary

def showUsageInformation():
	print() 
	print("Skeleton Script Python is the base for making new scripts in Python.")
	print("The user has to type here what the Python script can perform and does.")
	print() 
	print("Way of usage:")
	print() 
	print("The user has to type here how he has to work with the Python script.")
	print()
	print("Example:") 
	print()
	print("python SkeletonScriptPython.py")
	print()
	sys.exit()

def showfiles(file):
        nextline = ""
        nuclist = []
        scorelist = []
        namelist = []
        lengte = 0
        for lines in file:
                lines = lines.rstrip()
                if nextline == "score":
                        scorelist.append(lines)
                        nextline = ""
                        
                if nextline == "":
                        if lines.startswith("+"):
                                nextline = "score"
                                
                if nextline == "nuc":
                        nuclist.append(lines)
                        lengte = lengte + len(lines)
                        nextline = ""
                        
                if nextline == "":
                        if lines.startswith("@"):
                                nextline = "nuc"
                                namelist.append(lines)

        print(len(namelist))
        print(len(max(nuclist, key=len)))
        print(len(min(nuclist, key=len)))
        print(lengte/len(nuclist))
        print(scorelist[5])
def openfiles(lijn):

        lines = open(lijn).read().split('\n')

        return lines

def closefiles(sluit):

        sluit.close()

def main(argv):
	if len(argv) >= 2:
		if argv[1] == "-h" or argv[1] == "--h" or argv[1] == "-help" or argv[1] == "--help":
			showUsageInformation()
	
	lijn1 = openfiles('s_2_1_sequence.txt')
	showfiles(lijn1)
	#closefiles(lijn1)
	lijn2 = openfiles('s_2_2_sequence.txt')
	showfiles(lijn2)
        
                                 
if __name__ == "__main__":
	main(sys.argv)
	

# Additional information:
# =======================
#
# Remarks about the Skeleton Script Python itself.
# Description how it works.
# Description which improvements can be done to improve the Skeleton Script Python itself.
#

