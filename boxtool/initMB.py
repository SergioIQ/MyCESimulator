import pandas as pd
import numpy as np

class Table_Balances:
    '''
    Description
    Create a dataframe with columns with the name of inputs and outputs and index with studied properties
    inps and outs are numbers while prop is a list with strs
    ---___---
    Instructions of class:
    inps=number, streams which go to the unit
    outs=number, streams which go to the unit
    compounds=list, names of arrroys
    ---___---
    Notes
    The arroy flow will be always include, variable flow is the total flow of a columns
    #Mass balance without Q and without R has C indipendent
    #liberty freedom (C*(S-1))
    #La fila de totales debe incluirse por lo que debo quitarle 1 adicional a los calculos de grados de libertad
    #De momento la matriz debe mostrar los caucales masicos de cada compuesto, ya que mezclar composiciones y caudales complica la automatizacion de la resolucion
    '''
    def __init__(self,inps, outs, compounds):
        self.inps=inps
        self.outs=outs
        self.compounds=compounds
        flow='flow' #copy paste to avoid writing mistakes
        streams=[]
        for i in range(self.inps):
            streams.append('IN-'+str(i+1))
        for i in range(self.outs):
            streams.append('OU-'+str(i+1))
        self.MB=pd.DataFrame(columns=streams, index=compounds)  # Fixed: changed prop to compounds based on function parameters
    
    def unknown_v(self):
        #useful to calculate freedom degrees
        unkowns=self.MB.isna().sum().sum()
        print(f'There are {unkowns} variables without value')
    
flow='flow'
compounds=['H2O','H2','CO2',flow]
Table=Table_Balances(2, 2, compounds)
MB=Table.MB
print(Table.unknown_v())
