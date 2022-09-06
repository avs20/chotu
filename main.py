from email.mime import audio
import pyaudio
import wave
import msvcrt
import librosa 
import librosa.display 
import numpy as np 
import matplotlib.pyplot as plt 
import threading 
import time

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 8000  # Record at 44100 samples per second
seconds = 1
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

# print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Record continuosly and check if key press to stop 
# now how ot create a spectrogram of it 
# while True:
#     if msvcrt.kbhit():
#         print("you pressed",msvcrt.getch(),"so now i will quit")
#         break
#     data = stream.read(chunk)
#     if len(frames) == 84:
#         frames.pop(0)
#     frames.append(data)

#     audio=np.frombuffer(stream.read(chunk),dtype=np.int16)
#     S = librosa.feature.melspectrogram(audio.astype('float32'), sr=fs)
#     print(S)
#     # S = 10 * np.log(S + 1e-15)

#     plt.show(S)


audio_queue = []

def listen(audio_queue):
    while True:

        data = stream.read(chunk)
        if len(audio_queue) > 8:
            audio_queue.pop(0)            
        audio_queue.append(data)


thread = threading.Thread(target = listen, args=(audio_queue, ) , daemon = True)
thread.start()
print("We are listening")


def calculate_spectrogram():
    print("Claculates spectrogram")

def inference(audio_queue):
    while True :
        print(len(audio_queue))
        if len(audio_queue) > 8:
            while len(audio_queue) != 8:
                audio_queue.pop(0)
                calculate_spectrogram()
        else:
            calculate_spectrogram()
        time.sleep(1)

thread2 = threading.Thread(target = inference, args=(audio_queue,), daemon= True)
thread2.start()
print("we are predicting")

    

threading.Event().wait()



# Stop and close the stream 
# stream.stop_stream()
# stream.close()
# # Terminate the PortAudio interface
# p.terminate()

# print('Finished recording')

# # Save the recorded data as a WAV file
# wf = wave.open(filename, 'wb')
# wf.setnchannels(channels)
# wf.setsampwidth(p.get_sample_size(sample_format))
# wf.setframerate(fs)
# wf.writeframes(b''.join(frames))
# wf.close()


### To play what's recorded 
# play=pyaudio.PyAudio()
# stream_play=play.open(format=FORMAT,
#                       channels=CHANNELS,
#                       rate=RATE,
#                       output=True)
# for data in frames: 
#     stream_play.write(data)
# stream_play.stop_stream()
# stream_play.close()
# play.terminate()