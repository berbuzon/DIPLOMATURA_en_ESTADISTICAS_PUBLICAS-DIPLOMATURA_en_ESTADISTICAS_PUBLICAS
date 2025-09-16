import pandas as pd

df = pd.read_excel(
    r"C:\Users\Usuario\Documents\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS-DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\Trabajo_práctico_de_evaluación_de_la_Unidad_1\Ingresantes_anonimizado.xlsx",
    sheet_name="Educ_Genero",
)

genero = df["Género"].unique()
nivel_educativo = df["Nivel educativo"].unique()


df_genero = pd.DataFrame(genero, columns=["Género"])
df_nivel_educativo = pd.DataFrame(nivel_educativo, columns=["Nivel educativo"])

# df_categorias = pd.concat([df_genero, df_nivel_educativo], axis=1)

with pd.ExcelWriter(
    r"C:\Users\Usuario\Documents\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS-DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\Trabajo_práctico_de_evaluación_de_la_Unidad_1\Ingresantes_anonimizado.xlsx",
    mode="a",
    engine="openpyxl",
    if_sheet_exists="overlay",
) as writer:
    df_genero.to_excel(writer, sheet_name="Categorias",index=False,    startrow=0, startcol=0)
    df_nivel_educativo.to_excel(writer, sheet_name="Categorias",index=False,    startrow=len(df_genero)+3, startcol=0)


frecuencia_abs_genero = df["Género"].value_counts()
frecuencia_rel_genero = df["Género"].value_counts(normalize=True)*100
frecuencia_rel_genero = frecuencia_rel_genero.round(2)  # redondear a 2 decimales

frecuencia_rel_nivel = df["Nivel educativo"].value_counts(normalize=True) * 100
frecuencia_rel_nivel = frecuencia_rel_nivel.round(2)

tabla_genero = pd.DataFrame({
    "Frecuencia absoluta": frecuencia_abs_genero,
    "Frecuencia relativa": frecuencia_rel_genero
})

tabla_nivel = pd.DataFrame({
    "Frecuencia absoluta": frecuencia_abs_nivel,
    "Frecuencia relativa": frecuencia_rel_nivel
})

# df_frecuencias = pd.concat([tabla_genero, tabla_nivel], axis=1)

with pd.ExcelWriter(
    r"C:\Users\Usuario\Documents\DIPLOMATURA_en_ESTADISTICAS_PUBLICAS-DIPLOMATURA_en_ESTADISTICAS_PUBLICAS\Trabajo_práctico_de_evaluación_de_la_Unidad_1\Ingresantes_anonimizado.xlsx",
    mode="a",
    engine="openpyxl",
    if_sheet_exists="overlay"
) as writer:
    tabla_genero.to_excel(writer, sheet_name="Frecuencias", startrow=0, startcol=0)
    tabla_nivel.to_excel(writer, sheet_name="Frecuencias", startrow=len(tabla_genero)+3, startcol=0)


