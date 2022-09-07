I was able to run pyaudio on windows.

I have WSL as linux and it doesn't have audio driver by default. SO can't install pyaudio directly to it. Need to install some pulse audio on both windows and WSL to make it work so I went with windows.

Current problem is how to get 1 second slidning windo in chotu. I need to understand the params of framerate, sample size, in the pyaudio constructor.

4 Sept I got the value of last 1 second on click.

Now the question is to how frequently create the spectrograms.

Should we get into 25ms intervals. This will lead to 40 spectrograms per second. Or we do in every 1 second.

Let’s start with each one second.

---------------- 

6 Sept 2022 

------------- 

So we want to continously listen the audio and continuosly calculate the spectrogram also.  

 

So whenever we want to predict we take the last 1 second of audio and do spectrogram of it.  

 

This seems like a thread problem. A separate thread will calculate the spectrogram, sleep and calculate again.  

 

Also, we want to continously listen 

We got it working 
------------------------------
7 Sept 2022
-----------------------------
Let's try to make mel frequency spectrograms from the last 1 min audio