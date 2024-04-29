from data_processing import load_data, clean_data, load_data_2, get_data
from prediction import prediction_corners_home, prediction_over_under
from prepare_data import select_home_away, prepare_data_corners_home, prepare_data_over_under
from models import model_corners_home, model_over_under

# Ruta al archivo CSV
df1 = "../data/SC0.csv"
df2 = "../data/SC0(1).csv"
df3 = "../data/SC0(2).csv"
df4 = "../data/SC0(3).csv"
df5 = "../data/SC0(4).csv"

nombre_archivo = '../data/premier_league_data.csv'
# df = get_data(nombre_archivo)
# partidos= select_home_away(df, 'West Ham', 'Liverpool')
# partidos_equipo_local, partidos_equipo_visitante = partidos[0], partidos[1]
# model = prepare_data_over_under(partidos_equipo_local)
# X_train_over_under, X_test_over_under, y_train_over_under, y_test_over_under = model[0], model[1], model[2], model[3]
# corner_home_model = model_over_under(X_train_over_under, y_train_over_under)
# corner = prediction_over_under(corner_home_model, X_test_over_under)
# df_load = load_data(df1, df2, df3, df4, df5)
# clean_data(df_load, nombre_archivo)
# print('Se guardaron los datos correctamente.')
# df_load = load_data_2(nombre_archivo)
# df_unique = df_load['HomeTeam'].unique()
# print(corner)