#!/usr/bin/env python
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.dates import AutoDateLocator,DateFormatter
import string
import time
import dateutil,pylab,random
from pylab import *


Logfn= 'teleinfo.txt'
flog=open(Logfn,'r')

FlagENCRADEC=1
FlagPOSLVDT=1
FlagTempr=1
FlagGradTempr=1
FlagPwrBoxTempr=1
FlagUI=1
FlagRMS=1
FlagDRVCur=1
FlagUI2=1

AST2TimeFormat='%Y-%m-%dT%H:%M:%S'
XTimeFormat='%m%d\n%H:%M'
#================ini==========================
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
#=================start=================
cc=0
while True:
    lines1=flog.readline()
    if not lines1:break
#    if len(lines1)<30 :break
    cc=cc+1
    if '<ID=2><HA=' in lines1:
        s0=lines1.find('ENCRA')
        if s0 != -1:
            s0+=6
            e0=lines1.find('>',s0)
            value=string.atof(lines1[s0:e0])
            ENCRA.append(value)
            
        s1=lines1.find('ENCDEC')
        if s1 != -1:
            s1+=7
            e1=lines1.find('>',s1)
            value=string.atof(lines1[s1:e1])
            ENCDEC.append(value)
            
        s2=lines1.find('POS')
        if s2 != -1:
            s2+=4
            e2=lines1.find('>',s2)
            value=string.atof(lines1[s2:e2])
            Pos.append(value)
        
        s2=lines1.find('LVDT')
        if s2 != -1:
            s2+=5
            e2=lines1.find('>',s2)
            value=string.atof(lines1[s2:e2])
            LVDT.append(value)
            
        s3=lines1.find('TRA1')
        if s3 != -1:
            s3+=5
            e3=lines1.find('>',s3)
            value1=string.atof(lines1[s3:e3])
            if value1<100:
                TRA1.append(value1)
            else :
                TRA1.append(0)
        
        s4=lines1.find('TRA2')
        if s4 != -1:
            s4+=5
            e4=lines1.find('>',s4)
            value2=string.atof(lines1[s4:e4])
            if value2<100:
                TRA2.append(value2)
            else :
                TRA2.append(0)

        s5=lines1.find('TDEC1')
        if s5 != -1:
            s5+=6
            e5=lines1.find('>',s5)
            value3=string.atof(lines1[s5:e5])
            if value3<100:
                TDEC1.append(value3)
            else :
                TDEC1.append(0)
            
        s6=lines1.find('TDEC2')
        if s6 != -1:
            s6+=6
            e6=lines1.find('>',s6)
            value4=string.atof(lines1[s6:e6])
            if value4<100:
                TDEC2.append(value4)
            else :
                TDEC2.append(0)

        s7=lines1.find('TMR1')
        if s7 != -1:
            s7+=5
            e7=lines1.find('>',s7)
            value=string.atof(lines1[s7:e7])
            if value<100:
                TMR1.append(value)
            else :
                TMR1.append(0)
        
        s7=lines1.find('TMR2')
        if s7 != -1:
            s7+=5
            e7=lines1.find('>',s7)
            value=string.atof(lines1[s7:e7])
            if value<100:
                TMR2.append(value)
            else :
                TMR2.append(0)

        s7=lines1.find('TMR3')
        if s7 != -1:
            s7+=5
            e7=lines1.find('>',s7)
            value=string.atof(lines1[s7:e7])
            if value<100:
                TMR3.append(value)
            else :
                TMR3.append(0)
            
        s8=lines1.find('TAM')
        if s8 != -1:
            s8+=4
            e8=lines1.find('>',s8)
            value=string.atof(lines1[s8:e8])
            if value<100:
                TAM.append(value)
            else :
                TAM.append(0)

        s9=lines1.find('TCCD1')
        if s9 != -1:
            s9+=6
            e9=lines1.find('>',s9)
            value=string.atof(lines1[s9:e9])
            if value<100:
                TCCD1.append(value)
            else :
                TCCD1.append(0)
            
        s10=lines1.find('TCCD2')
        if s10 != -1:
            s10+=6
            e10=lines1.find('>',s10)
            value=string.atof(lines1[s10:e10])
            if value<100:
                TCCD2.append(value)
            else :
                TCCD2.append(0)

        s11=lines1.find('<U=')
        if s11 != -1:
            s11+=3
            e11=lines1.find('>',s11)
            valuev=string.atof(lines1[s11:e11])
            if valuev<500:
                VOL.append(valuev)
            else :VOL.append(0)
            
        s12=lines1.find('<I=')
        if s12 != -1:
            s12+=3
            e12=lines1.find('>',s12)
            valuei=string.atof(lines1[s12:e12])
            if valuei<500 and valuev<500:
                CUR.append(valuei)
                UI.append(valuev*valuei)
            else :
                CUR.append(0)
                UI.append(0)

        s14=lines1.find('<RARMS=')
        if s14!=-1:
            s14+=7
            e14=lines1.find('>',s14)
            value=string.atof(lines1[s14:e14])
            RARMS.append(value)
        else:
            RARMS.append(0)

        s14=lines1.find('<DECRMS=')
        if s14!=-1:
            s14+=8
            e14=lines1.find('>',s14)
            value=string.atof(lines1[s14:e14])
            DECRMS.append(value)
        else:
            DECRMS.append(0)
        
        valuec=0
        s16=lines1.find('<DrvRA1Cur=')
        if s16!=-1:
            s16+=11
            e16=lines1.find('>',s16)
            valuec=string.atof(lines1[s16:e16])
            DrvRA1Cur.append(valuec)
                            
        valuec=0
        s17=lines1.find('<DrvRA2Cur=')
        if s17!=-1:
            s17+=11
            e17=lines1.find('>',s17)
            valuec=string.atof(lines1[s17:e17])
            DrvRA2Cur.append(valuec)
                
        valuec=0
        s18=lines1.find('<DrvDEC1Cur=')
        if s18!=-1:
            s18+=12
            e18=lines1.find('>',s18)
            valuec=string.atof(lines1[s18:e18])
            DrvDEC1Cur.append(valuec)
                                                                                    
        valuec=0
        s19=lines1.find('<DrvDEC2Cur=')
        if s19!=-1:
            s19+=12
            e19=lines1.find('>',s19)
            valuec=string.atof(lines1[s19:e19])
            DrvDEC2Cur.append(valuec)


        s00=lines1.find('<INFO=OK>')
        if s00!=-1:
            INFO.append(0)
        elif lines1.find('<INFO=ERROR><ERR=CMD>')!=-1 :
            INFO.append(1)
        elif lines1.find('<INFO=ERROR><ERR=RANGE>')!=-1 :
            INFO.append(2)
        elif lines1.find('<INFO=ERROR><ERR=LMT><TYPE=RAZ>')!=-1 :
            INFO.append(3)
        elif lines1.find('<INFO=ERROR><ERR=LMT><TYPE=RAF>')!=-1 :
            INFO.append(4)
        elif lines1.find('<INFO=ERROR><ERR=LMT><TYPE=DECZ>')!=-1 :
            INFO.append(5)
        elif lines1.find('<INFO=ERROR><ERR=LMT><TYPE=DECF>')!=-1 :
            INFO.append(6)           
        elif lines1.find('<INFO=ERROR><ERR=CMD>')!=-1 :
            INFO.append(7)
        elif lines1.find('<INFO=ERROR><ERR=UMAC>')!=-1 :
            INFO.append(8)
        elif lines1.find('<INFO=ERROR><ERR=PORT>')!=-1 :
            INFO.append(9)            
        elif lines1.find('<INFO=ERROR><ERR=FOLERR><ERRTYPE=RA>')!=-1 :
            INFO.append(10)
        elif lines1.find('<INFO=ERROR><ERR=FOLERR><ERRTYPE=DEC>')!=-1 :
            INFO.append(11)
        elif lines1.find('<INFO=ERROR><ERR=FOLERR><TYPE=RA>')!=-1 :
            INFO.append(10)
        elif lines1.find('<INFO=ERROR><ERR=FOLERR><TYPE=DEC>')!=-1 :
            INFO.append(11)            
        elif lines1.find('<INFO=ERROR><ERR=PLCNSTART>')!=-1 :
            INFO.append(12)
        elif lines1.find('<INFO=ERROR><ERR=OVERVI>')!=-1 :
            INFO.append(13)
        elif lines1.find('<INFO=ERROR><ERR=DRIVEERR>')!=-1 :
            INFO.append(14)
        elif lines1.find('<INFO=ERROR><ERR=SOFTWARE>')!=-1 :
            INFO.append(15)
        elif lines1.find('<INFO=ERROR><ERR=BREAK>')!=-1 :
            INFO.append(16)           
        elif lines1.find('<INFO=ERROR><ERR=TIMEOUT>')!=-1 :
            INFO.append(17)
        elif lines1.find('<INFO=ERROR><ERR=NotHomed>')!=-1 :
            INFO.append(18) 

            
        s13=lines1.find('SENDTIME')
        if s13 != -1:
            s13+=9
            e13=lines1.find('>',s13)
            timestr0 = lines1[s13:e13]
            timestr1=timestr0[0:19]
            timestr2=timestr0[20:]
            millsec=string.atof(timestr2)/1000.
            sendtimeID2.append(time.mktime(time.strptime(timestr1,AST2TimeFormat))+millsec+8*3600)


        s14=lines1.find('<ERR=FOLERR><ERRTYPE=DEC>')
        if s14 != -1:
            DECFolErrST.append(time.mktime(time.strptime(timestr1,AST2TimeFormat))+millsec+8*3600)
            s14=lines1.find('<ENCRA=')
            if s14 != -1:
                s14 += 7
                e14 = lines1.find('>',s14)
                value=string.atof(lines1[s14:e14])
                DECFolErrENCRA.append(value)
        
            s14=lines1.find('<ENCDEC=')
            if s14 != -1:
                s14 += 8
                e14 = lines1.find('>',s14)
                value=string.atof(lines1[s14:e14])
                DECFolErrENCDEC.append(value)
        
        
        s14=lines1.find('<ERR=FOLERR><ERRTYPE=RA>')
        if s14 != -1:
            RAFolErrST.append(time.mktime(time.strptime(timestr1,AST2TimeFormat))+millsec+8*3600)
            s14=lines1.find('<ENCRA=')
            if s14 != -1:
                s14 += 7
                e14 = lines1.find('>',s14)
                value=string.atof(lines1[s14:e14])
                RAFolErrENCRA.append(value)
                
            s14=lines1.find('<ENCDEC=')
            if s14 != -1:
                s14 += 8
                e14 = lines1.find('>',s14)
                value=string.atof(lines1[s14:e14])
                RAFolErrENCDEC.append(value)

