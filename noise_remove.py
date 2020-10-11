# python noise_remove.py --wav_file_path="tracks\noisewmusic.wav" --noise_sample=9 --dest_file_path="tracks\onlymusic.wav"

import sys
import os
import wave
import numpy as np
import noisereduce as nr
import soundfile as sf
import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument('wav_file_path', help='path of wave file to be processed')
parser.add_argument('--noise_sample', help='length in seconds from the start to sample noise (ideally 5, i.e record 5 secs of just noise in your room before performing)')
parser.add_argument('--dest_file_path', help='destination file locations')

args=parser.parse_args()
args=vars(args)

if args.get("wav_file_path") is None:
    sys.exit("Wav file path required, type "+os.path.basename(__file__)+" --help")


if args.get("dest_file_path") is not None:
    dest_file = args.get("dest_file_path").strip()
else:
    dest_file = args.get("wav_file_path").split(".")[0]+"_noise_removed.wav"

if args.get("noise_sample") is not None:
    noise_period=args.get("noise_sample")
else:
    noise_period=5

# get cs list of audio files
fnames = args.get("wav_file_path").split(",")
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

#audio properties
ob = sf.SoundFile(fnames[0])
sample_rate = ob.samplerate
channels=ob.channels
duration = sample_rate*channels

#get noise & audio data samples
noise_sample= samples[0][:duration*int(noise_period)]
audio_sample= samples[0][duration*int(noise_period):n]

#TODO handle attribute error, although task completes
try:
    mix = nr.reduce_noise(audio_clip=audio_sample, noise_clip=noise_sample, verbose=False)
except AttributeError as ae: 
    raise ae


# Save the result
mix_wav = wave.open(dest_file, 'w')
mix_wav.setparams(wavs[0].getparams())

# before saving, we want to convert back to '<i2' bytes: (need more info)
mix_wav.writeframes(mix.astype('<i2').tobytes())
mix_wav.close()
print("success")




