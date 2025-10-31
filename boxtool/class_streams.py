# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 22:51:25 2025

@author: sergi
"""

"""
creation=10/28/2025
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

class NewStream:
    '''
    df_description is the minimun requiered to identidy a stream
    df_chem is the requiered data to calculate mass and energy balance (MB&EB)
    '''
    def __init__(self,name,origin,destiny):
        '''
        It is necesary to know the origin and deestiny to make mass balance in equipments
        It is necesary a unniq name to identidy streams
        '''
        
        'Streams info'
        self.name=name                                                                      #str
        self.origin=origin                                                                  #str
        self.destiny=destiny                                                                #str
        
        'Table creation'
        self.df_description=pd.DataFrame([self.origin,self.destiny],['origin','destiny'])   #dataframe
        self.df_description.rename(columns={0: self.name}, inplace=True)                    #!Rename column name!
        
        'Show table'
        print(self.df_description)                                                          #show resoults
        
    def chem_mass(self,mixture,compounds_mass):
        '''
        With the individual flow of each compound composition and mass flow is calculated
        ---If a properties is unkown use NaN value---
        '''
        
        'Mass info'
        '---Method copy is NECESARY to avoid cross information---'
        self.mixture=mixture.copy()                                                         #list,str
        self.compounds_mass=compounds_mass .copy()                                          #list,ints/floats
        
        'Creation of index'
        for i in range(len(mixture)):
            self.mixture.append(self.mixture[i]+'%')                                        #List,str+ compositions                      
        self.mixture.append('total')                                                        #List,str+ total
        self.df_chem=pd.DataFrame(columns=['data'], index=self.mixture)                     #Dataframe

        'Mass data and calculation'
        for i in range(len(mixture)):
            self.df_chem.loc[self.mixture[i]]=self.compounds_mass[i]                        #List,ints/float, introduce know mass flows
        'Total flow'
        self.df_chem.loc['total']=sum(self.compounds_mass)                                  #List,ints/float, calculate total flow
        'Compositions'
        self.compounds_comp=np.array(self.compounds_mass)/self.df_chem.loc['total','data']  #Array,ints/float, calculate compositions
        for i in range(len(mixture)):
            self.df_chem.loc[self.mixture[len(mixture)+i]]=self.compounds_comp[i]           #List,ints/float, introduce calculated values
        'report'
        print(self.df_chem)                                                                 #show resoults
        
    def chem_comp(self,mixture,compounds_comp,flow):
        '''
        With the individual composition and mass flow is individual flows are calculate 
        ---If a properties is unkown use NaN value---
        '''
        'Mass info'
        '---Method copy is NECESARY to avoid cross information---'
        self.mixture=mixture.copy()                                                         #list,str
        self.compounds_comp=compounds_comp .copy()                                          #list,ints/floats
        
        'Creation of index'
        for i in range(len(mixture)):
            self.mixture.append(self.mixture[i]+'%')                                        #List,str+ compositions                      
        self.mixture.append('total')                                                        #List,str+ total
        self.df_chem=pd.DataFrame(columns=['data'], index=self.mixture)                     #Dataframe
        
        'Mass data and calculation'
        'compositions'
        for i in range(len(mixture)):
            self.df_chem.loc[self.mixture[len(mixture)+i]]=self.compounds_comp[i]           #List,ints/float, introduce know compositions
        'Total flow'
        self.df_chem.loc['total','data']=flow                                               #List,ints/float, introduce know total flow
        'Mass'
        self.compounds_mass=np.array(self.compounds_comp)*self.df_chem.loc['total','data']  #List,ints/float, calculate mass flows
        for i in range(len(mixture)):
            self.df_chem.loc[self.mixture[i]]=self.compounds_mass[i]                        #List,ints/float, introduce calculated mass flows
            
        'report'
        print(self.df_chem)                                                                 #show resoults
 
    
    def design(self,unitsTP,P,V):
        'Pipping design'
        print('future update')
    def show_all(self):
        #row is the name of the index (use MB.index[x])
        #p is a string (kg, %....)
        #useful to calculate freedom degrees
        print('basic info----\n',self.df_description)
        print('composition----\n',self.df_chem)
        
        
#Example
print('Example of use')
#Values of stream S_1
s_1_name='s_1'
s_1_origin='0'
s_1_destiny='U1'
mixture=['A','B','C']
s_1_units=['Kg','Kg','Kg']
s_1_mass=[10,np.nan,5]
comp=[0.285714,0.571429,np.nan]
s_1_T=10
s_1_P=10
s_1_unitsTP=['c','atm']
##Creation of  S_1
s_1=NewStream(s_1_name, s_1_origin, s_1_destiny)
## S_1 methods
#s_1.chem_mass(s_1_mixture, s_1_values)
'''
Solved, Make it looks beautiful and comment
More clear sintasix, after it, decide start with evaporator A1. 

'''
'Examples of use'
s_1=NewStream(s_1_name, s_1_origin, s_1_destiny)
s_1.chem_mass(mixture, s_1_mass)
s_1.chem_comp(mixture, comp, 35)
s_1.design(1, 1, 1)
s_1.show_all()
