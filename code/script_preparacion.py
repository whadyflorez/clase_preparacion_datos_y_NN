import pandas as pd
import numpy as np

# 1. Crear un dataset sintético con problemas de escala y outliers
data = {
    'Horas_Operacion': [10, 12, 11, 15, 9, 13, 100, 11], # El 100 es un outlier
    'RPM_Motor': [1500, 1600, 1550, 1700, 1480, 1620, 1580, 1510], # Escala alta
    'Consumo_KW': [25, 28, 26, 32, 22, 30, 29, 24] # Variable objetivo
}

df = pd.DataFrame(data)
print("--- Dataset Original ---")
print(df)

# ==========================================
# A. DETECCIÓN Y TRATAMIENTO DE OUTLIERS (IQR)
# ==========================================
Q1 = df['Horas_Operacion'].quantile(0.25)
Q3 = df['Horas_Operacion'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrar el dataframe para eliminar el outlier
df_limpio = df[(df['Horas_Operacion'] >= limite_inferior) & (df['Horas_Operacion'] <= limite_superior)].copy()

print("\n--- Dataset sin Outliers ---")
print(df_limpio)

# ==========================================
# B. ESCALAMIENTO MIN-MAX [0, 1]
# ==========================================
min_rpm = df_limpio['RPM_Motor'].min()
max_rpm = df_limpio['RPM_Motor'].max()

df_limpio['RPM_Escalado'] = (df_limpio['RPM_Motor'] - min_rpm) / (max_rpm - min_rpm)
print("\n--- Con RPM Escalado (0 a 1) ---")
print(df_limpio[['RPM_Motor', 'RPM_Escalado']])

# ==========================================
# C. ESTANDARIZACIÓN (Z-SCORE)
# ==========================================
media_horas = df_limpio['Horas_Operacion'].mean()
std_horas = df_limpio['Horas_Operacion'].std()

df_limpio['Horas_Estandarizado'] = (df_limpio['Horas_Operacion'] - media_horas) / std_horas
print("\n--- Con Horas Estandarizadas ---")
print(df_limpio[['Horas_Operacion', 'Horas_Estandarizado']])
