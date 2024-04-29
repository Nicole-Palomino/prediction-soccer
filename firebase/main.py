from .prepare_data import prepare_data_victory, prepare_data_corners, prepare_data_cards_yellow, prepare_data_over_under, prepare_data_goals_home, prepare_data_goals_away, prepare_data_btts, prepare_data_corners_home, prepare_data_corners_away, prepare_data_over_corners
from .models import model_victory, model_corner, model_corners_home, model_corners_away, model_yellow_cards, model_over_under, model_goals_home, model_goals_away, model_btts
from .prediction import prediction_victory, prediction_corner, prediction_corners_home, prediction_corners_away, prediction_yellow_cards, prediction_over_under, prediction_goals_home, prediction_goals_away, prediction_btts

def predictions_results(partidos_equipo_local, partidos_equipo_visitante, home_team, away_team):
    # victory
    victory = prepare_data_victory(partidos_equipo_local)
    X_victoria, X_train_victoria, X_test_victoria, y_train_victoria, y_test_victoria = victory[0], victory[1], victory[2], victory[3], victory[4]

    victory_model = model_victory(X_train_victoria, y_train_victoria)
    victory_prediction = prediction_victory(victory_model, X_test_victoria, y_test_victoria, home_team, away_team)

    # corners
    corner = prepare_data_corners(partidos_equipo_local)
    X_train_corners, X_test_corners, y_train_corners, y_test_corners = corner[0], corner[1], corner[2], corner[3]

    corner_model = model_corner(X_train_corners, y_train_corners)
    corner_prediction = prediction_corner(corner_model, X_test_corners)

    # corners home
    corners_home = prepare_data_corners_home(partidos_equipo_local)
    X_train_corners_equipo_local, X_test_corners_equipo_local, y_train_corners_equipo_local, y_test_corners_equipo_local = corners_home[0], corners_home[1], corners_home[2], corners_home[3]

    corners_home_model = model_corners_home(X_train_corners_equipo_local, y_train_corners_equipo_local)
    corner_home_prediction = prediction_corners_home(corners_home_model, X_test_corners_equipo_local, home_team)

    # corners away
    corners_away = prepare_data_corners_away(partidos_equipo_visitante)
    X_train_corners_equipo_visitante, X_test_corners_equipo_visitante, y_train_corners_equipo_visitante, y_test_corners_equipo_visitante = corners_away[0], corners_away[1], corners_away[2], corners_away[3]

    corners_away_model = model_corners_away(X_train_corners_equipo_visitante, y_train_corners_equipo_visitante)
    corner_away_prediction = prediction_corners_away(corners_away_model, X_test_corners_equipo_visitante, away_team)
    
    # yellow cards
    yc = prepare_data_cards_yellow(X_victoria, partidos_equipo_local)
    X_train_tarjetas, X_test_tarjetas, y_train_tarjetas, y_test_tarjetas = yc[0], yc[1], yc[2], yc[3]

    yc_model = model_yellow_cards(X_train_tarjetas, y_train_tarjetas)
    yc_prediction = prediction_yellow_cards(yc_model, X_test_tarjetas)

    # over under
    over_under = prepare_data_over_under(partidos_equipo_local)
    X_train_over_under, X_test_over_under, y_train_over_under, y_test_over_under = over_under[0], over_under[1], over_under[2], over_under[3]

    over_under_model = model_over_under(X_train_over_under, y_train_over_under)
    over_under_prediction = prediction_over_under(over_under_model, X_test_over_under)

    # goals home
    goals_home = prepare_data_goals_home(partidos_equipo_local)
    X_train_goals_local, X_test_goals_local, y_train_goals_local, y_test_goals_local = goals_home[0], goals_home[1], goals_home[2], goals_home[3]

    goals_home_model = model_goals_home(X_train_goals_local, y_train_goals_local)
    goals_home_prediction = prediction_goals_home(goals_home_model, X_test_goals_local, home_team)

    # goals away
    goals_away = prepare_data_goals_away(partidos_equipo_visitante)
    X_train_goals_away, X_test_goals_away, y_train_goals_away, y_test_goals_away = goals_away[0], goals_away[1], goals_away[2], goals_away[3]

    goals_away_model = model_goals_away(X_train_goals_away, y_train_goals_away)
    goals_away_prediction = prediction_goals_away(goals_away_model, X_test_goals_away, away_team)

    # btts
    btts = prepare_data_btts(partidos_equipo_local)
    X_train_ambos_marcan, X_test_ambos_marcan, y_train_ambos_marcan, y_test_ambos_marcan = btts[0], btts[1], btts[2], btts[3]

    btts_model = model_btts(X_train_ambos_marcan, y_train_ambos_marcan)
    btts_prediction = prediction_btts(btts_model, X_test_ambos_marcan)

    # corners prob
    prob_corners = prepare_data_over_corners(partidos_equipo_local, partidos_equipo_visitante, home_team, away_team)
    
    return victory_prediction, corner_prediction, corner_home_prediction, corner_away_prediction, yc_prediction, over_under_prediction, goals_home_prediction, goals_away_prediction, btts_prediction, prob_corners
