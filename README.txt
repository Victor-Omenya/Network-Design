# Phase 2 README.md

## Group 6 Members:
Victor  
Samonorom  
Adarsh  
Nishchay  

## Environment:  
Operating Systems : Mac / Windows 11
Programming Language : Python
Version : Python 3

## Files:'
I.    DesignFiles-Screenshots - this folder contains screenshots of the different stages of phase 2.
II.   DesignFile.md - this is the design file that explains what all the python files do.
III.  DesignFile.docx - this is the word document version of the DesignFile.md.
IV.   README.md - a brief overview of what this phase is about.
V.    README.txt - the ReadMe file containing the group members, environment, file list and instructions about phase 2. 
VI.   bubbles.jpg - one of the files to be transfered from the client to the server.
VII.  received_image.jpg - the transmitted file in server from the client.
VIII. clientUDP.py - the client python code. 
IX.   serverUDP.py - the server python code.

## Instructions:  
I.    Following the link ( https://github.com/Victor-Omenya/Network-Design.git ) to the github repository, download the zip file. 
II.   Open pycharm or any IDE that can open or run any python code.
III.  Open the serverUDP.py file and run it. A message in the commandline section will pop up stating that the "Server is ready to receive the image".
IV.   Open the clientUDP.py file and check line #23. Make sure that the name matches any of the .jpg files in the zip file. If they match, run the clientUDP.py code.
V.    Note the messages provided in the commandline section of the IDE which would show this message "A chunk of the image was received as a packet" each time a packet was received by the server.
VI.  Once the transmission is done, open the file named received_image.jpg to view the transmitted file. Open the original jpg file to compare to see whether there were any lost packets.

Note: All the files should be in the same folder.
