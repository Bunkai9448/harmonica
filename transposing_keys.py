# file: transposing_keys
# Python version used: 3.7.3
# author : Bunkai
# Version: 0.01
# Date: 

"""
	The goal of this file is to convert any harmonica tab between different keys.
	In the desire of people being able to make use of any prior written tab instead
	of having to go hunting one written for their key.
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
	
# adjustment
for i in range(0,len(G_key_num)):
	if G_key_num[i] < 0 and (slide < 0) and (G_key_num[i]-abs(slide) < -10) :
		print('key out of range, tab_pos',i+1, 'note', G_key_num[i])
		
	elif G_key_num[i] > 0 and (slide > 0) and  (G_key_num[i]+abs(slide) > 10) :
		print('key out of range, tab_pos',i+1, 'note', G_key_num[i])
	
	elif (G_key_num[i]+slide) == 0: 
		C_key_num.append(1)
	else:
		C_key_num.append(G_key_num[i]+slide)
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
		if melody[i] < 0 and (slide < 0) and (melody[i]-abs(slide) < -10) :
			print('key out of range, tab_pos',i+1, 'note', melody[i])
		
		elif melody[i] > 0 and (slide > 0) and  (melody[i]+abs(slide) > 10) :
			print('key out of range, tab_pos',i+1, 'note', melody[i])
	
		elif (melody[i]+slide) == 0: 
			newTab.append(1)
		else:
			newTab.append(melody[i]+slide)
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
