'''
Title:        Piano Compositions Playback Studio
Author:       Morag Brown

Institution:  University of Cape Town

Description:  This program plays piano notes according to the data held within
              a text file. The notes were recorded from a Steinway Model D piano
              and saved as .wav files.
              
              The convention adopted in the text file for each note is:
                          note_noteDuration_timeUntilNextNote_noteVolume
                          
              For example: a4_2000_0.5_1 -> play note A4 for 2 seconds at 100% volume, play the next 
					    note in the list 0.5 seconds after starting the current note
	      Note: 'noteDuration' must be in milliseconds and 'timeUntilNextNote' must be in seconds
                    The data for each new note must be on a new line
                    
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
'''

#================================Imports=====================================
from tkinter import *
from tkinter.filedialog import askopenfilename
import pygame
import time
import random

#=============================Initialisation=================================
pygame.mixer.init()

#Create root widget and set up layout
root = Tk()
root.title("Piano Composition Playback Studio")
root.configure(background='white')

mainFrame = Frame(root, bg = '#202020', borderwidth=4, relief = "groove")
mainFrame.grid()
c1Frame = Frame(mainFrame, bg = '#202020', borderwidth=4, relief = "groove")
c1Frame.grid()
c2Frame = Frame(mainFrame, bg = '#3c3c3c',padx=8, pady=30, borderwidth=4, relief = "groove")
c2Frame.grid()

#============================Labels & Displays===============================
#Create labels to show information
Label(c1Frame, text = "Piano Composition Playback Studio",
      font = ('open sans', 25),
      padx=8, pady=2,bd = 5,
      bg="#202020", fg="white",
      justify=CENTER).grid(row=0, column=0, columnspan=11)

Label(c1Frame, text = "Steinway Model D",
      font = ('open sans', 12),
      padx=8, pady=2,
      bg="#202020", fg="white",
      justify=CENTER).grid(row=1, column=0)

Label(c1Frame, text = "By Morag Brown",
      font = ('open sans', 12),
      padx=8, pady=4,
      bg="#202020", fg="white",
      justify=RIGHT).grid(row=1, column=10)

#Create entry that displays the file currently being played
action_String = StringVar()
#action_String.set("Action Display")
action_Display = Entry(c2Frame, textvariable = action_String,
                       width = 35, justify = 'center',
                       font = ('open sans', 15),
                       bd = 4, bg="#3c3c3c",fg="white")
action_Display.grid(row = 0, column = 1)

#=================================Samples====================================
#Create a Sound from the audio sample

a0Note  = pygame.mixer.Sound(r"Samples\A0.wav")
as0Note = pygame.mixer.Sound(r"Samples\A#0.wav")
b0Note  = pygame.mixer.Sound(r"Samples\B0.wav")

c1Note  = pygame.mixer.Sound(r"Samples\C1.wav")
cs1Note = pygame.mixer.Sound(r"Samples\C#1.wav")
d1Note  = pygame.mixer.Sound(r"Samples\D1.wav")
ds1Note = pygame.mixer.Sound(r"Samples\D#1.wav")
e1Note  = pygame.mixer.Sound(r"Samples\E1.wav")
f1Note  = pygame.mixer.Sound(r"Samples\F1.wav")
fs1Note = pygame.mixer.Sound(r"Samples\F#1.wav")
g1Note  = pygame.mixer.Sound(r"Samples\G1.wav")
gs1Note = pygame.mixer.Sound(r"Samples\G#1.wav")
a1Note  = pygame.mixer.Sound(r"Samples\A1.wav")
as1Note = pygame.mixer.Sound(r"Samples\A#1.wav")
b1Note  = pygame.mixer.Sound(r"Samples\B1.wav")

c2Note  = pygame.mixer.Sound(r"Samples\C2.wav")
cs2Note = pygame.mixer.Sound(r"Samples\C#2.wav")
d2Note  = pygame.mixer.Sound(r"Samples\D2.wav")
ds2Note = pygame.mixer.Sound(r"Samples\D#2.wav")
e2Note  = pygame.mixer.Sound(r"Samples\E2.wav")
f2Note  = pygame.mixer.Sound(r"Samples\F2.wav")
fs2Note = pygame.mixer.Sound(r"Samples\F#2.wav")
g2Note  = pygame.mixer.Sound(r"Samples\G2.wav")
gs2Note = pygame.mixer.Sound(r"Samples\G#2.wav")
a2Note  = pygame.mixer.Sound(r"Samples\A2.wav")
as2Note = pygame.mixer.Sound(r"Samples\A#2.wav")
b2Note  = pygame.mixer.Sound(r"Samples\B2.wav")

