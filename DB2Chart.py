#!/usr/bin/env python
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.dates import AutoDateLocator,DateFormatter
import string
import time
import dateutil,pylab,random
from pylab import *

FlagENCRADEC=1
FlagPOSLVDT=1
FlagTempr=1
FlagGradTempr=1
FlagPwrBoxTempr=1
FlagUI=1
FlagRMS=1
FlagDRVCur=1
FlagUI2=1




ENCRA=[]
ENCDEC=[]
Pos=[]
LVDT=[]
TRA1=[]
TRA2=[]
TDEC1=[]
TDEC2=[]
TMR1=[]
TMR2=[]
TMR3=[]
TAM=[]
TCCD1=[]
TCCD2=[]
PWRBOX=[]
GRAD0M=[]
GRAD1M=[]
GRAD2M=[]
GRAD3M=[]
GRAD4M=[]
VOL=[]
CUR=[]
UI=[]
RARMS=[]
DECRMS=[]
DrvRA1Cur=[]
DrvRA2Cur=[]
DrvDEC1Cur=[]
DrvDEC2Cur=[]
U24=[]
I24=[]
U12=[]
I12=[]
U10=[]
I10=[]
U5=[]
U6=[]
INFO=[]
sendtimeID2=[]
sendtimeID37=[]
sendtimeID42=[]
tstr=[]


DECFolErrENCRA=[]
DECFolErrENCDEC=[]
DECFolErrST=[]
RAFolErrENCRA=[]
RAFolErrENCDEC=[]
RAFolErrST=[]

AST2TimeFormat='%Y-%m-%dT%H:%M:%S'
XTimeFormat='%m%d\n%H:%M'
#================get data from db================
conn=sqlite3.connect('TeleAST32.db')
curs=conn.cursor()

fromtime="2016-02-18T00:00:00"
totime="2016-02-24T00:00:00"
t1=time.mktime(time.strptime(fromtime,AST2TimeFormat))+8*3600
t2=time.mktime(time.strptime(totime,AST2TimeFormat))+8*3600
print t1
print t2
curs.execute('SELECT * FROM TeleID2 ASC WHERE SENDTIME>? and SENDTIME<?',(t1,t2)) 
rows=curs.fetchall()
for row in rows:
    sendtimeID2.append(row[0])
    ENCRA.append(row[1])
    ENCDEC.append(row[2])
    Pos.append(row[3])
    LVDT.append(row[4])
    TRA1.append(row[5])
    TRA2.append(row[6])
    TDEC1.append(row[7])
    TDEC2.append(row[8])
    TMR1.append(row[9])
    TMR2.append(row[10])
    TMR3.append(row[11])
    TAM.append(row[12])
    TCCD1.append(row[13])
    TCCD2.append(row[14])
    VOL.append(row[15])
    CUR.append(row[16])
    UI.append(row[17])
    RARMS.append(row[18])
    DECRMS.append(row[19])
    DrvRA1Cur.append(row[20])
    DrvRA2Cur.append(row[21])
    DrvDEC1Cur.append(row[22])
    DrvDEC2Cur.append(row[23])
    INFO.append(row[24])
conn.commit()

curs.execute('SELECT * FROM TeleID37 WHERE SENDTIME>? and SENDTIME<?',(t1,t2)) 
rows=curs.fetchall()
for row in rows:
    sendtimeID37.append(row[0])
    U24.append(row[1])
    I24.append(row[2])
    U12.append(row[3])
    I12.append(row[4])
    U10.append(row[5])
    I10.append(row[6])
    U5.append(row[7])
    U6.append(row[8])
conn.commit()

curs.execute('SELECT * FROM TeleID42 WHERE SENDTIME>? and SENDTIME<?',(t1,t2)) 
rows=curs.fetchall()
for row in rows:
    sendtimeID42.append(row[0])
    PWRBOX.append(row[1])
    GRAD0M.append(row[2])
    GRAD1M.append(row[3])
    GRAD2M.append(row[4])
    GRAD3M.append(row[5])
    GRAD4M.append(row[6])
conn.commit()
conn.close()
#=========================get chart=================
#=========================get chart=================
#=========================get chart=================


limmin=0
limmax=0
step=0
print len(sendtimeID2)
if len(sendtimeID2):
 #   firstst = float(sendtimeID2[0])
#    lastst = float(sendtimeID2[len(sendtimeID2)-1])
 #   offset=int(firstst)%3600
