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

# Obtener análisis descriptivo de variables numéricas para todos los pacientes
description = data.describe()

# Obtener análisis descriptivo de variables numéricas por grupo
grouped_description = data.groupby('grupo_x').describe()

# Crear gráfico de barras para la frecuencia de cada grupo y categoría Bethesda
palette = 'Paired'
ax1 = sns.countplot(x='grupo_x', data=data, palette=palette)
ax1.set_title("Pacientes por grupo")
ax1.set_xlabel("Grupo")
ax1.set_ylabel("Frecuencia")

# Agregar etiquetas de frecuencia en las barras
for p in ax1.patches:
    ax1.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='baseline', fontsize=8, color='black', xytext=(0, 3),
                 textcoords='offset points')

plt.show()

# Crear el gráfico de barras para 'bethesda_x'
ax2 = sns.countplot(x='bethesda_x', data=data, palette=palette)
ax2.set_title("Pacientes por categoría Bethesda")
ax2.set_xlabel("Categoría Bethesda")
ax2.set_ylabel("Frecuencia")

# Agregar etiquetas de frecuencia en las barras
for p in ax2.patches:
    ax2.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='baseline', fontsize=8, color='black', xytext=(0, 3),
                 textcoords='offset points')

plt.show()