c3Note  = pygame.mixer.Sound(r"Samples\C3.wav")
cs3Note = pygame.mixer.Sound(r"Samples\C#3.wav")
d3Note  = pygame.mixer.Sound(r"Samples\D3.wav")
ds3Note = pygame.mixer.Sound(r"Samples\D#3.wav")
e3Note  = pygame.mixer.Sound(r"Samples\E3.wav")
f3Note  = pygame.mixer.Sound(r"Samples\F3.wav")
fs3Note = pygame.mixer.Sound(r"Samples\F#3.wav")
g3Note  = pygame.mixer.Sound(r"Samples\G3.wav")
gs3Note = pygame.mixer.Sound(r"Samples\G#3.wav")
a3Note  = pygame.mixer.Sound(r"Samples\A3.wav")
as3Note = pygame.mixer.Sound(r"Samples\A#3.wav")
b3Note  = pygame.mixer.Sound(r"Samples\B3.wav")

c4Note  = pygame.mixer.Sound(r"Samples\C4.wav")
cs4Note = pygame.mixer.Sound(r"Samples\C#4.wav")
d4Note  = pygame.mixer.Sound(r"Samples\D4.wav")
ds4Note = pygame.mixer.Sound(r"Samples\D#4.wav")
e4Note  = pygame.mixer.Sound(r"Samples\E4.wav")
f4Note  = pygame.mixer.Sound(r"Samples\F4.wav")
fs4Note = pygame.mixer.Sound(r"Samples\F#4.wav")
g4Note  = pygame.mixer.Sound(r"Samples\G4.wav")
gs4Note = pygame.mixer.Sound(r"Samples\G#4.wav")
a4Note  = pygame.mixer.Sound(r"Samples\A4.wav")
as4Note = pygame.mixer.Sound(r"Samples\A#4.wav")
b4Note  = pygame.mixer.Sound(r"Samples\B4.wav")

c5Note  = pygame.mixer.Sound(r"Samples\C5.wav")
cs5Note = pygame.mixer.Sound(r"Samples\C#5.wav")
d5Note  = pygame.mixer.Sound(r"Samples\D5.wav")
ds5Note = pygame.mixer.Sound(r"Samples\D#5.wav")
e5Note  = pygame.mixer.Sound(r"Samples\E5.wav")
f5Note  = pygame.mixer.Sound(r"Samples\F5.wav")
fs5Note = pygame.mixer.Sound(r"Samples\F#5.wav")
g5Note  = pygame.mixer.Sound(r"Samples\G5.wav")
gs5Note = pygame.mixer.Sound(r"Samples\G#5.wav")
a5Note  = pygame.mixer.Sound(r"Samples\A5.wav")
as5Note = pygame.mixer.Sound(r"Samples\A#5.wav")
b5Note  = pygame.mixer.Sound(r"Samples\B5.wav")

c6Note  = pygame.mixer.Sound(r"Samples\C6.wav")
cs6Note = pygame.mixer.Sound(r"Samples\C#6.wav")
d6Note  = pygame.mixer.Sound(r"Samples\D6.wav")
ds6Note = pygame.mixer.Sound(r"Samples\D#6.wav")
e6Note  = pygame.mixer.Sound(r"Samples\E6.wav")
f6Note  = pygame.mixer.Sound(r"Samples\F6.wav")
fs6Note = pygame.mixer.Sound(r"Samples\F#6.wav")
g6Note  = pygame.mixer.Sound(r"Samples\G6.wav")
gs6Note = pygame.mixer.Sound(r"Samples\G#6.wav")
a6Note  = pygame.mixer.Sound(r"Samples\A6.wav")
as6Note = pygame.mixer.Sound(r"Samples\A#6.wav")
b6Note  = pygame.mixer.Sound(r"Samples\B6.wav")

