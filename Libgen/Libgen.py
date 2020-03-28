from Soundboard import *
import os
import time

start = time.time()
for i in range(20,20):
    for j in range(100,101):
        SoundBoard.build([[0,9,0.125,j,i]])
        SoundBoard.compile("LibgenFREQ="+str(i)+"&AMP="+str(j)+".wav")
        #os.replace("/Users/parth/Desktop/Music/Libgen/LibgenFREQ="+str(i)+"&AMP="+str(j)+".wav","/Users/parth/Desktop/Music/Libgen/FREQ="+str(i)+"/LibgenFREQ="+str(i)+"&AMP="+str(j)+".wav")
    print("FREQ="+str(i)+" Completed! "+str(time.time()-start))