#=============end ID2======================
    if '<ID=37><INFO=OK><' in lines1:
        s0=lines1.find('<V1=')
        if s0 != -1:
            s0+=4
            e0=lines1.find('>',s0)
            value=string.atof(lines1[s0:e0])
            U24.append(value)

        s1=lines1.find('<I1=')
        if s1 != -1:
            s1+=4
            e1=lines1.find('>',s1)
            value=string.atof(lines1[s1:e1])
            I24.append(value)

        s2=lines1.find('<V2=')
        if s2 != -1:
            s2+=4
            e2=lines1.find('>',s2)
            value=string.atof(lines1[s2:e2])
            U12.append(value)

        s3=lines1.find('<I2=')
        if s3 != -1:
            s3+=4
            e3=lines1.find('>',s3)
            value=string.atof(lines1[s3:e3])
            I12.append(value)

        s4=lines1.find('<V3=')
        if s4 != -1:
            s4+=4
            e4=lines1.find('>',s4)
            value=string.atof(lines1[s4:e4])
            U10.append(value)

        s5=lines1.find('<I3=')
        if s5 != -1:
            s5+=4
            e5=lines1.find('>',s5)
            value=string.atof(lines1[s5:e5])
            I10.append(value)

        s6=lines1.find('<V4=')
        if s6 != -1:
            s6+=4
            e6=lines1.find('>',s6)
            value=string.atof(lines1[s6:e6])
            U5.append(value)
        
        s7=lines1.find('<V5=')
        if s7 != -1:
            s7+=4
            e7=lines1.find('>',s7)
            value=string.atof(lines1[s7:e7])
            U6.append(value)

        s13=lines1.find('SENDTIME')
        if s13 != -1:
            s13+=9
            e13=lines1.find('>',s13)
            timestr0 = lines1[s13:e13]
            timestr1=timestr0[0:19]
            timestr2=timestr0[20:]
            millsec=string.atof(timestr2)/1000.
            sendtimeID37.append(time.mktime(time.strptime(timestr1,AST2TimeFormat))+millsec+8*3600)
