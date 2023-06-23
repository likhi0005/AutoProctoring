import speech_recognition
import pyttsx3
import sounddevice as sd
from colored import fg
import os
import platform
import sys

red1=fg('red')
white1=fg('white')
yellow1 =fg('yellow')
def print_s(indata, outdata, frames, time, status):
    recognizer = speech_recognition.Recognizer()
    count = 0
    ad =0
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio =recognizer.listen(mic)
                if (audio):
                    print(red1 + "\n\nPlease dont talk\n")
                    print(yellow1 + "Your exam will be cancelled\n\n\n" + white1)
                    count = count + 1
                    ad = ad + 1
                    if (ad):
                        if platform.system() == 'Windows':
                            import winsound
                            frequency = 2500  # Set frequency (Hz)
                            duration = 1000  # Set duration (ms)
                            winsound.Beep(frequency, duration)
                        elif platform.system() == 'Linux':
                            duration = 1  # Set duration (s)
                            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (frequency,duration))
                        else:
                            sys.stderr.write('Your platform is not supported.')
                            sys.exit()
                if (count ==3):
                    os.system("taskkill/im chrome.exe")                   
        except speech_recognition.UnknownValueError():
            recognizer = speech_recognition.Recognizer()
            continue
def sound():
    with sd.Stream(callback=print_s):
        sd.sleep(-1)
if __name__ == "__main__":
    sound()
import platform
import sys