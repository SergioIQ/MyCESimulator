# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 12:31:20 2025

@author: sergi
"""

"""
Libraries
"""

import os
import pandas as pd
import numpy as np

from streamsv2 import NewStream
"""
Beautiful code
"""
os.system('cls' if os.name == 'nt' else 'clear')

"""
Code
"""

'mixture'
mixture=['water','solt']

'A'
name='A'
origin='0'
destiny='Evaporator'
A=NewStream(name, origin, destiny)

'A-values'
compounds_comp=[95/100,5/100]
flow=10000
A.chem_comp(mixture, compounds_comp, flow)

'B'
name='B'
origin='Evaporator'
destiny='0'
B=NewStream(name, origin, destiny)

'B-values'
compounds_comp=[1,0]
flow=np.nan
B.chem_comp(mixture, compounds_comp, flow)

'C'
name='C'
origin='Evaporator'
destiny='0'
C=NewStream(name, origin, destiny)

'B-values'
compounds_comp=[70/100,30/100]
flow=np.nan
C.chem_comp(mixture, compounds_comp, flow)

'Table'
''''
-----axis=0&1-----
axis=0, ignore index, long table
axis=1, add data in same index, rectangular table
'''
df_table_ID=pd.concat([A.df_description,B.df_description,C.df_description],axis=1)#para indix havia falta una lita no un objeto
print(df_table_ID)
