# MyCESimulator Intro
## Mission
A repository with libraries and solved problems of Chemical engineering (CE) 

## MOTIVATION
- Practise Python and their libraries
- Practise Git and documentation
- Review and increase concepts of CE
- Show my skills to interested parties

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

## Table of mass and energy balance

- class
(two tables, % and mass)

| INDEX\COLUMNS  | PROP | IN-1  | IN-X  | OU-1  | OU-X  |
| :--------------| :--: | ----: |----:  |----:  |----:  |
| PROP           |   0  | Phase | Phase | Phase | Phase |
| H2O            | Unit | NaN   | NaN   | NaN   | NaN   |
| NH3            | Unit | NaN   | NaN   | NaN   | NaN   |
| H2S            | Unit | NaN   | NaN   | NaN   | NaN   |
| H2S            | Unit | NaN   | NaN   | NaN   | NaN   |
 