#    print offset
#    limmin = firstst-offset
#    offset=3600-int(lastst)%3600
#    print offset
#    limmax = lastst +offset

    limmin = t1
    limmax = t2
    step = int((limmax-limmin)/36000)*3600
    if step == 0 :
        step = int((limmax-limmin)/9000)*900
    if step == 0 :
        step = int((limmax-limmin)/1000)*100
    if step == 0 :
        step = int((limmax-limmin)/90)*9
    tnn=limmin+step
    while True :
        tstr.append(time.strftime(XTimeFormat,time.gmtime(tnn)))
        tnn+=step
        if tnn>limmax+10: break

if FlagENCRADEC:
    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.68,b*1.2,w,h])
    plt.title("Axes Position")
    plt.xlabel("UT Time")
    plt.ylabel("Position(Degree)")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID2,ENCRA,'.-r',label="EncRA")
    plt.plot(sendtimeID2,ENCDEC,'.-b',label="EncDEC")
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8)
    plt.savefig('Enc.png')
 #   plt.show()
    print "Enc.png"


if FlagPOSLVDT:
    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b*1.2,w,h])
    plt.title("Focus Position")
    plt.xlabel("UT Time")
    plt.ylabel("Focus Position(mm)")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID2,Pos,'o-r',label="POS")
    plt.plot(sendtimeID2,LVDT,'o-b',label="LVDT")
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8)
    plt.savefig('Focus.png')
    print "Focus.png"

if FlagTempr:
    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b*1.2,w,h])
    plt.title("Focus Position")
    plt.xlabel("UT Time")
    plt.ylabel("Focus Position(mm)")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID2,TRA1,'.-b',label="TRA1")
    plt.plot(sendtimeID2,TRA2,'.-c',label="TRA2")
    plt.plot(sendtimeID2,TDEC1,'.-g',label="TDEC1")
    plt.plot(sendtimeID2,TDEC2,'.-k',label="TDEC2")
    plt.plot(sendtimeID2,TMR1,'.-',label="TMR1",color=(0.7,0.7,0.9))
    plt.plot(sendtimeID2,TMR2,'.-m',label="TMR2")
    plt.plot(sendtimeID2,TMR3,'.-',label="TMR3",color=(0.7,0.9,0.9))
    plt.plot(sendtimeID2,TAM,'.-',label="TAM",color=(0.9,0.7,0.9))
    plt.plot(sendtimeID2,TCCD1,'.-y',label="TCCD1")
    plt.plot(sendtimeID2,TCCD2,'.-',label="TCCD2",color=(1.0,0.8,0.5))     #plt.subplots_adjust(top=0.7)
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8,borderpad=0.1,labelspacing=0,handletextpad=0)
    plt.savefig('Tempr.png')
    print "Tempr.png"

if FlagUI:
    plt.subplot(3,1,1)
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b,w,h])
    plt.plot(sendtimeID2,VOL,'.-r',label="Vol")
    plt.title("AC Voltage")
 #   plt.xlabel("UT Time")
    plt.ylabel("V")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),"")
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8) 
    plt.grid()

    plt.subplot(3,1,2)
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b,w,h])
    plt.plot(sendtimeID2,CUR,'+b',label="Cur")
    plt.title("AC Current")
 #   plt.xlabel("UT Time")
    plt.ylabel("A")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),"")
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8) 
    plt.grid()

    plt.subplot(3,1,3)
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b,w,h])
    plt.plot(sendtimeID2,UI,'*g',label="Pwr")
    plt.title("AC Power")
    plt.xlabel("UT Time")
    plt.ylabel("W")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8) 
    plt.grid()
    
    plt.savefig('UI.png')
    print "UI.png"


if FlagRMS:
    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b*1.2,w,h])
    plt.title("Following Error")
    plt.xlabel("UT Time")
    plt.ylabel("arcsec")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID2,RARMS,'.-r',label="RA_RMS")
    plt.plot(sendtimeID2,DECRMS,'.-b',label="DEC_RMS")
    plt.legend(prop={'size':10},numpoints=1,loc=7,borderaxespad=-9) 
    plt.savefig('RMS.png')
    print "RMS.png"

if FlagDRVCur:
    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b*1.2,w,h])
    plt.title("Drives Current")
    plt.xlabel("UT Time")
    plt.ylabel("Current(A)")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID2,DrvRA1Cur,'.-r',label="RA1_Drv Cur")
    plt.plot(sendtimeID2,DrvRA2Cur,'.-k',label="RA2_Drv Cur")
    plt.plot(sendtimeID2,DrvDEC1Cur,'.-b',label="DEC1_Drv Cur")
    plt.plot(sendtimeID2,DrvDEC2Cur,'.-g',label="DEC2_Drv Cur")
    plt.legend(prop={'size':8},numpoints=1,loc=7,borderaxespad=-12) 
    plt.savefig('DrvCur.png')
    print "DrvCur.png"


