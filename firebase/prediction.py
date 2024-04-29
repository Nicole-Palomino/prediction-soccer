from scipy.stats import mode

def prediction_victory(model_victoria, X_test_victoria, y_test_victoria, home_team, away_team):
    prediccion_victoria = model_victoria.predict(X_test_victoria)[0]
    etiquetas_reales = y_test_victoria
    conteo_aciertos = sum(prediccion_victoria == etiquetas_reales)
    porcentaje_aciertos = round((conteo_aciertos / len(etiquetas_reales)) * 100, 2)

    if prediccion_victoria == 'H':
        prediccion_victoria = f'{home_team} gana ({porcentaje_aciertos}%)'
    elif prediccion_victoria == 'A':
        prediccion_victoria = f'{away_team} gana ({porcentaje_aciertos}%)'
    else:
        prediccion_victoria = f'Empate ({porcentaje_aciertos}%)'

    return prediccion_victoria

def prediction_corner(model_corners, X_test_corners):
    prediccion_corners = model_corners.predict(X_test_corners)[0]
    prediction_corner = str(prediccion_corners)

    return prediction_corner

def prediction_corners_home(model_corners_equipo_local, X_test_corners_equipo_local, home_away):
    prediccion_corners_equipo_local = mode(model_corners_equipo_local.predict(X_test_corners_equipo_local))[0][0]
    prediction_home = str(prediccion_corners_equipo_local)

    return prediction_home

def prediction_corners_away(model_corners_equipo_visitante, X_test_corners_equipo_visitante, home_away):
    prediccion_corners_equipo_visitante = mode(model_corners_equipo_visitante.predict(X_test_corners_equipo_visitante))[0][0]
    prediction_away = str(prediccion_corners_equipo_visitante)

    return prediction_away

def prediction_yellow_cards(model_tarjetas, X_test_tarjetas):
    prediccion_tarjetas = model_tarjetas.predict(X_test_tarjetas)[0]
    prediction_cards = str(prediccion_tarjetas)

    return prediction_cards

def prediction_over_under(model_over_under, X_test_over_under):
    prediccion_over_under = mode(model_over_under.predict(X_test_over_under))[0][0]

    if prediccion_over_under == True:
        prediccion_ou = f'over 2.5 goals'
    else:
        prediccion_ou = f'under 2.5 goals'

    return prediccion_ou

def prediction_goals_home(model_goals_local, X_test_goals_local, home_team):
    prediccion_goals_local = mode(model_goals_local.predict(X_test_goals_local))[0][0]
    prediction_home = str(prediccion_goals_local)

    return prediction_home

def prediction_goals_away(model_goals_away, X_test_goals_away, away_team):
    prediccion_goals_away = mode(model_goals_away.predict(X_test_goals_away))[0][0]
    prediction_away = str(prediccion_goals_away)

    return prediction_away

def prediction_btts(model_ambos_marcan, X_test_ambos_marcan):
    prediccion_ambos_marcan = model_ambos_marcan.predict(X_test_ambos_marcan)[0]

    if prediccion_ambos_marcan == True:
        prediccion_btts = f'Sí'
    else:
        prediccion_btts = f'No'

    return prediccion_btts