from data_processing import load_data, clean_data, load_data_2

# Ruta al archivo CSV
df1 = "../data/SC0.csv"
df2 = "../data/SC0(1).csv"
df3 = "../data/SC0(2).csv"
df4 = "../data/SC0(3).csv"
df5 = "../data/SC0(4).csv"

nombre_archivo = '../data/liga_escocia_data.csv'

# df_load = load_data(df1, df2, df3, df4, df5)
# clean_data(df_load, nombre_archivo)
# print('Se guardaron los datos correctamente.')
# df_load = load_data_2(nombre_archivo)
# df_unique = df_load['HomeTeam'].unique()
# print(df_unique)