#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:50:35 2024
@author: andreaross

Script para el analisis descriptivo de los datos de pacientes con nódulo 
tiroideo. El archivo de entrada es un merge de datos clinicos, de ultrasonido
y moleculares.

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
data = pd.read_excel('thyroid_merged.xlsx')
print(data.head())