
import pyaudio
import wave
import os 
import pyautogui
import speech_recognition as sr
import random
try:
    j=0
    while True:
        
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5


        p = pyaudio.PyAudio()
        WAVE_OUTPUT_FILENAME = str(j)+".wav"
            
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        try:
            filename = WAVE_OUTPUT_FILENAME
            r = sr.Recognizer()
            with sr.AudioFile(filename) as source:
          
                audio_data = r.record(source)
                
                text = r.recognize_google(audio_data)
                print(text)
            os.remove(WAVE_OUTPUT_FILENAME)
            get_text=text.split()

            target_text=["Samuel","samuel","britto","Britto","register number 64","64","sixty four","sixty for","registor number sixty four"]

            output = ["64 present","Present"]
            choice=random.choice(output)
            for target in get_text:
                if target in target_text:
                    
                    pyautogui.click(x=632, y=686)
                    pyautogui.write(choice) 

                    pyautogui.press('enter') 
                    print("")
                    continue
        except:
            continue

        j+=1
except:
    print("Restart the bot!")
