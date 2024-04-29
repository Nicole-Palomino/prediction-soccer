from sklearn.linear_model import LogisticRegression

def model_victory(X_train_victoria, y_train_victoria):
    model_victoria = LogisticRegression()
    model_victoria.fit(X_train_victoria, y_train_victoria)

    return model_victoria

def model_corner(X_train_corners, y_train_corners):
    model_corners = LogisticRegression()
    model_corners.fit(X_train_corners, y_train_corners)

    return model_corners

def model_corners_home(X_corners_equipo_local, y_corners_equipo_local):
    model_corners_equipo_local = LogisticRegression()
    model_corners_equipo_local.fit(X_corners_equipo_local, y_corners_equipo_local)

    return model_corners_equipo_local

def model_corners_away(X_corners_equipo_visitante, y_corners_equipo_visitante):
    model_corners_equipo_visitante = LogisticRegression()
    model_corners_equipo_visitante.fit(X_corners_equipo_visitante, y_corners_equipo_visitante)

    return model_corners_equipo_visitante

def model_yellow_cards(X_train_tarjetas, y_train_tarjetas):
    model_tarjetas = LogisticRegression()
    model_tarjetas.fit(X_train_tarjetas, y_train_tarjetas)

    return model_tarjetas

def model_over_under(X_train_over_under, y_train_over_under):
    model_over_under = LogisticRegression()
    model_over_under.fit(X_train_over_under, y_train_over_under)

    return model_over_under

def model_goals_home(X_train_goals_local, y_train_goals_local):
    model_goals_local = LogisticRegression()
    model_goals_local.fit(X_train_goals_local, y_train_goals_local)

    return model_goals_local

def model_goals_away(X_train_goals_away, y_train_goals_away):
    model_goals_away = LogisticRegression()
    model_goals_away.fit(X_train_goals_away, y_train_goals_away)

    return model_goals_away

def model_btts(X_ambos_marcan, y_ambos_marcan):
    model_ambos_marcan = LogisticRegression()
    model_ambos_marcan.fit(X_ambos_marcan, y_ambos_marcan)

    return model_ambos_marcan