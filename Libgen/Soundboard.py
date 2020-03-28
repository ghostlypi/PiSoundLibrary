import math
import wave
import struct
import os

class SoundBoard:
    def compile(arr,file_name):
        # Open up a wav file
        wav_file=wave.open(file_name,"w")
        # wav params
        nchannels = 1
        sample_rate = 44100
        sampwidth = 2
        nframes = 0;
        for i in range(len(arr)):
            nframes += arr[i][3]*sample_rate

        # 44100 is the industry standard sample rate - CD quality.  If you need to
        # save on file size you can adjust it downwards. The stanard for low quality
        # is 8000 or 8kHz.
        comptype = "NONE"
        compname = "not compressed"
        wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

        # WAV files here are using short, 16 bit, signed integers for the
        # sample size.  So we multiply the floating point data we have by 32767, the
        # maximum value for a short integer.  NOTE: It is theortically possible to
        # use the floating point -1.0 to 1.0 data directly in a WAV file but not
        # obvious how to do that using the wave module in python.
        for i in range(len(arr)):
            s = arr[i][2]
            a = arr[i][3]/100*32767
            freq = arr[i][4]
            for j in range(int(44100*s)):
                wav_file.writeframes(struct.pack('h',int(a*math.sin(freq*j*2*math.pi/44100))))
        wav_file.close()
        return
