import pandas as pd

# -------------------------------
# Funciones auxiliares
# -------------------------------

def crear_fila_total(frecuencia_abs, frecuencia_rel):
    """
    Recibe dos Series (frecuencia absoluta y relativa),
    calcula los totales y devuelve un DataFrame con una fila "Total".
    """
    total_abs = frecuencia_abs.sum()
    total_rel = frecuencia_rel.sum()
    return pd.DataFrame(
        {"Frecuencia absoluta": [total_abs], "Frecuencia relativa": [total_rel]},
        index=["Total"],
    )

def crear_fila_vacia():
    """
    Devuelve un DataFrame con una fila vacía,
    para dejar separación en las tablas.
    """
    return pd.DataFrame(
        {"Frecuencia absoluta": [""], "Frecuencia relativa": [""]}, index=[""]
    )

# -------------------------------
# Flujo principal
# -------------------------------

# Leer archivo original
df = pd.read_excel(
    r"C:\Users\20204041157\Documents\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\Trabajo_práctico_de_evaluación_de_la_Unidad_1\Ingresantes_anonimizado.xlsx",
    sheet_name="Educ_Genero",
)

# Extraer categorías únicas
genero = df["Género"].unique()
nivel_educativo = df["Nivel educativo"].unique()


df_genero = pd.DataFrame(genero, columns=["Género"])
df_nivel_educativo = pd.DataFrame(nivel_educativo, columns=["Nivel educativo"])

# Guardar categorías en hoja Excel
# with pd.ExcelWriter(
#     r"C:\Users\20204041157\Documents\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\Trabajo_práctico_de_evaluación_de_la_Unidad_1\Ingresantes_anonimizado.xlsx",
#     mode="a",
#     engine="openpyxl",
#     if_sheet_exists="overlay",
# ) as writer:
#     df_genero.to_excel(writer, sheet_name="Categorias", index=False, startrow=0, startcol=0)
#     df_nivel_educativo.to_excel(writer, sheet_name="Categorias", index=False, startrow=len(df_genero)+3, startcol=0)

# -------------------------------
# Tabla de frecuencias: Género
# -------------------------------
frecuencia_abs_genero = df["Género"].value_counts()
frecuencia_rel_genero = df["Género"].value_counts(normalize=True) * 100
frecuencia_rel_genero = frecuencia_rel_genero.round(2)

tabla_genero = pd.DataFrame({
    "Frecuencia absoluta": frecuencia_abs_genero,
    "Frecuencia relativa": frecuencia_rel_genero,
})

tabla_genero = pd.concat([
    tabla_genero,
    crear_fila_vacia(),
    crear_fila_total(frecuencia_abs_genero, frecuencia_rel_genero)
])

# -------------------------------
# Tabla de frecuencias: Nivel educativo
# -------------------------------
frecuencia_abs_nivel = df["Nivel educativo"].value_counts()
frecuencia_rel_nivel = df["Nivel educativo"].value_counts(normalize=True) * 100
frecuencia_rel_nivel = frecuencia_rel_nivel.round(2)

tabla_nivel = pd.DataFrame({
    "Frecuencia absoluta": frecuencia_abs_nivel,
    "Frecuencia relativa": frecuencia_rel_nivel,
})

tabla_nivel = pd.concat([
    tabla_nivel,
    crear_fila_vacia(),
    crear_fila_total(frecuencia_abs_nivel, frecuencia_rel_nivel)
])

# -------------------------------
# Guardar resultados en Excel
# -------------------------------
# with pd.ExcelWriter(
#     r"C:\Users\20204041157\Documents\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\Trabajo_práctico_de_evaluación_de_la_Unidad_1\Ingresantes_anonimizado.xlsx",
#     mode="a",
#     engine="openpyxl",
#     if_sheet_exists="overlay",
# ) as writer:
#     tabla_genero.to_excel(writer, sheet_name="Frecuencias", startrow=0, startcol=0)
#     tabla_nivel.to_excel(writer, sheet_name="Frecuencias", startrow=len(tabla_genero)+3, startcol=0)

# Mostrar tabla en consola
# print("print(type(genero))")
# print(type(genero))

# print("print(type(df_genero))")
# print(type(df_genero))

# print("print(type(frecuencia_abs_genero))")
# print(type(frecuencia_abs_genero))


# print("print(type(tabla_genero))")
# print(type(tabla_genero))

# print("print(type(df['Género']))")
# print(type(df["Género"]))

# print("genero1=df['Género']")
# genero1=df["Género"]
# print(type(genero1))

import matplotlib.pyplot as plt

x=frecuencia_abs_genero.index
y=frecuencia_abs_genero.values

plt.bar(x,y)
plt.show()