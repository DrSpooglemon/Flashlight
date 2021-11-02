from threading import Thread
from time import sleep
from kivy.clock import mainthread

morse = {'A': '.-',   'G': '--.',  'M': '--',   'S': '...', 'Y': '-.--', 
         'B': '-...', 'H': '....', 'N': '-.',   'T': '-',   'Z': '--..',
         'C': '-.-.', 'I': '..',   'O': '---',  'U': '..-',  
         'D': '-..',  'J': '.---', 'P': '.--.', 'V': '...-', 
         'E': '.',    'K': '-.-',  'Q': '--.-', 'W': '.--',  
         'F': '..-.', 'L': '.-..', 'R': '.-.',  'X': '-..-'}


class PatternController:
    
    def __init__(self, app, flash):
        self.app = app
        self.flash = flash
        
    def __call__(self, string, loop=False):
        self._generate_sequence_string(string.upper())
        self._do_sequence(loop)
        
    def _generate_sequence_string(self, string):
        self._sequence_string = ' '.join([morse[char] for char in string])
        
    @mainthread
    def _do_sequence(self, loop):
        self._running = True
        def seq():
            sequence = (char for char in self._sequence_string)
            while self._running:
                try:
                    self._action(next(sequence))
                except StopIteration:
                    if loop:
                        self._action(' ')
                        self._action(' ')
                        sequence = (char for char in self._sequence_string)
                    else:
                        break
        self.thread = Thread(target=seq)
        self.thread.start()
        
    def _action(self, char):
        if char == '.':
            self._dot()
        elif char == '-':
            self._dash()
        else:
            self._rest()
            
    def _dot(self):
        try:
            self.flash.on()
            sleep(.2)
            self.flash.off()
            sleep(.1)
        except:
            print('dot')
            sleep(.3)
            
    def _dash(self):
        try:
            self.flash.on()
            sleep(.6)
            self.flash.off()
            sleep(.1)
        except:
            print('dash')
            sleep(.7)
            
    def _rest(self):
        sleep(.2)
        
    def stop(self):
        self._running = False