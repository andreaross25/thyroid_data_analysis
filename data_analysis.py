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

palette = 'Paired'
numericas = ['edad', 'edad_dx_px', 'peso_kg', 'altura_cm', 'IMC', 'numero', 'volumen_cc', 'CLDN1 LOG', 'TIMP1 LOG', 'KRT19 LOG']
categoricas = ['braf', 'A', 'T', 'sexo', 'localizacion', 'origen_paciente', 'escolaridad', 'oficio_profesion', 
               'enfermedades_respiratorias', 'enfermedad_tiroidea', 'tabaquismo', 'alcoholismo', 'radiografias',
               'resonancias', 'tomografias', 'mastografias', 'radioterapia', 'yodo_radiactivo', 'terapias_hormonales',
               'acido_folico', 'calcio', 'cancer_previo_px', 'cancer_familiar_1', 'numero', 'distribucion', 'localizacion',
               'composicion', 'forma', 'bordes_margen', 'ecogenicidad', 'artefactos_ecogenicos', 'elastografia',
               'vascularidad', 'ganglios', 'tirads', 'microcarcinomas', 'IMC Categorico']

# Crear gráfico de barras para la frecuencia de cada grupo y categoría Bethesda
ax1 = sns.countplot(x='grupo', data=data, palette=palette)
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
ax2 = sns.countplot(x='bethesda', data=data, palette=palette)
ax2.set_title("Pacientes por categoría Bethesda")
ax2.set_xlabel("Categoría Bethesda")
ax2.set_ylabel("Frecuencia")

# Agregar etiquetas de frecuencia en las barras
for p in ax2.patches:
    ax2.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='baseline', fontsize=8, color='black', xytext=(0, 3),
                 textcoords='offset points')

plt.show()


def analisis_categoricas():
    for col in categoricas:
        # Filtrar los valores que no sean 'REPORTE PENDIENTE'
        filtered_data = data[data[col] != 'REPORTE PENDIENTE']

        print(f"\nAnálisis de la columna: {col}")
        freq_abs = data[col].value_counts(dropna=True)  # Frecuencia absoluta
        freq_rel = data[col].value_counts(normalize=True, dropna=True) * 100  # Frecuencia relativa
        analysis = pd.DataFrame({'Frecuencia': freq_abs, 'Porcentaje (%)': freq_rel})
        print(analysis)

    # Crear los gráficos

        plt.figure(figsize=(8, 4))
        ax = sns.countplot(x=col, data=filtered_data, order=filtered_data[col].value_counts().index, palette=palette)
        
        # Añadir las etiquetas con la frecuencia en la parte superior de las barras
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='baseline', fontsize=8, color='black', 
                        xytext=(0, 5), textcoords='offset points')
        
        # Títulos y etiquetas
        plt.title(col)
        plt.ylabel("Frecuencia")
        plt.xlabel(col)
        plt.xticks(rotation=0)
        plt.show()

def analisis_categoricas_grouped(data, grupo_col):
    for col in categoricas:
        # Filtrar los valores que no sean 'REPORTE PENDIENTE'
        filtered_data = data[data[col] != 'REPORTE PENDIENTE']

        print(f"\nAnálisis de la columna: {col}")
        
        # Agrupando por grupo y calculando frecuencias
        freq_abs = filtered_data.groupby(grupo_col)[col].value_counts().unstack(fill_value=0)  # Frecuencia absoluta
        freq_rel = (filtered_data.groupby(grupo_col)[col].value_counts(normalize=True)
                     .unstack(fill_value=0) * 100)  # Frecuencia relativa
        
        # Imprimir análisis
        print("Frecuencia Absoluta:")
        print(freq_abs)
        print("\nPorcentaje (%):")
        print(freq_rel)

        # Graficar frecuencias absolutas
        freq_abs.plot(kind='bar', stacked=True, figsize=(10, 6), colormap=palette, palette=palette)
        plt.title(f'Distribución de {col} por {grupo_col}')
        plt.ylabel("Frecuencia")
        plt.xlabel(grupo_col)
        plt.xticks(rotation=45)
        plt.legend(title=col, bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

analisis_categoricas_grouped(data, 'grupo')
