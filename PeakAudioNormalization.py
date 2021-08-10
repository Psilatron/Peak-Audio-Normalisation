#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
"""
Created on Fri Nov 2 11:01:34 2018
"""

# /----------------------------[General Info]---------------------------------\
# General description here.

import numpy as np
import soundfile as sf

#--------------------------------

def MonoNorm (inputfile,PkDbInput): # (input file name, Desired Peak Db Value)
    PkNormVal=0.0
    MonoNormalised=0
    PkNormVal=np.power(10,PkDb/20) #convert dB input value  
    MonoCh = AudioIn #left channel of input audio       
    MonoPkVal=np.max(np.abs(MonoCh)) #maximum absoslute value of audio file amplitude
      
    #Normalization calculation
    MonoNormalised=MonoCh*(PkNormVal/MonoPkVal)

    outstring='norm_'+str(PkDbInput)+'dB_'+filename
    sf.write(outstring,MonoNormalised,fs)
    print('Normalised audio file saved as: ' + outstring)


def StereoNorm (inputfile,PkDbInput): # (input file name, Desired Peak Db Value)
    # The stereo audio file be normalised by using the peak value taken from 
    # channel with the highest peak as a reference. That means that if 
    # the one channel has a lower peak than the other this difference will
    # be preserved and scaled accordingly.

    maxCh=0 #variable used to detect channel with highest peak level
    ChL=ChR=0
    PkNormVal=0.0
    maxL=maxR=0
    NormL=NormR=0
    out=0
    PkNormVal=np.power(10,PkDb/20) #convert dB input value           
    ChL = AudioIn[:,0] #left channel of input audio   
    ChR = AudioIn[:,1] #right channel of input audio
    
    #maximum absosute value of audio file amplitude
    maxL=np.max(np.abs(ChL)) 
    maxR=np.max(np.abs(ChR)) 
    
    #Find channel with highest amplitude. 
    if maxL>maxR:
        maxCh=maxL
    elif maxR>maxL:
        maxCh=maxR
    elif maxL==maxR:
        maxCh=maxL

    #Normalization calculation
    NormL=ChL*(PkNormVal/maxCh)
    NormR=ChR*(PkNormVal/maxCh) 
    out=np.stack((NormL,NormR),axis=1) #create stereo array using normalised channels.
    outstring='norm_'+str(PkDbInput)+'dB_'+filename
    sf.write(outstring,out,fs)
    print('Normalised audio file saved as: ' + outstring)

#--------------------------------

#precision=9 #debug variable. max value = 308

#user defined variables
filename="duo.wav" #name of audio file, located in script directory
PkDb=-1.5  # Peak Normalisation Value. Use only values ≤0, unless you want clipping.

#channel couner variables
ChannelCount=0
x=0


#--------------------------------

[AudioIn,fs]=sf.read(filename)

#check number of channels
monocheck=np.ndim(AudioIn)
if monocheck == 1:
    ChannelCount=1
elif monocheck>1:
    for x in AudioIn[x]:
        ChannelCount=ChannelCount+1

if ChannelCount==1:
    MonoNorm(filename,PkDb)

elif ChannelCount==2:
    StereoNorm(filename,PkDb)

elif ChannelCount>2:
    print('Only mono and stereo files supported')

# references
# https://www.w3schools.com/python/numpy/numpy_array_join.asp
# https://stackoverflow.com/questions/28590669/tkinter-tkfiledialog-doesnt-exist
