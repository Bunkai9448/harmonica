# file: sample
# Python version used: 3.7.3
# author : Bunkai
# Version: 0.01
# Date: 

"""
	Transposing_keys, example of use.
	
	The following rulers were used as a reference for the tool test :
	https://www.harptabs.com/displayfile.php?ID=31
	The following tab was used as a reference for the tool test :	
	https://www.harptabs.com/song.php?ID=15847

"""

from transposing_keys import *

# Input Data
source_key = 'G'
target_key = 'C'
newTab =[]
melody = [8, -8, 7, -8, 8, 8, 8, -8, 7, -8, 8, 8, 
	-9, 8, -9,-8, 7, -7, 7, -8, -8, -8, 7, -7, 8, 
	-9, 8, -8, 7, -7, 7, -8, 8, 8, -8, 7, -8, 8, 
	8, 8, -8, 7, -8, 8, 8, -9, 8, -9,-8, 7, -7, 7, 
	-8, -8, -8, 7, -7, 7, -7, -6]

print('Previous Tab.')
print('Key:',source_key,"\n")
clean_Display(melody) 

# Using the function to obtain the new tab printed on screen
transpose_Melody(melody,newTab,source_key,target_key)

# Making the tab easy to read (with line breaks)
print('New Clean Tab.')
print('Key:',target_key,"\n")
clean_Display(newTab)