c7Note  = pygame.mixer.Sound(r"Samples\C7.wav")
cs7Note = pygame.mixer.Sound(r"Samples\C#7.wav")
d7Note  = pygame.mixer.Sound(r"Samples\D7.wav")
ds7Note = pygame.mixer.Sound(r"Samples\D#7.wav")
e7Note  = pygame.mixer.Sound(r"Samples\E7.wav")
f7Note  = pygame.mixer.Sound(r"Samples\F7.wav")
fs7Note = pygame.mixer.Sound(r"Samples\F#7.wav")
g7Note  = pygame.mixer.Sound(r"Samples\G7.wav")
gs7Note = pygame.mixer.Sound(r"Samples\G#7.wav")
a7Note  = pygame.mixer.Sound(r"Samples\A7.wav")
as7Note = pygame.mixer.Sound(r"Samples\A#7.wav")
b7Note  = pygame.mixer.Sound(r"Samples\B7.wav")

c8Note  = pygame.mixer.Sound(r"Samples\C8.wav")

action_String.set("Samples Loaded")

#==========================Play Notes Function===============================
def playNotes():
    #Get file to play
    filename = askopenfilename()
    print("Playing: " + filename)
    name = filename.split('/')[11]
    action_Display.delete(0, END)                                       
    action_Display.insert(0, "Playing " + "\'" + name + "\'")
    root.update_idletasks()
    noteList = open(filename, 'r').read().split('\n')   

#============================================================================
    #Iterate through data from text file
    #Check what note must be played
    #Fetch note duration
    #Fetch note volume
    #Play note for duration
    #Fadeout at end adds a linear fadeout to give a mroe natural stopping effect
#============================================================================
    for i in noteList:
        dataList = i.split('_')
        note = dataList[0]
        duration = int(dataList[1])
        hold = float(dataList[2])
        volume = float(dataList[3])

#================================A0-B0=======================================
        if 'a0' in i:
            noteName = "A0"
            x = a0Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'b0' in i:
            noteName = "B0"
            x = b0Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
#=================================C1-B1======================================
        if 'c1' in i:
            noteName = "C1"
            x = c1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)                                                 
        if 'cs1' in i:
            noteName = "C#1"
            x = cs1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'd1' in i:
            noteName = "D1"
            x = d1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'ds1' in i:
            noteName = "D#1"
            x = ds1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'e1' in i:
            noteName = "E1"
            x = e1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'f1' in i:
            noteName = "F1"
            x = f1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'fs1' in i:
            noteName = "F#1"
            x = fs1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'g1' in i:
            noteName = "G1"
            x = g1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'gs1' in i:
            noteName = "G#1"
            x = gs1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'a1' in i:
            noteName = "A1"
            x = a1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'as1' in i:
            noteName = "A#1"
            x = as1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'b1' in i:
            noteName = "B1"
            x = b1Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)

#================================C2-B2=======================================
        if 'c2' in i:
            noteName = "C2"
            x = c2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)                                                 
        if 'cs2' in i:
            noteName = "C#2"
            x = cs2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'd2' in i:
            noteName = "D2"
            x = d2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'ds2' in i:
            noteName = "D#2"
            x = ds2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'e2' in i:
            noteName = "E2"
            x = e2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'f2' in i:
            noteName = "F2"
            x = f2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'fs2' in i:
            noteName = "F#2"
            x = fs2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'g2' in i:
            noteName = "G2"
            x = g2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'gs2' in i:
            noteName = "G#2"
            x = gs2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'a2' in i:
            noteName = "A2"
            x = a2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'as2' in i:
            noteName = "A#2"
            x = as2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'b2' in i:
            noteName = "B2"
            x = b2Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)

