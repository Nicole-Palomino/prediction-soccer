from collections import Counter

def prediction_victory(model_victoria, X_test_victoria, y_test_victoria, home_team, away_team):
    prediccion_victoria = model_victoria.predict(X_test_victoria)

    etiquetas_reales = y_test_victoria

    # Contadores para cada resultado
    total_partidos = len(etiquetas_reales)
    total_victorias_local = sum(pred == 'H' and real == 'H' for pred, real in zip(prediccion_victoria, etiquetas_reales))
    total_empates = sum(pred == 'D' and real == 'D' for pred, real in zip(prediccion_victoria, etiquetas_reales))
    total_victorias_visitante = sum(pred == 'A' and real == 'A' for pred, real in zip(prediccion_victoria, etiquetas_reales))

    # Calcular porcentajes
    porcentaje_victorias_local = (total_victorias_local / total_partidos) * 100
    porcentaje_empates = (total_empates / total_partidos) * 100
    porcentaje_victorias_visitante = (total_victorias_visitante / total_partidos) * 100

    # Crear cadena de predicción
    prediccion_de_victoria = f'{home_team} ({porcentaje_victorias_local:.2f}%) Draw ({porcentaje_empates:.2f}%) {away_team} ({porcentaje_victorias_visitante:.2f}%)'

    return prediccion_de_victoria

def prediction_corner(model_corners, X_test_corners):
    prediccion_corners = model_corners.predict(X_test_corners)
    promedio = round(sum(prediccion_corners) / len(prediccion_corners), 2)
    prediction_corner = str(promedio)

    return prediction_corner

def prediction_corners_home(model_corners_equipo_local, X_test_corners_equipo_local, home_away):
    prediccion_corners_equipo_local = model_corners_equipo_local.predict(X_test_corners_equipo_local)
    promedio = round(sum(prediccion_corners_equipo_local) / len(prediccion_corners_equipo_local), 2)
    prediction_home = str(promedio)

    return prediction_home

def prediction_corners_away(model_corners_equipo_visitante, X_test_corners_equipo_visitante, home_away):
    prediccion_corners_equipo_visitante = model_corners_equipo_visitante.predict(X_test_corners_equipo_visitante)
    promedio = round(sum(prediccion_corners_equipo_visitante) / len(prediccion_corners_equipo_visitante), 2)
    prediction_away = str(promedio)

    return prediction_away

def prediction_yellow_cards(model_tarjetas, X_test_tarjetas):
    prediccion_tarjetas = model_tarjetas.predict(X_test_tarjetas)
    promedio = round(sum(prediccion_tarjetas) / len(prediccion_tarjetas), 2)
    prediction_cards = str(promedio)

    return prediction_cards

def prediction_over_under(model_over_under, X_test_over_under):
    prediccion_over_under = model_over_under.predict(X_test_over_under)

    frecuencias = Counter(prediccion_over_under)
    valor_mas_comun = frecuencias.most_common(1)[0][0]

    if valor_mas_comun:
        prediccion_ou = f'over 2.5 goals'
    else:
        prediccion_ou = f'under 2.5 goals'

    return prediccion_ou

def prediction_goals_home(model_goals_local, X_test_goals_local, home_team):
    prediccion_goals_local = model_goals_local.predict(X_test_goals_local)
    promedio = round(sum(prediccion_goals_local) / len(prediccion_goals_local), 2)
    prediction_home = str(promedio)

    return prediction_home

def prediction_goals_away(model_goals_away, X_test_goals_away, away_team):
    prediccion_goals_away = model_goals_away.predict(X_test_goals_away)
    promedio = round(sum(prediccion_goals_away) / len(prediccion_goals_away), 2)
    prediction_away = str(promedio)

    return prediction_away

def prediction_btts(model_ambos_marcan, X_test_ambos_marcan):
    prediccion_ambos_marcan = model_ambos_marcan.predict(X_test_ambos_marcan)

    frecuencias = Counter(prediccion_ambos_marcan)
    valor_mas_comun = frecuencias.most_common(1)[0][0]

    if valor_mas_comun == True:
        prediccion_btts = f'Sí'
    else:
        prediccion_btts = f'No'

    return prediccion_btts