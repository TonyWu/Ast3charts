#! /usr/bin/env python
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.dates import AutoDateLocator,DateFormatter
import string
import time
import dateutil,pylab,random
from pylab import *

conn=sqlite3.connect('TeleAST32.db')
curs=conn.cursor()

curs.execute('CREATE TABLE TeleID2 \
(SENDTIME FLOAT PRIMARY KEY UNIQUE, \
ENCRA FLOAT, ENCDEC FLOAT, \
Pos FLOAT,LVDT FLOAT,\
TRA1 FLOAT, TRA2 FLOAT, TDEC1 FLOAT, TDEC2 FLOAT, TMR1 FLOAT,TMR2 FLOAT, TMR3 FLOAT, TAM FLOAT, TCCD1 FLOAT, TCCD2 FLOAT,\
VOL FLOAT, CUR FLOAT, UI FLOAT,\
RARMS FLOAT, DECRMS FLOAT,\
DrvRA1Cur FLOAT, DrvRA2Cur FLOAT, DrvDEC1Cur FLOAT, DrvDEC2Cur FLOAT,\
INFO INTEGER)')

curs.execute('CREATE TABLE TeleID37 \
(SENDTIME FLOAT PRIMARY KEY UNIQUE, \
U24 FLOAT,I24 FLOAT,U12 FLOAT,I12 FLOAT,U10 FLOAT,I10 FLOAT,U5 FLOAT,U6 FLOAT)')


curs.execute('CREATE TABLE TeleID42 \
(SENDTIME FLOAT PRIMARY KEY UNIQUE, \
PWRBOX FLOAT,GRAD0M FLOAT, GRAD1M FLOAT, GRAD2M FLOAT, GRAD3M FLOAT, GRAD4M FLOAT)') 

conn.commit()
conn.close()
