import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurar el estilo de los gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("pastel")

# Definir rutas
ruta_excel = r"C:\Users\berbu\Documents\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\Unidad_1\Ingresantes_anonimizado.xlsx"
directorio_salida = r"C:\Users\berbu\Documents\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\Trabajo_práctico_de_evaluación_de_la_Unidad_1"

# Leer el archivo Excel
df = pd.read_excel(ruta_excel)

# Exploración inicial de los datos
print("Primeras filas del dataset:")
print(df.head())
print("\nInformación del dataset:")
print(df.info())
print("\nValores únicos por variable:")
for columna in df.columns:
    print(f"{columna}: {df[columna].nunique()} categorías")

# Análisis de las variables solicitadas
# Frecuencias absolutas y relativas para Género y Nivel Educativo
frecuencia_genero = df['Género'].value_counts()
frecuencia_educativo = df['Nivel educativo'].value_counts()

porcentaje_genero = df['Género'].value_counts(normalize=True) * 100
porcentaje_educativo = df['Nivel educativo'].value_counts(normalize=True) * 100

# Crear tabla de distribución
tabla_distribucion = pd.DataFrame({
    'Género_Frecuencia': frecuencia_genero,
    'Género_Porcentaje': porcentaje_genero,
    'Nivel_Educativo_Frecuencia': frecuencia_educativo,
    'Nivel_Educativo_Porcentaje': porcentaje_educativo
})

print("\nTabla de distribución de frecuencias:")
print(tabla_distribucion)

# Gráfico de barras para Nivel Educativo
plt.figure(figsize=(10, 6))
ax1 = sns.barplot(x=frecuencia_educativo.values, y=frecuencia_educativo.index, orient='h')
plt.title('Distribución de Nivel Educativo', fontsize=16, fontweight='bold')
plt.xlabel('Frecuencia Absoluta', fontsize=12)
plt.ylabel('Nivel Educativo', fontsize=12)

# Añadir etiquetas con los valores
for i, v in enumerate(frecuencia_educativo.values):
    plt.text(v + 0.1, i, str(v), va='center', fontweight='bold')

plt.figtext(0.95, 0.01, f"Fuente: {os.path.basename(ruta_excel)}", ha="right", fontsize=8, style='italic')
plt.tight_layout()
plt.savefig(os.path.join(directorio_salida, 'nivel_educativo.png'), dpi=300, bbox_inches='tight')
plt.show()

# Gráfico de barras para Género
plt.figure(figsize=(8, 6))
ax2 = sns.barplot(x=frecuencia_genero.values, y=frecuencia_genero.index, orient='h')
plt.title('Distribución por Género', fontsize=16, fontweight='bold')
plt.xlabel('Frecuencia Absoluta', fontsize=12)
plt.ylabel('Género', fontsize=12)

# Añadir etiquetas con los valores
for i, v in enumerate(frecuencia_genero.values):
    plt.text(v + 0.1, i, str(v), va='center', fontweight='bold')

plt.figtext(0.95, 0.01, f"Fuente: {os.path.basename(ruta_excel)}", ha="right", fontsize=8, style='italic')
plt.tight_layout()
plt.savefig(os.path.join(directorio_salida, 'genero.png'), dpi=300, bbox_inches='tight')
plt.show()

# Tabla de doble entrada (cruce de variables)
tabla_cruce = pd.crosstab(
    index=df['Género'],
    columns=df['Nivel educativo'],
    margins=True,
    margins_name='Total'
)

tabla_cruce_porcentaje = pd.crosstab(
    index=df['Género'],
    columns=df['Nivel educativo'],
    normalize='index'  # Porcentajes por fila (Género)
) * 100

print("\nTabla de cruce (frecuencias absolutas):")
print(tabla_cruce)
print("\nTabla de cruce (porcentajes por género):")
print(tabla_cruce_porcentaje.round(2))

# Guardar resultados en archivos
tabla_distribucion.to_excel(os.path.join(directorio_salida, 'distribucion_frecuencias.xlsx'))
tabla_cruce.to_excel(os.path.join(directorio_salida, 'cruce_absoluto.xlsx'))
tabla_cruce_porcentaje.to_excel(os.path.join(directorio_salida, 'cruce_porcentaje.xlsx'))

print(f"\nAnálisis completado. Resultados guardados en: {directorio_salida}")