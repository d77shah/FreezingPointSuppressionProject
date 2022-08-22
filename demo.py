import pyfirmata as pf
from jupyterplot import ProgressPlot
import numpy as np
from time import sleep

board=pf.Arduino("/dev/cu.usbmodem101") #board is the arduino object
it=pf.util.Iterator(board)
it.start()

a0=board.get_pin('a:0:i') #analog pin, number 0, mode input 

voltage=a0.read()
#returns something between 0 and 1, is 5volts
#when plugged into A0 and Ground, ans is 0volts
#when plugged into A0 and 5volts, ans is 1.0volts
#when plugged into A0 and 3.3 volts, ans is 3.3/5=0.66

print(voltage)

alpha=0.003925
v=voltage*5
kr=3824

i=v/kr
print(i)

r=(5-v)/i
print(r)

t=((r/1000)-1)/0.003925
print(t)

pp=ProgressPlot(line_names=["Voltage of AA"],x_lim=[0,1000],y_lim=[0,30],x_label='time')
for t in range(1000):
    voltage=a0.read()
    alpha=0.003925
    v=voltage*5
    kr=3824
    i=v/kr
    r=(5-v)/i
    t=((r/1000)-1)/0.003925
    pp.update(t)
    sleep(0.05)
pp.finalize()

