import pandas as pd
import numpy as np

def initMB(inps, outs, compounds):
    #compounds is a list
    flow='flow' #copy paste to avoid writing mistakes
    """Create a dataframe with columns with the name of inputs and outputs and index with studied properties
     inps and outs are numbers while prop is a list with strs"""
    #Mass balance without Q and without R has C indipendent
    #liberty freedom (C*(S-1))
    #La fila de totales debe incluirse por lo que debo quitarle 1 adicional a los calculos de grados de libertad
    #De momento la matriz debe mostrar los caucales masicos de cada compuesto, ya que mezclar composiciones y caudales complica la automatizacion de la resolucion
    '''En el futuro crear una funcion que cree la analoga de composiciones'''
    streams=[]
    for i in range(inps):
        streams.append('IN-'+str(i+1))
    for i in range(outs):
        streams.append('OU-'+str(i+1))
    MB=pd.DataFrame(columns=streams, index=compounds)  # Fixed: changed prop to compounds based on function parameters
    return MB
flow='flow'
compounds=['H2O','H2','CO2',flow]
MB=initMB(2, 2, compounds)
