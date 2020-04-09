import pyaudio
import numpy as np

CHUNKSIZE = 1024 # fixed chunk size
RATE = 44100

# initialize portaudio
p = pyaudio.PyAudio()

# Get input device number
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print ("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

stream = p.open(format=pyaudio.paInt16, channels=2, rate=RATE,
                input=True, frames_per_buffer=CHUNKSIZE,
                input_device_index = 2)

# do this as long as you want fresh samples
data = stream.read(CHUNKSIZE)
numpydata = np.fromstring(data, dtype=np.int16)

# close stream
stream.stop_stream()
stream.close()
