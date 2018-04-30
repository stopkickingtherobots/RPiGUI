from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
ledRed = LED(14)
ledGreen = LED(15)
ledWhite = LED(18)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

## EVENT FUNCTIONS ##
def ledRedToggle():
    if ledRed.is_lit:
        ledRed.off()
        ledRedButton["text"] = "Turn Red LED on"
        ledRedButton["bg"] = 'bisque2'
    else:
        ledRed.on()
        ledRedButton["text"] = "Turn Red LED off"
        ledRedButton["bg"] = 'red'
        ledGreen.off()
        ledGreenButton["text"] = "Turn Green LED on"
        ledGreenButton["bg"] = 'bisque2'
        ledWhite.off()
        ledWhiteButton["text"] = "Turn Green LED on"
        ledWhiteButton["bg"] = 'bisque2'
                
def ledGreenToggle():
    if ledGreen.is_lit:
        ledGreen.off()
        ledGreenButton["text"] = "Turn Green LED on"
        ledGreenButton["bg"] = 'bisque2'
    else:
        ledGreen.on()
        ledGreenButton["text"] = "Turn Green LED off"
        ledGreenButton["bg"] = 'green'
        ledWhite.off()
        ledWhiteButton["bg"] = 'bisque2'
        ledWhiteButton["text"] = "Turn White LED on"
        ledRed.off()
        ledRedButton["text"] = "Turn Red LED on"
        ledRedButton["bg"] = 'bisque2'
                
def ledWhiteToggle():
    if ledWhite.is_lit:
        ledWhite.off()
        ledWhiteButton["text"] = "Turn White LED on"
        ledWhiteButton["bg"] = 'bisque2'
    else:
        ledWhite.on()
        ledWhiteButton["text"] = "Turn White LED off"
        ledWhiteButton["bg"] = 'white'
        ledRed.off()
        ledRedButton["text"] = "Turn Red LED on"
        ledRedButton["bg"] = 'bisque2'
        ledGreen.off()
        ledGreenButton["text"] = "Turn Green LED on"
        ledGreenButton["bg"] = 'bisque2'
        
### WIDGETS ###
ledRedButton = Button(win, text = 'Turn Red LED On', font = myFont, command = ledRedToggle, bg = 'bisque2', height = 1, width = 24)
ledRedButton.grid(row=0, column=1)

ledGreenButton = Button(win, text = 'Turn Green LED On', font = myFont, command = ledGreenToggle, bg = 'bisque2', height = 1, width = 24)
ledGreenButton.grid(row=0, column=2)

ledWhiteButton = Button(win, text = 'Turn White LED On', font = myFont, command = ledWhiteToggle, bg = 'bisque2', height = 1, width = 24)
ledWhiteButton.grid(row=0, column=3)

def close():
    RPi.GPIO.cleanip()
    win.destroy()