#================================C3-B3=======================================           
        if 'c3' in i:
            noteName = "C3"
            x = c3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)                                                 
        if 'cs3' in i:
            noteName = "C#3"
            x = cs3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'd3' in i:
            noteName = "D3"
            x = d3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'ds3' in i:
            noteName = "D#3"
            x = ds3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'e3' in i:
            noteName = "E3"
            x = e3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'f3' in i:
            noteName = "F3"
            x = f3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'fs3' in i:
            noteName = "F#3"
            x = fs3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'g3' in i:
            noteName = "G3"
            x = g3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'gs3' in i:
            noteName = "G#3"
            x = gs3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'a3' in i:
            noteName = "A3"
            x = a3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'as3' in i:
            noteName = "A#3"
            x = as3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'b3' in i:
            noteName = "B3"
            x = b3Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)

    #================================C4-B4=======================================           
        if 'c4' in i:
            noteName = "C4"
            x = c4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)                                                 
        if 'cs4' in i:
            noteName = "C#4"
            x = cs4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'd4' in i:
            noteName = "D4"
            x = d4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'ds4' in i:
            noteName = "D#4"
            x = ds4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'e4' in i:
            noteName = "E4"
            x = e4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'f4' in i:
            noteName = "F4"
            x = f4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'fs4' in i:
            noteName = "F#4"
            x = fs4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'g4' in i:
            noteName = "G4"
            x = g4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'gs4' in i:
            noteName = "G#4"
            x = gs4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'a4' in i:
            noteName = "A4"
            x = a4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'as4' in i:
            noteName = "A#4"
            x = as4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'b4' in i:
            noteName = "B4"
            x = b4Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
            
    #================================C5-B5======================================= 
        if 'c5' in i:
            noteName = "C5"
            x = c5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)                                                 
        if 'cs5' in i:
            noteName = "C#5"
            x = cs5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'd5' in i:
            noteName = "D5"
            x = d5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'ds5' in i:
            noteName = "D#5"
            x = ds5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'e5' in i:
            noteName = "E5"
            x = e5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'f5' in i:
            noteName = "F5"
            x = f5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'fs5' in i:
            noteName = "F#5"
            x = fs5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'g5' in i:
            noteName = "G5"
            x = g5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'gs5' in i:
            noteName = "G#5"
            x = gs5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'a5' in i:
            noteName = "A5"
            x = a5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'as5' in i:
            noteName = "A#5"
            x = as5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'b5' in i:
            noteName = "B5"
            x = b5Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)

#================================C6-B6======================================= 
        if 'c6' in i:
            noteName = "C6"
            x = c6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)                                                 
        if 'cs6' in i:
            noteName = "C#6"
            x = cs6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'd6' in i:
            noteName = "D6"
            x = d6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'ds6' in i:
            noteName = "D#6"
            x = ds6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'e6' in i:
            noteName = "E6"
            x = e6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'f6' in i:
            noteName = "F6"
            x = f6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'fs6' in i:
            noteName = "f#6"
            x = fs6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'g6' in i:
            noteName = "G6"
            x = g6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'gs6' in i:
            noteName = "G#6"
            x = gs6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'a6' in i:
            noteName = "A6"
            x = a6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'as6' in i:
            noteName = "A#6"
            x = as6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'b6' in i:
            noteName = "B6"
            x = b6Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)

#================================C7-B7======================================= 
        if 'c7' in i:
            noteName = "C7"
            x = c7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)                                                 
        if 'cs7' in i:
            noteName = "C#7"
            x = cs7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'd7' in i:
            noteName = "D7"
            x = d7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'ds7' in i:
            noteName = "D#7"
            x = ds7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'e7' in i:
            noteName = "E7"
            x = e7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'f7' in i:
            noteName = "F7"
            x = f7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'fs7' in i:
            noteName = "F#7"
            x = fs7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'g7' in i:
            noteName = "G7"
            x = g7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'gs7' in i:
            noteName = "G#7"
            x = gs7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'a7' in i:
            noteName = "A7"
            x = a7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'as7' in i:
            noteName = "A#7"
            x = as7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)
        if 'b7' in i:
            noteName = "B7"
            x = b7Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)

#==================================C8======================================== 
        if 'c8' in i:
            noteName = "C8"
            x = c8Note
            x.set_volume(volume)
            x.play(maxtime=duration)
            time.sleep(hold)

#==========================Update Display====================================           
        #Add additonal fadeout of sound
        x.fadeout(duration)
        print(noteName)
    action_Display.delete(0, END)                                       
    action_Display.insert(0, "Action Display")  

#==============================Start Button==================================
start_Button = Button(c2Frame, height = 3,
                      width = 7, text = "START",
                      font = ('open sans', 18, 'bold'),
                      bd= 6, relief = "raised", bg = "#5396b3", 
                      fg = "white", command = playNotes)
start_Button.grid(row = 0, column = 0)

#============================================================================
root.mainloop()




        


