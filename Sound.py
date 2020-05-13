import pyaudio
import numpy as np
import wave
import thread
import time
from pyAudioAnalysis import ShortTermFeatures

CHUNKSIZE = 64   # fixed chunk size
RATE = 8000      # 8kHz Sampling rate
SAMPLE_DUR = 0.5 # 500ms sampling with 250ms overlap

# initialize pyaudio
p = pyaudio.PyAudio()


# -- This code snippet was used to determine ID of I2S Microphone -- #

# Get input device number
#info = p.get_host_api_info_by_index(0)
#numdevices = info.get('deviceCount')
#for i in range(0, numdevices):
#        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
#            print ("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


# -- Init *MUST* be called before any of the other functions -- #
#it must also be called if Terminate() is called to resume audio stream
def Init():
    global p
    stream = p.open(format=pyaudio.paInt32, channels=1, rate=RATE,
                input=True, frames_per_buffer=CHUNKSIZE,
                input_device_index = 2)

first_half = []
second_half = []
combinedData = []
counter = 0

def AnalyzeData(data):
    F, f_names = ShortTermFeatures.feature_extraction(data, RATE, SAMPLE_DUR*RATE, (SAMPLE_DUR/2)*RATE)
    # F is the data, so save that to the CSV file for audio data
    return


#Only to be used in case that you want to store audio samples 
def WriteData(data):
    t = Time.time() # use to generate timestamp for file name
    filename = "RawAudio.wav" # <- file naming convention
    wf = wave.open(filename,'wb') #Open wave file in write bytes mode
    wf.setchannels(1)     #Mono channel audio
    wf.setsampwidth(4)    #Using 32-bit audio samples - 4 bytes
    wf.setframerate(RATE) #Set the sampling freq of audio
    wf.writeframes(b''.join(frames))
    wf.close()
    return 

def CombineData(first_half,second_half):
    global combinedData
    combinedData = []
    if counter%2 == 0:
        combinedData.append(second_half)
        combinedData.append(first_half)
    else:
        combinedData.append(first_half)
        combinedData.append(second_half)

    AnalyzeData(combinedData)

    # -- NO LONGER NEEDED -- #
    #Write to .wav file on another thread
    #WriteData(combinedData)

def DataThread(fh,sh):
    #Copy data
    f_h = fh[:]
    s_h = sh[:]
    #Do everything in a new thread
    CombineData(f_h,s_h)
    return

# -- Gathers data from the micrphone and calls WriteData then AnalyzeData() -- #
def GetData():
    global first_half, second_half, counter
    npd = []
    #d = []

    # -- Take 250ms of sound and put it in either first/second half -- #
    for i in range(0, int(RATE/CHUNKSIZE * .25)):
        data = stream.read(CHUNKSIZE)
        numpydata = np.frombuffer(data, dtype=np.uint32)
	#d.append(data)
	#npd.append(numpydata)
    if counter % 2 == 0:
        first_half = npd[:]
    else:
        second_half = npd[:]

    DataThread(first_half,second_half)
    counter += 1

def StopAudoStream():
    stream.stop_stream()
    stream.close()

def Terimante():
    stream.stop_stream()
    stream.close()
