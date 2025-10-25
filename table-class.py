import pandas as pd
import numpy as np

class Table_Balancesv2:
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
    def __init__(self,inps, outs, compounds,):
        prop='prop-'
        
        flow='flow' #copy paste to avoid writing mistakes
        self.inps=inps
        self.outs=outs
        self.compounds=compounds.insert(0, prop+'columns')
        self.streams=[prop+'rows']
        

        simbols=[0]
        for i in range(self.inps):
            self.streams.append('IN-'+str(i+1))
            simbols.append(1)
        for i in range(self.outs):
            self.streams.append('OU-'+str(i+1))
            simbols.append(-1)
        
        self.MB=pd.DataFrame(columns=self.streams, index=compounds)  # Fixed: changed prop to compounds based on function parameters
        self.MB.loc[compounds[0]]=simbols
        
    def unknown_v(self):
        #useful to calculate freedom degrees
        unkowns=self.MB.isna().sum().sum()
        print(f'There are {unkowns} variables without value')
    def prop_compounds(self,row,p):
        #row is the name of the index (use compunds[])
        #p is a string (kg, %....)
        #useful to calculate freedom degrees
        self.MB.loc[row,'prop-rows']=p
    def show(self):
        #row is the name of the index (use MB.index[x])
        #p is a string (kg, %....)
        #useful to calculate freedom degrees
        print(self.MB)
    def show_all(self):
        #row is the name of the index (use MB.index[x])
        #p is a string (kg, %....)
        #useful to calculate freedom degrees
        print(self.inps)
        print(self.outs)
        print(self.compounds)
        print(self.MB)
        print(self.streams)
    def matrix_mb(self,materials):
        self.materials=materials
        for i in self.streams:
            for j in self.materials:
            #self.MB.iloc[i+1]=self.MB[i]*self.MB.loc['prop-columns',i]
                self.MB.loc[j,i]=self.MB.loc[j,i]*self.MB.loc['prop-columns',i]
            

    
flow='flow'
materials=['H2O','H2','CO2']
compounds=materials.copy()
compounds.append(flow)
Table=Table_Balancesv2(2, 2, compounds)
Table.unknown_v()
Table.matrix_mb(materials)
Table.MB.iloc[0,0]=0
Table.MB.iloc[1,1]=1
Table.MB.iloc[2,2]=2
Table.MB.iloc[3,3]=3
Table.MB.iloc[4,4]=4
MB=Table.MB
print(MB)
print(MB.iloc[1,:])
print(MB.iloc[:,4]*MB.iloc[0,4])
print(MB.loc[:,Table.streams[2]])
print(MB.loc[:,Table.streams[3]]*MB.loc['prop-columns',Table.streams[3]])
print(Table.streams)

Table.matrix_mb(materials)
MB2=Table.MB
print(MB2)

#ALTERNATIV MAS RAPIDA QUE AUN NO SE IMPLEMENTAR
A=MB2.iloc[0,:]
print(MB2)
print(A)
print(MB2.iloc[3,:]*A)
print(MB2.iloc[3,:]*A)
