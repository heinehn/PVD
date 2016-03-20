# -*- coding: utf-8 -*-
from pylab import*
import numpy as np
import os
import re

dir = os.getcwd()
#os.chdir(dir + "/Log")

#fileNumberFromUser = input("Type file number (S2P1-Al_Oflow_#): ")
#fileName = "S2P1-Al_Oflow_" + str(fileNumberFromUser)
print "***********************\n"
print "Angstrom super plotter\n"
print "***********************\n"
print "Enter filname with .log"

def removeFileExtension(filename):
	return re.sub(r"\.[a-zA-Z]+$", "" ,filename)

#Finding directory of .py-file
fileNameFromUser = raw_input("File name: ")
fileName = fileNameFromUser

my_path = os.path.abspath(dir)
logPath = dir + "/Log"
imagePath = dir + "/Images"
epsImagePath = imagePath + "/eps/" 
pngImagePath = imagePath + "/png/"

#Creating Image, eps and png folders
try:
    os.stat(imagePath)
except:
	os.mkdir(imagePath)
try:
	os.stat(epsImagePath)
except:
	os.mkdir(epsImagePath)
try:
    os.stat(pngImagePath)
except:
	os.mkdir(pngImagePath)

#Create sensor data from log directory
os.chdir(logPath)
inputSensor_1 = np.loadtxt(fileName  , delimiter = ',', dtype = 'float', skiprows = 6, usecols = (12,13,14))
inputSensor_2 = np.loadtxt(fileName  , delimiter = ',', dtype = 'float', skiprows = 6, usecols = (15,16,17))
inputSensor_3 = np.loadtxt(fileName  , delimiter = ',', dtype = 'float', skiprows = 6, usecols = (18,19,20))
inputSensor_4 = np.loadtxt(fileName  , delimiter = ',', dtype = 'float', skiprows = 6, usecols = (21,22,23))
inputOutput_1 = np.loadtxt(fileName  , delimiter = ',', dtype = 'float', skiprows = 6, usecols = (7,8,9,10))


#Create process time
time = []
for i in range(0,len(inputSensor_2)):
	x = i
	time.append(x)

#Figure 1 - Frequency vs Time
fig1 = figure()
ax = fig1.add_subplot(1,1,1)
grid('on')
#ax.plot(time,inputSensor_1[:,2], label = r'Sensor 1', color = 'k')
ax.plot(time,inputSensor_2[:,2]*1e6, label = r'Sensor 2', color = 'r')
#ax.plot(time,inputSensor_3[:,2], label = r'Sensor 3', color = 'gray')
ax.plot(time,inputSensor_4[:,2]*1e6, label = r'Sensor 4', color = 'b')
xlabel(r'Process time,[s]', size = 20,labelpad= 5 )
ylabel(r'Frequency, [MHz]',size = 20, labelpad = 5)
title( r'Sensor frequency vs time: ' + removeFileExtension(fileName) )
legend(loc='smart')
fig1.savefig(epsImagePath + removeFileExtension(fileName) + '_Frequency' ,bbox_inches='tight', format = "eps")
fig1.savefig(pngImagePath + removeFileExtension(fileName) + '_Frequency' ,bbox_inches='tight', format = "png")


#Figure 2 - Rate vs Time
fig2 = figure()
bx = fig2.add_subplot(1,1,1)
grid('on')
#bx.plot(time,inputSensor_1[:,1], label = r'Sensor 1', color = 'k')
bx.plot(time,inputSensor_2[:,1], label = r'Sensor 2', color = 'r')
#bx.plot(time,inputSensor_3[:,1], label = r'Sensor 3', color = 'gray')
bx.plot(time,inputSensor_4[:,1], label = r'Sensor 4', color = 'b')
bx2 = bx.twinx() #Make double y-axis with power
bx2.plot(time, inputOutput_1[:,3], 'k')
bx.set_xlabel(r'Process time,[s]', size = 20,labelpad= 5 )
bx.set_ylabel(r'Rate, [$\frac{A}{s}$]',size = 20, labelpad = 5)
bx2.set_ylabel(r'Power, [%]',size = 20, labelpad = 5)
title( r'Deposition rate vs time: ' + removeFileExtension(fileName) )
bx.legend(loc='smart')
bx.set_ylim(-0.1,)
bx2.set_ylim(0,50)
fig2.savefig(epsImagePath + removeFileExtension(fileName) + '_Rate' ,bbox_inches='tight', format = "eps")
fig2.savefig(pngImagePath + removeFileExtension(fileName) + '_Rate' ,bbox_inches='tight', format = "png")


#Figure 3 - Thickness vs Time
fig3 = figure()
cx = fig3.add_subplot(1,1,1)
grid('on')
#cx.plot(time,inputSensor_1[:,0]*10**2, label = r'Sensor 1', color = 'k')
cx.plot(time,inputSensor_2[:,0]*10**2, label = r'Sensor 2', color = 'r')
#cx.plot(time,inputSensor_3[:,0]*10**2, label = r'Sensor 3', color = 'gray')
cx.plot(time,inputSensor_4[:,0]*10**2, label = r'Sensor 4', color = 'b')
xlabel(r'Process time,[s]', size = 20,labelpad= 5 )
ylabel(r'Thickness, [$nm$]',size = 20, labelpad = 5)
title( r'Film thickness vs time: ' + removeFileExtension(fileName) )
legend(loc='smart')
fig3.savefig(epsImagePath + removeFileExtension(fileName) + '_Thickness' ,bbox_inches='tight', format = "eps")
fig3.savefig(pngImagePath + removeFileExtension(fileName) + '_Thickness' ,bbox_inches='tight', format = "png")
show()

