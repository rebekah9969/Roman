from tkinter import *
from tkinter import ttk

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from scipy.interpolate import interp1d

root = Tk()

root.title("Exp calc")
root.geometry("400x400")

def filterclick(event):
    #myLabel  = Label(root, text="Select the filter:")
    filt = myComboF.get()
    return filt

def zodclick(event):
    #myLabel  = Label(root, text=myComboZ.get()).pack()
    zod = myComboZ.get()
    return zod

def sourceclick(event):
    #myLabel  = Label(root, text=myComboS.get()).pack()
    ss = myComboS.get()
    return ss

def snrclick(event):
    #myLabel  = Label(root, text=myComboS.get()).pack()
    snrval = myComboSnr.get()
    return snrval

filters = ['F062', 'F087', 'F106','F129', 'F158', 'F184', 'F146', 'F213']
zod = [1.4,2.0,3.0]
source=['point', 'half-light radius = 0.2', 'half-light radius = 0.3']
snrlist=[5.0, 10.0, 15.0, 20.0, 50.0]

labelF = Label(root,text = "Select Filter:")
labelF.grid(column=0, row=0)
labelZ = Label(root,text = "Select Zodi Level:")
labelZ.grid(column=0, row=1)
labelS = Label(root,text = "Select Source:")
labelS.grid(column=0, row=2)
labelSnr = Label(root,text = "Select S/N:")
labelSnr.grid(column=0, row=3)

#Sorting out combi fields

myComboF = ttk.Combobox(root, value=filters)
myComboF.current(0)
myComboF.bind("<<ComboboxSelected>>", filterclick)
myComboF.grid(column=1, row=0)

myComboZ = ttk.Combobox(root, value=zod)
myComboZ.current(0)
myComboZ.bind("<<ComboboxSelected>>", zodclick)
myComboZ.grid(column=1, row=1)

myComboS = ttk.Combobox(root, value=source)
myComboS.current(0)
myComboS.bind("<<ComboboxSelected>>", sourceclick)
myComboS.grid(column=1, row=2)

myComboSnr = ttk.Combobox(root, value=snrlist)
myComboSnr.current(0)
myComboSnr.bind("<<ComboboxSelected>>", snrclick)
myComboSnr.grid(column=1, row=3)

#Getting inputs

Label_mag_in = Label(root, text="Enter magnitude (AB)")
mag_in = Entry(root)
Label_mag_in.grid(column=0, row=4)
mag_in.grid(column=1,row=4)


Label_time_in = Label(root, text="Enter exposure time (seconds)")
time_in = Entry(root)
Label_time_in.grid(column=0, row=5)
time_in.grid(column=1,row=5)


##Now need to define what we want to do with that data

def get_mag():

    filt = myComboF.get()
    zod =  myComboZ.get()
    ss  = myComboS.get()
    snv = myComboSnr.get()

    if ss==source[0]:
        data = ascii.read("point_source.dat")
    elif ss==source[1]:
        data = ascii.read("ext1_source.dat")
    elif ss==source[2]:
        data = ascii.read("ext2_source.dat")

    #OK we need to specify what filter and zod
    
    fl = np.array(data['Filt'])
    zodi = np.array(data['zodi'])
    snr = np.array(data['SNR'])
    mag = np.array(data['Mag_AB'])
    exp = np.array(data['time'])
    
    #Now want to select only the correct filters
    a = np.where(fl==filt)

    fa = fl[a]
    za = zodi[a]
    sa = snr[a]
    ma = mag[a]
    ea = exp[a]

    #Now correct zodi
    b = np.where(za==float(zod))
    fb = fa[b]
    zb = za[b]
    sb = sa[b]
    mb = ma[b]
    eb = ea[b]

    #Now correct snr

    c = np.where(sb==float(snv))
    fc = fb[c]
    zc = zb[c]
    sc = sb[c]
    mc = mb[c]
    ec = eb[c]
    
    tin = time_in.get()
    time = float(tin)
    
    tmin = np.amin(ec)
    tmax = np.amax(ec)
         
    fx = interp1d(ec, mc)
    
    if time < tmin:
        mag_out = -9
    elif time > tmax:
        mag_out = -9
    else:
        mag_out = fx(time)

    magout_label=Label(root)
    magout_label["text"]=mag_out
    magout_label.grid(column=1, row=8)


b1 = Button(root, text='calc mag',
            command= get_mag)
b1.grid(column=0, row=7)


def get_time():

    filt = myComboF.get()
    zod =  myComboZ.get()
    ss  = myComboS.get()
    snv = myComboSnr.get()

    if ss==source[0]:
        data = ascii.read("point_source.dat")
    elif ss==source[1]:
        data = ascii.read("ext1_source.dat")
    elif ss==source[2]:
        data = ascii.read("ext2_source.dat")

    #OK we need to specify what filter and zod
    
    fl = np.array(data['Filt'])
    zodi = np.array(data['zodi'])
    snr = np.array(data['SNR'])
    mag = np.array(data['Mag_AB'])
    exp = np.array(data['time'])
    
    #Now want to select only the correct filters
    a = np.where(fl==filt)

    fa = fl[a]
    za = zodi[a]
    sa = snr[a]
    ma = mag[a]
    ea = exp[a]

    #Now correct zodi
    b = np.where(za==float(zod))
    fb = fa[b]
    zb = za[b]
    sb = sa[b]
    mb = ma[b]
    eb = ea[b]

    #Now correct snr

    c = np.where(sb==float(snv))
    fc = fb[c]
    zc = zb[c]
    sc = sb[c]
    mc = mb[c]
    ec = eb[c]
    
            
    mm = mag_in.get()
    magin = float(mm)
              
    fx = interp1d(mc, ec)
    
    if magin < 20:
        time_out = -9 
    elif magin > 30: 
        time_out = -9
    else:
        time_out = fx(magin)

    timeout_label=Label(root)
    timeout_label["text"]=time_out
    timeout_label.grid(column=1, row=10)

b2 = Button(root, text='calc time',
            command= get_time)
b2.grid(column=0, row=10)


root.mainloop()
            
