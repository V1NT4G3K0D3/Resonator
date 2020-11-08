import pyaudio
import winsound
import time

winsound.Beep(1000, 50)


# global constants
FREQ = 7000
dot_duration = 100  # in ms
dash_duration = 250 # in ms

# winsound.Beep(FREQ, dot_duration)
# winsound.Beep(FREQ, dash_duration)

morsetab = {
    'a': '.- ',     'b': '-... ',
    'c': '-.-. ',   'd': '-.. ',
    'e': '. ',      'f': '..-. ',
    'g': '--. ',    'h': '.... ',
    'i': '.. ',     'j': '.--- ',
    'k': '-.- ',    'l': '.-.. ',
    'm': '-- ',     'n': '-. ',
    'o': '--- ',    'p': '.--. ',
    'q': '--.- ',   'r': '.-. ',
    's': '... ',    't': '- ',
    'u': '..- ',    'v': '...- ',
    'w': '.-- ',    'x': '-..- ',
    'y': '-.-- ',   'z': '--.. ',
    '0': '----- ',  ',': '--..-- ',
    '1': '.---- ',  '.': '.-.-.- ',
    '2': '..--- ',  '?': '..--.. ',
    '3': '...-- ',  ';': '-.-.-. ',
    '4': '....- ',  ':': '---... ',
    '5': '..... ',  "'": '.----. ',
    '6': '-.... ',  '-': '-....- ',
    '7': '--... ',  '/': '-..-. ',
    '8': '---.. ',  '(': '-.--.- ',
    '9': '----. ',  ')': '-.--.- ',
    ' ': '|',       '_': '..--.- ',
}


def main(s):
    convert_string = s.lower()
    s = string_to_code(convert_string)
    print(s)
    # play(s)

def play(s):
    for i in s:
        if i == '.':
            winsound.Beep(FREQ, dot_duration)
        elif i == '-':
            winsound.Beep(FREQ, dash_duration)
        else:
            time.sleep(0.15)
    print("played")

def string_to_code(convert_string):
    res = ''
    for c in convert_string:
        try:
            res += morsetab[c]
        except KeyError:
            pass
    return res

if __name__ == '__main__':
    s = input()
    main(s)
