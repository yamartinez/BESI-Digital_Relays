import pyaudio
import numpy as np

CHUNKSIZE = 64 # fixed chunk size
RATE = 8000

# initialize portaudio
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
    stream = p.open(format=pyaudio.paInt32, channels=1, rate=RATE,
                input=True, frames_per_buffer=CHUNKSIZE,
                input_device_index = 2)

first_half = []
second_half = []
combinedData = []
counter = 0

def AnalyzeData():
    #Use the Python audio lib that Nutta Sent to Analyze the Audio File
    #Use System Call to Start pyAudioAnalysis -> ShortTermFeatures.py with file name

    return

def WriteData():
    global combinedData
    combinedData = []
    if counter%2 == 0:
        combinedData.append(second_half)
        combinedData.append(first_half)
    else:
        combinedData.append(first_half)
        combinedData.append(second_half)

    #Write to .wav file on another thread



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
	npd.append(numpydata)
    if counter % 2 == 0:
        first_half = numpydata
    else:
        second_half = numpydata

    WriteData()
    AnalyzeData()
    counter += 1

def StopAudoStream():
    stream.stop_stream()
    stream.close()

def Terimante():
    stream.stop_stream()
    stream.close()