#=============end ID37=================
    if '<ID=42><INFO=OK><' in lines1:
        s0=lines1.find('<PwrBox=')
        if s0 != -1:
            s0+=8
            e0=lines1.find('>',s0)
            value=string.atof(lines1[s0:e0])
            PWRBOX.append(value)

        s1=lines1.find('<Grad0m=')
        if s1 != -1:
            s1+=8
            e1=lines1.find('>',s1)
            value=string.atof(lines1[s1:e1])
            GRAD0M.append(value)

        s2=lines1.find('<Grad1m=')
        if s2 != -1:
            s2+=8
            e2=lines1.find('>',s2)
            value=string.atof(lines1[s2:e2])
            GRAD1M.append(value)
        
        s3=lines1.find('<Grad2m=')
        if s3 != -1:
            s3+=8
            e3=lines1.find('>',s3)
            value=string.atof(lines1[s3:e3])
            GRAD2M.append(value)
        
        s4=lines1.find('<Grad3m=')
        if s4 != -1:
            s4+=8
            e4=lines1.find('>',s4)
            value=string.atof(lines1[s4:e4])
            GRAD3M.append(value)
        
        s5=lines1.find('<Grad4m=')
        if s5 != -1:
            s5+=8
            e5=lines1.find('>',s5)
            value=string.atof(lines1[s5:e5])
            GRAD4M.append(value)

        s13=lines1.find('SENDTIME')
        if s13 != -1:
            s13+=9
            e13=lines1.find('>',s13)
            timestr0 = lines1[s13:e13]
            timestr1=timestr0[0:19]
            timestr2=timestr0[20:]
            millsec=string.atof(timestr2)/1000.
            sendtimeID42.append(time.mktime(time.strptime(timestr1,AST2TimeFormat))+millsec+8*3600)
