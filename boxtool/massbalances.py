"""
Created on Sat Nov  8 20:24:32 2025

@author: sergi
"""

"""
Libraries
"""

import os
import pandas as pd
import numpy as np

"""
Beautiful code
"""
os.system('cls' if os.name == 'nt' else 'clear')

"""
Code
"""

def massbalance(unit,df_table_ID,df_table_balance):
    #unit str
    streams_number=list(df_table_ID.shape)[1]
    signs=[]
    streams=[]
    for i in range(streams_number):
        if df_table_ID.iloc[0,i]==df_table_ID.iloc[1,i]:
            print('ERROR RECIRCULATION')
        elif df_table_ID.iloc[0,i]==unit:
            print('stream: ',df_table_ID.columns[i],'is an output')
            signs.append(-1)
            streams.append(df_table_balance.columns[i])
            
        elif df_table_ID.iloc[1,i]==unit:
            print('stream: ',df_table_ID.columns[i],'is an input')
            signs.append(1)
            streams.append(df_table_balance.columns[i])
        else:
            print('stream: ',df_table_ID.columns[i],'is not in: ',unit)
    #balance
    np_table=21
    np_table=np.array(df_table_balance[streams])
    np_tabla_non_nan=np_table.fill(0)
    #np_tabla_non_nan=np.nan_to_num(np_table,nan=0)
    #matriz de soluciones x+y+z=w, lo que significa que w menos todo lo que se a la izquierda
    
    
    return  np_tabla_non_nan
