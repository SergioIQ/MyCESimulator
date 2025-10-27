# MyCESimulator Intro
## Legal
Copyright (c) 2025 SERGIO GONZALEZ RODRIGUEZ
(ES)
Todos los derechos reservados.

Este repositorio se publica únicamente con fines de visualización. 
No se permite el uso, copia, modificación o redistribución del contenido sin autorización expresa por escrito del autor.
(EN)
All rights reserved.

This repository is published for viewing purposes 
Use, copying, modification, or redistribution of the content is prohibited without express written permission from the author.
## Mission and motivation
A repository with libraries and solved problems of Chemical engineering (CE) 

- Practise Python and their libraries
- Practise Git and documentation
- Review and increase concepts of CE
- Show my skills to interested parties


## Step of the project 
Currently I am designning class, objects and methods to solve basic problems. Goals during this step are:
- Design basic objet to solve mass balances in simple problems (no reactions, mass energy, mixer and heater) and identify the type of problem (optimization, no solution, solution).
- Get resoults in dataframes with a standar structure.
- The use and managment of dataframes will belong to methods of the basic objects.  



# Nomenclature of files
## Problems
XXX-*-MEDO-EA-N-YYY
- XXX  :Number of unitary operation (UO)
  1-MIXER
  2-DIVIDER
  3-HEATER
  4-EVAPOTOR
  5-CRYSTALLIZER
- '*'  :In case of different kinds of UOs the number of the UO
- M    :(0/1) include mass balance?     (YES/NO)
- E    :(0/1) include ENERGY balance?   (YES/NO)
- D    :(0/1) include Design?           (YES/NO)
- O    :(0/1) include Optimization?     (YES/NO)
- E    :(0/1) include mass balance?     (YES/NO)
- A    :(0/1) include mass balance?     (YES/NO)
- N    :Number of compounds (water, hydrogen...)
- YYY  :In case of same code, number of the problem (1,2,3...)

# Objects
I am designning so
## Streams
---properties
Conditions (T and P) 
  Only one can be choosen
Mixture (Compounds)
  Units (kg/h,g...)

  
Way (origin and destiny) *if it comes/goes from or to the outside=0
Properties (Diameter,lenght, material...)
Control and equimments (valvule, sensor...)
---methods
Starting

## Compounds
---properties
density, molecular weight, cost...
---methods
No methods for the moment
## Equipment
---properties
No properties for the moment
---methods
No methods for the moment


## Table of mass and energy balance
A mass balance table is a collection of streams + totals 
* In future steps it will also include equipments conditions
- class
(two tables, % and mass)
<img width="1237" height="394" alt="image" src="https://github.com/user-attachments/assets/f785ce90-9603-4334-9523-9f1f2a5d8d37" />


| INDEX\COLUMNS  | PROP | IN-1  | IN-X  | OU-1  | OU-X  |
| :--------------| :--: | ----: |----:  |----:  |----:  |
| H2O            | Unit | NaN   | NaN   | NaN   | NaN   |
| NH3            | Unit | NaN   | NaN   | NaN   | NaN   |
| H2S            | Unit | NaN   | NaN   | NaN   | NaN   |
| H2S            | Unit | NaN   | NaN   | NaN   | NaN   |
 
