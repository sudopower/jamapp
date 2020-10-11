# repo for audio jam 

## 1. [merge_track.py](merge_track.py) 
    merges audio tracks, takes wave file paths as arg
```
example: python mergetrack.py "tracks\bass.wav,tracks\drums.wav,tracks\vocals.wav" "tracks\jam.wav"

$ python mergetrack.py --help
usage: merge_track.py [-h] [--dest_file_path DEST_FILE_PATH] files_to_merge

positional arguments:
  files_to_merge        comma seperated file paths that you want to merge

optional arguments:
  -h, --help            show this help message and exit
  --dest_file_path DEST_FILE_PATH
                        destination file locations
```

## 2. [noise_remove.py](noise_remove.py)
    removes noise from audio takes, wave file path as arg, samples first n (--noise_sample) seconds of ambient noise to be removed from whole track 
```
example: python noise_remove.py --wav_file_path="tracks\noisewmusic.wav" --noise_sample=9 --dest_file_path="tracks\onlymusic.wav"

$ python noise_remove.py --help
usage: noise_remove.py [-h] [--noise_sample NOISE_SAMPLE] [--dest_file_path DEST_FILE_PATH] wav_file_path

positional arguments:
  wav_file_path         path of wave file to be processed

optional arguments:
  -h, --help            show this help message and exit
  --noise_sample NOISE_SAMPLE
                        length in seconds from the start to sample noise (ideally 5, i.e record 5 secs of just noise in your room before performing)
  --dest_file_path DEST_FILE_PATH
                        destination file locations
```