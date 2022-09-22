# harmonica
Tool to easily shift an harmonica tab to another key

**Documentation used**
- Tab rulers: https://www.harptabs.com/displayfile.php?ID=31 
- Shift logic: https://qr.ae/pvWj1O


**Prerequisites**
- Python version used: 3.7.3
- The Melody Tab

**Considerations**
- The author doesn't have any musical background, take this with a grain of salt.

- You need to have sample.py and transposing_keys.py in the same folder.

- This tool only work for diatonic harmonicas. 

- Feel free to improve it to add other features, like chromatic harmonicas.

- If a note go out of range for the new key a warning will appear: "key out of range, tab_pos note"
 and the note will be omited from the clean tab.


**How to use**
- Go to sample.py and edit source_key, target_key and melody with your tab key and notes.
- Run sample.py (I recommend echoing to a file in order to easily save the result)

**Result example*
#####
Transposing slide, theory:
G key: ['G', 'A', 'B', 'C', 'D', 'E', 'F']
C key: ['C', 'D', 'E', 'F', 'G', 'A', 'B']
slide: C+3 = G
G key: [1, -1, 2, -2, 3, -3, -3]
C key: [-2, -4, -1, -5, 1, -6, -6]
#####


Previous Tab.
Key: G 

-8 8 8 -9 8
-9 -8 7 -7 7
-8 -8 -8 7 -7
7 -7 -6 
-----
Transposing melody ...
key out of range, tab_pos 1 note -8
key out of range, tab_pos 4 note -9
key out of range, tab_pos 6 note -9
key out of range, tab_pos 7 note -8
key out of range, tab_pos 9 note -7
key out of range, tab_pos 11 note -8
key out of range, tab_pos 12 note -8
key out of range, tab_pos 13 note -8
key out of range, tab_pos 15 note -7
key out of range, tab_pos 17 note -7
Melody transposed. 

New Clean Tab.
Key: C 

4 4 4 3 3
3 3 -10 
-----

**Author**

 - Bunkai

**License**

 - Creative Commons Zero v1.0 Universal

 - All the code and builds are free to use, modify and distribute.

