Title:        Piano Compositions Playback Studio
Author:       Morag Brown

Institution:  University of Cape Town

Description:  This program plays piano notes according to the data held within
              a text file. The notes were recorded from a Steinway Model D piano
              and saved as .wav files.
              
              The convention adopted in the text file for each note is:
              note_noteDuration_timeUntilNextNote_noteVolume -> with each note's data on a new line.
              For example: a4_2000_0.5_1 -> play note A4 for 2 seconds at 100% volume, play the next 
					    note in the list after 0.5 seconds
	      Note: 'noteDuration' must be in milliseconds and 'timeUntilNextNote' must be in seconds
              
              This program employs a similar method to MIDI messages.
              MIDI messages contain "note on", "note off" and volume data

Requirements: A Python IDE
	      The latest Python V3, Tkinter and Pygame modules

How to use:   >Run the PiComPS.py file
              >Left click on the START button
              >When prompted, select the text file you wish to play*
              >The selected text file should load and
               the correct notes should play
              >The current note being played will print on the shell
               behind the PiComPS UI

              *Text files will only play if they contain
              data conforming to the convention shown above
		
	      Note: occasionally notes play slightly out of time, especially if the music is played right
	            after the studio is opened