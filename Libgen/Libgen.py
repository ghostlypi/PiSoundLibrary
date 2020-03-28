from Soundboard import *
import os
import time

start = time.time()
for i in range(20,20000):
    for j in range(1,101):
        SoundBoard.compile([[0,9,0.125,j,i]],"LibgenFREQ="+str(i)+"&AMP="+str(j)+".wav")
        os.replace("/Users/parth/Desktop/Music/Libgen/LibgenFREQ="+str(i)+"&AMP="+str(j)+".wav","/Users/parth/Desktop/Music/Libgen/FREQ="+str(i)+"/LibgenFREQ="+str(i)+"&AMP="+str(j)+".wav")
    print("FREQ="+str(i)+" Completed! "+str(time.time()-start))
