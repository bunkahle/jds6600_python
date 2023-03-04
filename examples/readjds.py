#!/usr/bin/python
# -*- coding: utf-8 -*-

# example application to read and change the status of a JDS6600
# connected over USB

# version 0.1 - 20180126
# version 0.2 - 20191007

# kristoff Bonne (ON1ARF)
# slightly corrected by Andreas Bunkahle for the new machines in 2023

# import library

from __future__ import print_function

import sys, time
from jds6600 import jds6600

j = jds6600("COM7")

print(j.getAPIinfo_version())
print(j.getAPIinfo_release())


# API information calls
print(j.getinfo_devicetype())
print(j.getinfo_serialnumber())

print(j.getinfo_waveformlist())

# get status of jds6600
print(j.getchannelenable())

for ch in (1,2):
	print("Channel "+str(ch), "Waveform:", j.getwaveform(ch))
	print("Channel "+str(ch), "Frequency:", j.getfrequency(ch))
	print("Channel "+str(ch), "Amplitude:", j.getamplitude(ch))
	print("Channel "+str(ch), "Offset:", j.getoffset(ch))
	print("Channel "+str(ch), "Dutycycle:", j.getdutycycle(ch))

print("Phase:", j.getphase())

# changing status
j.setfrequency(1,1000)
time.sleep(2)	
j.setfrequency(1,40000,1)
time.sleep(2)
j.setwaveform(2,2)
time.sleep(2)
j.setwaveform(1,"sinc")
j.setchannelenable(True, False)
time.sleep(2)
j.setchannelenable(False, True)
time.sleep(2)
j.setchannelenable(True, True)
time.sleep(2)
j.setchannelenable(False, False)
