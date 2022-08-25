# Initial code setup by importing modules and interfacing Arduino Uno
import pyfirmata as pf
from jupyterplot import ProgressPlot
import numpy as np
from time import sleep

# An Arduino object ‘board’ and an iterator thread were created to use the analog ports of the Uno
board=pf.Arduino("/dev/cu.usbmodem101") #board is the arduino object
it=pf.util.Iterator(board)
it.start()

# A variable ‘a0’ was created to collect reading
a0=board.get_pin('a:0:i') #analog pin, number 0, mode input 

# File called ‘saltmeltingtemp.txt’ was created to store the data for time and temperature
with open("saltmeltingtemp.txt","w") as f:
    f.write("Time \t Temperature")
    
# Progress plot creation for a real-time graph
pp=ProgressPlot(plot_names = ["Temperature v/s Time Graph"],x_lim = [0,1000],y_lim = [-20,40],line_names = ["Melting temperature"],x_label = "Time per minute")

#Converting voltage to temperature and storing time and temperature data in a text file
for t in range(500):
    alpha=0.003925              #temperature coefficient of resistance for platinum
    v=a0.read()*5               #reads voltage between 0 and 1, and is multiplied with 5 
    kr=3824                     #known resistance in Ohms
    kr=4000
    i=v/kr
    r=(5-v)/i                   #5V port was used, hence the coefficient
    temp=((r/1000)-1)/alpha     #temperature calculation based on resistance values
    
    #appending time and temperature values to the text file
    with open("saltmeltingtemp.txt","a") as f:
        f.write(str(t) + " " + "\t" + str(temp) + "\n")
    pp.update(temp)
    
sleep(60)
pp.finalize()