#===============end ID42=======================
flog.close()
print "lines="
print cc
print "len ID42"
print len(sendtimeID42)
print len(PWRBOX)
print len(GRAD0M)
conn=sqlite3.connect('TeleAST32.db')
curs=conn.cursor()

for i in range(len(sendtimeID2)) :
    params=(float(sendtimeID2[i]),ENCRA[i],ENCDEC[i],Pos[i],LVDT[i],\
            TRA1[i],TRA2[i],TDEC1[i],TDEC2[i],TMR1[i],TMR2[i],TMR3[i],TAM[i],TCCD1[i],TCCD2[i],\
            VOL[i],CUR[i],UI[i],RARMS[i],DECRMS[i],\
            DrvRA1Cur[i],DrvRA2Cur[i],DrvDEC1Cur[i],DrvDEC2Cur[i],INFO[i])
    curs.execute("INSERT INTO TeleID2 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",params)

for i in range(len(sendtimeID37)) :
    params=(float(sendtimeID37[i]),U24[i],I24[i],U12[i],I12[i],U10[i],I10[i],U5[i],U6[i])
    curs.execute("INSERT INTO TeleID37 VALUES (?,?,?,?,?,?,?,?,?)",params)

for i in range(len(sendtimeID42)-1) :
    params=(float(sendtimeID42[i]),PWRBOX[i],GRAD0M[i],GRAD1M[i],GRAD2M[i],GRAD3M[i],GRAD4M[i])
    curs.execute("INSERT INTO TeleID42 VALUES (?,?,?,?,?,?,?)",params)

conn.commit()
conn.close()
