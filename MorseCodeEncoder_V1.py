from machine import Pin, PWM
from time import sleep

# Morse code dictionary, s is for dots and l is for the dashes
MorseCode = {
    ' ': '',
    'a': 'sl',
    'b': 'lsss',
    'c': 'lsls',
    'd': 'lss',
    'e': 's',
    'f': 'ssls',
    'g': 'lls',
    'h': 'ssss',
    'i': 'ss',
    'j': 'slll',
    'k': 'lsl',
    'l': 'slss',
    'm': 'll',
    'n': 'ls',
    'o': 'lll',
    'p': 'slls',
    'q': 'llsl',
    'r': 'sls',
    's': 'sss',
    't': 'l',
    'u': 'ssl',
    'v': 'sssl',
    'w': 'sll',
    'x': 'lssl',
    'y': 'lsll',
    'z': 'llss',
    '1': 'sllll',
    '2': 'sslll',
    '3': 'sssll',
    '4': 'ssssl',
    '5': 'sssss',
    '6': 'lssss',
    '7': 'llsss',
    '8': 'lllss',
    '9': 'lllls',
    '0': 'lllll'}

# The LEDs that will morse code out the message
dot = Pin(14, Pin.OUT)
dash = Pin(15, Pin.OUT)
buzzer = PWM(Pin(16))

slow = 0.6	# Represents the delay associated with the dash
fast = 0.3	#Represents dot delay
pitch = 1000
volume = 4000
buzzer.freq(pitch) #Higher value means higher pitch (sharpness of buzzer sound)

dot.low()
dash.low()

def letterlookup(stringval):
    for k in MorseCode:
        if MorseCode[k] == stringval:
            return k
    return " "

def blinkletter(letter):
    
    if letter != "":
        currentletter = MorseCode[letter]
    if letter == " ":
        dot.high()
        dash.high()
        sleep(0.2)
        dot.low()
        dash.low()
        sleep(.2)
        return
    
    print(letter+" : "+currentletter)
    for c in currentletter:
        if (c == "l"):
            blinkspeed = slow
            dash.high()
            buzzer.duty_u16(volume)
            sleep(blinkspeed)
            dash.low()
            buzzer.duty_u16(0)
        if (c == "s"):
            blinkspeed = fast
            dot.high()
            buzzer.duty_u16(volume)
            sleep(blinkspeed)
            dot.low()
            buzzer.duty_u16(0)
        
        sleep(.15)
            
    sleep(0.6)

def playmessage(message):
    for c in message:
        blinkletter(str.lower(c))



while True:
    message = input("Type message to be encoded: ")
    playmessage(message)
    sleep(0.8)














