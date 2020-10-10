# python mergetrack.py "tracks\bass.wav,tracks\drums.wav,tracks\vocals.wav" "tracks\jam.wav"

import sys
import wave
import numpy as np

if sys.argv[1] is None:
    sys.exit("pl insert list of filenames")

try:
    if sys.argv[2] is not None:
        dest_file = sys.argv[2].strip()
except (IndexError):
    dest_file = "jam.wav"

# get cs list of audio files
fnames = sys.argv[1].split(",")
#open files & get handles list 
wavs = [wave.open(fn.strip()) for fn in fnames]

#extract frame (frames contain audio amplitude(loudness), multiple frames make up frequencies to produce sound)
frames = [w.readframes(w.getnframes()) for w in wavs]

# here's efficient numpy conversion of the raw byte buffers (read this somewhere, need more info)
# '<i2' is a little-endian two-byte integer.
#sample is within a frame per channel (need more info)
samples = [np.frombuffer(f, dtype='<i2') for f in frames]
samples = [samp.astype(np.float64) for samp in samples]

# mix as much as possible (need more info)
n = min(map(len, samples))
mix=0

#join numpy arrays
for index in range(len(fnames)):
    mix+= samples[index][:n]

# Save the result
mix_wav = wave.open(dest_file, 'w')
mix_wav.setparams(wavs[0].getparams())

# before saving, we want to convert back to '<i2' bytes: (need more info)
mix_wav.writeframes(mix.astype('<i2').tobytes())
mix_wav.close()
print("success")

