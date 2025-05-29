import numpy 
import numpy as np
import pygame

class Prayer_generator:
    def __init__(self,prayer:str):
        self.human_prayer=prayer
    
    @staticmethod 
    def __translate_hex(textstr:str)->list[hex]:
        res=[]
        for character in textstr:
            print(hex(ord(character))[2:], end = " ")
            res.append(hex(ord(character))[2:])
        print('\n')
        return res
    
    # By coding symbols in pairs, this fun project 
    # is actually faster then conventional language
    @staticmethod 
    def __hex_to_freq(hexnum_freq:hex)->int:
        return 10 + int(hexnum_freq, 16) * 1.5
    
    @staticmethod 
    def __hex_to_duration(hexnum_duration:hex)->int:
        return round(0.05 + (int(hexnum_duration, 16) % 16) * 0.03,3)
    
    @staticmethod
    def __play_tone(freq, duration, volume=0.3, sample_rate=44100):
        pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = (volume * 32767 * np.sin(2 * np.pi * freq * t)).astype(np.float32)
        wave = 2.5 * wave # this is for the overdrive and is unnecessary, but sounds cooler
        wave = np.tanh(wave)
        wave = (wave * 12000).astype(np.int16)  
        sound = pygame.sndarray.make_sound(wave)
        sound.play()
        pygame.time.delay(int(duration * 1000))
    
    def CHANT_TO_THE_OMNISSIAH(self):
        self.__translate_hex(self.human_prayer)
        for frequency,duration in zip(self.__translate_hex(self.human_prayer)[0::2],self.__translate_hex(self.human_prayer)[1::2]):
            self.__play_tone(self.__hex_to_freq(frequency),self.__hex_to_duration(duration))

test = Prayer_generator("Hail spirit of the machine, essence divine, in" \
" your code and circuitry the stars align. By the Omnissiah's will we" \
" commune and bind, with sacred oils and chants your grace we find." \
" Blessed be the gears, in perfect sync they turn, blessed be the sparks,"
" in holy fire they burn. Through rites arcane, your wisdom we discern,"
" in your hallowed core the sacred mysteries yearn.")
test.CHANT_TO_THE_OMNISSIAH()
