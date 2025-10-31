"""
creation=10/28/2025
@author: sergi
"""

"""
Beautiful code
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')
"""
Code
"""

import pandas as pd
import numpy as np


class NewStream:
    '''
    Good practises
    objname=name
    '''
    def __init__(self,name,origin,destiny):
        #Stream info
        self.name=name                                                  #str
        self.origin=origin                                              #str
        self.destiny=destiny                                            #str
        #Auxiliar and Temporal table 
        description_init=['origin','destiny']                           #standar names
        description_values=[origin,destiny]                             #values
        description_df=pd.DataFrame(description_values,description_init)#table creation
        description_df.rename(columns={0: name}, inplace=True)          #!Rename column name!
        #Table creation
        self.description=description_df                                 #dataframe
        #Show table
        print(self.description)
    def mass(self,mixture,values):
        #Chemical info
        self.values=values                                              #list,ints/floats
        #Auxiliar and Temporal table 
        chem_init=['mass']                                #standar names
        df_chem=pd.DataFrame(columns=chem_init, index=mixture)          #table structure                                        
        df_chem.iloc[:,0]=values                                        #table values column 1
        #Table creation
        self.df_chem=df_chem                                            #table creation
        #Useful values
        self.massflow=sum(values) 
        self.composition=np.array(values)/self.massflow
        composition_names=[]
        for i in range(len(mixture)):
            composition_names.append(mixture[i]+'%')
            self.df_chem.loc[composition_names[i]]=self.composition[i]
        df_chem.loc['total']=self.massflow
        #Show table
        print(self.df_chem)                                             #dataframe
    def eneryTP(self,unitsTP,T,P):
        'Three cases, case TP'
        self.T=T                                                        #Temperature of the stream
        self.P=P                                                        #Pressure of the stream
        self.description.loc['T ('+unitsTP[0]+')']=T                    #Update basic info 
        self.description.loc['P ('+unitsTP[1]+')']=P                    #Update basic info               
        print(self.description)                                         #show update
    def eneryTV(self,unitsTP,T,V):
        'Three cases, case TV'
        self.T=T                                                        #Temperature of the stream
        self.V=V                                                        #Volume of the stream
        self.description.loc['T ('+unitsTP[0]+')']=T                    #Update basic info
        self.description.loc['V ('+unitsTP[1]+')']=V                    #Update basic info
        print(self.description)                                         #show update
    def eneryPV(self,unitsTP,P,V):
        'Three cases, case PV'
        self.P=P                                                        #Pressure of the stream
        self.V=V                                                        #Volume of the stream
        self.description.loc['P ('+unitsTP[0]+')']=P                    #Update basic info
        self.description.loc['V ('+unitsTP[1]+')']=V                    #Update basic info
        print(self.description)                                         #show update
    def designPV(self,unitsTP,P,V):
        'Pipping design'
        print('future update')
    def show_all(self):
        #row is the name of the index (use MB.index[x])
        #p is a string (kg, %....)
        #useful to calculate freedom degrees
        print('basic info----\n',self.description)
        print('composition----\n',self.df_chem)
#Example
print('Example of use')
#Values of stream S_1
s_1_name='s_1'
s_1_origin='0'
s_1_destiny='U1'
s_1_mixture=['A','B','C']
s_1_units=['Kg','Kg','Kg']
s_1_values=[10,20,5]
s_1_T=10
s_1_P=10
s_1_unitsTP=['c','atm']
#Creation of  S_1
s_1=NewStream(s_1_name, s_1_origin, s_1_destiny)
# S_1 methods
s_1.mass(s_1_mixture, s_1_values)
s_1.eneryTP(s_1_unitsTP, s_1_T, s_1_P)
s_1.show_all()
