# file: transposing_keys
# Python version used: 3.7.3
# author : Bunkai
# Version: 0.01
# Date: 

"""
	The goal of this file is to convert any harmonica tab between different keys.
	In the desire of people being able to make use of any prior written tab instead
	of having to go hunting one written for their key.

 	This will help you to easily translate the tabs from one key to another.
	Keep in mind that the above is a basic method and the final result may not be 100% accurate.
	It's always best to check the final tab
"""

print()
print('#####')
print('Transposing slide, theory:')
# You can see the Tab rulers here https://www.harptabs.com/displayfile.php?ID=31
# Following this logic https://qr.ae/pvWj1O

# If we write both base scales in a list,
G_key_Ltr = ['G','A','B','C','D','E','F'] 
C_key_Ltr = ['C','D','E','F','G','A','B']

print('G key:', G_key_Ltr)
print('C key:', C_key_Ltr)

# We can see the interval that we need to adjust (G-3 = C) -> slide = 3
print('slide: C+3 = G')
#Therefore if we do the addition to the tab numbers:
G_key_num = [1,-1,2,-2,3,-3,-3]
C_key_num = []

slide = -3	# adjust to be made
	
# Fill the new key (Rewrite the key to the new one)
for i in range(0,len(G_key_num)):

	noteToTab = 0
	# Do the slide shift from each number in the tab
	noteToTab = G_key_num[i]+slide
	# If the number is 0 or below, adjust; add 10
	if noteToTab <= 0:
		noteToTab += 10
	# If the number is above 10, adjust; delete the slide subtract 10
	elif noteToTab > 10:
		noteToTab -= 10

	C_key_num.append(noteToTab)
	i += 1	
	
print('G key:', G_key_num)
print('C key:', C_key_num)
print('#####')

print()


def transpose_Melody(melody,newTab,source_key,target_key):
	print('Transposing melody ...')
	slide = ord(target_key) - ord(source_key)	# adjust to be made
	
	# adjustment
	for i in range(0,len(melody)):
		noteToTab = 0
		# Do the slide shift from each number in the tab
		noteToTab = melody[i]+slide
		# If the number is 0 or below, add 10
		if noteToTab <= 0:
			noteToTab += (10+slide)
		# If the number is above 10, subtract 10
		elif noteToTab > 10:
			noteToTab -= 10

		newTab.append(noteToTab)
		i += 1	
	print('Melody transposed.', "\n")

# Display the new tab in a nice way (with break lines):
def clean_Display(tab):

	y = 1
	for x in range(0,len(tab)):
		if y < 5:
			print(tab[x], end=' ')
			y += 1
		else:
			print(tab[x])
			y = 1

	print()
	print('-----')

print()
