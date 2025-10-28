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


## Step of the project :
Currently step
- Mass balance

Future steps

- Energy balance
- Equipment Design
- Control
- Optimization


# Nomenclature of files
CE problems share Units operations and also type of problems (mass balance, energy balance, equipment design, optimizacion, control, economic and ambiental)
These problems have unlimited posibilities due to the quantity of compounds
Each solved problem will have two types of tags
- unitary operations (in case of more than one)
- compounds (CAS NUMBER of each compound)

## Problems
XXX-*-MEDOC-EA-N-YYY
- XXX  :Number of unitary operation (UO)
  1-MIXER
  2-DIVIDER
  3-HEATER
  4-EVAPOTOR
  5-CRYSTALLIZER
  ...
- '*'  :In case of different kinds of UOs the number of the UO
- M    :(0/1) include mass balance?     (YES/NO)
- E    :(0/1) include ENERGY balance?   (YES/NO)
- D    :(0/1) include Design?           (YES/NO)
- O    :(0/1) include Optimization?     (YES/NO)
- C    :(0/1) control problem?          (YES/NO)
- E    :(0/1) economic problem?          (YES/NO)
- A    :(0/1) ambiental balance?     (YES/NO)
- YYY  :In case of same code, number of the problem (1,2,3...)

# Objects
## Streams
currently:

<img width="353" height="837" alt="image" src="https://github.com/user-attachments/assets/d8881807-138b-4982-b925-26281fd0a201" />

<img width="353" height="229" alt="image" src="https://github.com/user-attachments/assets/7e99b8a4-4b6a-4e01-88bb-a67da63e0cda" />

<img width="353" height="343" alt="image" src="https://github.com/user-attachments/assets/a3b5a845-33ef-43e9-a0cb-466fce4547d4" />

*Design method is empy
*Energy methods don't calculate things only introduce values (It will be update during Energy balance step)

## Compounds
---properties
Each compund shoud have it's own database and method to introduce them
---methods
No methods for the moment
## Equipment
---properties
No properties for the moment
---methods
No methods for the moment


## Mass balance table
A mass balance is a function which use a collection of streams to create a table
This table will have methods to solve the mass balance
- class
(two tables, % and mass)

type:
- 1 = input
- -1= output
| INDEX\COLUMNS  | Name1 | Name2 | Name3 | Name4 |
| :--------------| ----: |----:  |----:  |----:  |
| type           | 1     | 1     | 1     | -1    |
| H2O            | NaN   | NaN   | NaN   | NaN   |
| NH3            | NaN   | NaN   | NaN   | NaN   |
| H2S            | NaN   | NaN   | NaN   | NaN   |
| H2S            | NaN   | NaN   | NaN   | NaN   |
 
