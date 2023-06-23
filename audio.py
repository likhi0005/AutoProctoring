import sounddevice as sd
import numpy as np
from colored import fg
import os
red1=fg('red')
white1=fg('white')
war1 = red1 + "Please Dont Talk"
war2 = red1 + "The exam is going to be Canceled"
SOUND_AMPLITUDE = 0
AUDIO_CHEAT = 0
CALLBACKS_PER_SECOND = 38               # callbacks per sec(system dependent)
SUS_FINDING_FREQUENCY = 2               # calculates SUS *n* times every sec
SOUND_AMPLITUDE_THRESHOLD = 20          # amplitude considered for SUS calc 
FRAMES_COUNT = int(CALLBACKS_PER_SECOND/SUS_FINDING_FREQUENCY)
AMPLITUDE_LIST = list([0]*FRAMES_COUNT)
SUS_COUNT = 0
count = 0
def print_sound(indata, outdata, frames, time, status):
    avg_amp = 0
    global SOUND_AMPLITUDE, SUS_COUNT, count, SOUND_AMPLITUDE_THRESHOLD, AUDIO_CHEAT
    vnorm = int(np.linalg.norm(indata)*10)
    AMPLITUDE_LIST.append(vnorm)
    count += 1
    AMPLITUDE_LIST.pop(0)
    if count == FRAMES_COUNT:
        avg_amp = sum(AMPLITUDE_LIST)/FRAMES_COUNT
        SOUND_AMPLITUDE = avg_amp
        if SUS_COUNT >= 2:
            print(war1)
            AUDIO_CHEAT = 1
            SUS_COUNT = 0
        if avg_amp > SOUND_AMPLITUDE_THRESHOLD:
            SUS_COUNT += 1
            print(war2)
            os.system("taskkill/im chrome.exe")
        else:
            SUS_COUNT = 0
            AUDIO_CHEAT = 0
        count = 0
def sound():
    with sd.Stream(callback=print_sound):
        sd.sleep(-1)
def sound_analysis():
    global AMPLITUDE_LIST, FRAMES_COUNT, SOUND_AMPLITUDE
    while True:
        AMPLITUDE_LIST.append(SOUND_AMPLITUDE)
        AMPLITUDE_LIST.pop(0)
        avg_amp = sum(AMPLITUDE_LIST)/FRAMES_COUNT
        if avg_amp > 0.2:
            print(white1 + "Sus...")
if __name__ == "__main__":
    sound()