print len(sendtimeID37)
if len(sendtimeID37):
##    firstst = float(sendtimeID37[0])
##    lastst = float(sendtimeID37[len(sendtimeID37)-1])
##    offset=int(firstst)%3600
##    limmin = firstst-offset
##    offset=3600-int(lastst)%3600
##    limmax = lastst +offset

##    limmin = firstst
##    limmax = lastst
    limmin = t1
    limmax = t2    
    step = int((limmax-limmin)/36000)*3600
    if step == 0 :
        step = int((limmax-limmin)/9000)*900
    if step == 0 :
        step = int((limmax-limmin)/1000)*100
    if step == 0 :
        step = int((limmax-limmin)/90)*9
    if step == 0 :
        step = 1       
    tnn=limmin+step
    while True :
        tstr.append(time.strftime(XTimeFormat,time.gmtime(tnn)))
        tnn+=step
        if tnn>limmax+10: break

if FlagUI2:
    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b*1.2,w,h])
    plt.title("Voltages")
    plt.xlabel("UT Time")
    plt.ylabel("Vol(V)")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID37,U24,'.-r',label="U24")
    plt.plot(sendtimeID37,U12,'.-k',label="U12")
    plt.plot(sendtimeID37,U10,'.-b',label="U10")
    plt.plot(sendtimeID37,U5,'.-g',label="U5")
    plt.plot(sendtimeID37,U6,'.-m',label="U6")
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8) 
    plt.savefig('VOL2.png')
    print "VOL2.png"

    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b*1.2,w,h])
    plt.title("Currents")
    plt.xlabel("UT Time")
    plt.ylabel("Cur(A)")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID37,I24,'.-r',label="I24")
    plt.plot(sendtimeID37,I12,'.-k',label="I12")
    #    plt.plot(sendtimeID37,I10,'.-b',label="I10")
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8) 
    plt.savefig('Cur2.png')
    print "Cur2.png"

print len(sendtimeID42)
if len(sendtimeID42):
##    firstst = float(sendtimeID42[0])
##    lastst = float(sendtimeID42[len(sendtimeID42)-1])
##    offset=int(firstst)%3600
##    limmin = firstst-offset
##    offset=3600-int(lastst)%3600
##    limmax = lastst +offset
##
##    limmin = firstst
##    limmax = lastst
    limmin = t1
    limmax = t2
    step = int((limmax-limmin)/36000)*3600
    if step == 0 :
        step = int((limmax-limmin)/9000)*900
    if step == 0 :
        step = int((limmax-limmin)/1000)*100
    if step == 0 :
        step = int((limmax-limmin)/90)*9
    if step == 0 :
        step = 1    
    tnn=limmin+step
    while True :
        tstr.append(time.strftime(XTimeFormat,time.gmtime(tnn)))
        tnn+=step
        if tnn>limmax+10: break

if FlagGradTempr:
    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b*1.2,w,h])
    plt.title("Tempratures")
    plt.xlabel("UT Time")
    plt.ylabel("Temprs(C)")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID42,GRAD0M,'.-r',label="0m")
    plt.plot(sendtimeID42,GRAD1M,'.-k',label="1m")
    plt.plot(sendtimeID42,GRAD2M,'.-b',label="2m")
    plt.plot(sendtimeID42,GRAD3M,'.-g',label="3m")
    plt.plot(sendtimeID42,GRAD4M,'.-m',label="4m")
    plt.legend(prop={'size':11},numpoints=1,loc=7,borderaxespad=-8) 
    plt.savefig('Tempr_grad.png')
    print "Tempr_grad.png"

if FlagPwrBoxTempr:
    FEnc=plt.figure(figsize=(10,6))
    l,b,w,h=plt.gca().get_position().bounds
    plt.gca().set_position([l*0.618,b*1.2,w,h])
    plt.title("Temprature of PowerBox")
    plt.xlabel("UT Time")
    plt.ylabel("Temprs(C)")
    plt.xlim(limmin,limmax)
    plt.xticks(np.arange(limmin+step,limmax,step),tstr)
    plt.grid()
    plt.plot(sendtimeID42,PWRBOX,'.-r',label="PwrBox Tempr")
    plt.legend(prop={'size':8},numpoints=1,loc=7,borderaxespad=-11) 
    plt.savefig('Tempr_PwrBox.png')
    print "Tempr_PwrBox.png"
#================end===========================

