#! python3
#bulletpointadder.py - adds wikipedia bullet points to the start
#of each line of the text on the clipboard.

import pyperclip
text = pyperclip.paste()

#TODO: seperate lined and add stars.

#seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):   #loop through all indexes in the "lines" list
 lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines) 
pyperclip.copy(text)
print(pyperclip.paste())
