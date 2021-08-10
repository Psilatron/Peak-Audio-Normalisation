# Peak-Audio-Normalisation
A python script which can peak normalise mono or stereo .wav format audio files based on the user defined value.

This script will accept either mono or stereo .wav format audio files and normalise their peaks based on the value set by by the user. There are no restrictions on the normalization value, however a gain > 0 will result in distortion; for standard operation keep this value 0dB or below.

The stereo audio file be normalised by using the peak value taken from channel with the highest peak as a reference. That means that if the one channel has a lower peak than the other this difference will be preserved and scaled accordingly.

To run the script, keep the audio file you wish to normalise in the same directory as this script. It will automatically detect if the file is mono or stereo and write the output file in the same directory as 'norm_xdB_filename.wav'.

This script will be expanded upon in another repository with the capability of batch processing a directory of .wav files, which can be quite usefull for setting a bunch of tracks to a user defined value in preparing for mixing and mastering. Normally the value for this purpose is set to between -6dBFS and -3dBFS to allow for headroom.
