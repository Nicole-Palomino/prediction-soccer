from sklearn.model_selection import train_test_split
from scipy.stats import poisson

def select_home_away(df, home_team, away_team):
 
    partidos_equipo_local = df[df['HomeTeam'] == home_team]
    partidos_equipo_visitante = df[df['AwayTeam'] == away_team]

    return partidos_equipo_local, partidos_equipo_visitante

def prepare_data_victory(partidos_equipo_local):
    X_victoria = partidos_equipo_local[['FTHG', 'FTAG', 'HY', 'AY']]
    y_victoria = partidos_equipo_local['FTR']

    X_train_victoria, X_test_victoria, y_train_victoria, y_test_victoria = train_test_split(X_victoria, y_victoria, test_size=0.2, random_state=42)

    return X_victoria, X_train_victoria, X_test_victoria, y_train_victoria, y_test_victoria

def prepare_data_corners(partidos_equipo_local):
    X_corners = partidos_equipo_local[['FTHG', 'FTAG', 'HC', 'AC']]
    y_corners = partidos_equipo_local['HC'] + partidos_equipo_local['AC']

    X_train_corners, X_test_corners, y_train_corners, y_test_corners = train_test_split(X_corners, y_corners, test_size=0.2, random_state=42)

    return X_train_corners, X_test_corners, y_train_corners, y_test_corners

def prepare_data_corners_home(partidos_equipo_local):
    X_corners_equipo_local = partidos_equipo_local[['FTHG', 'FTAG', 'HY', 'AY']]
    y_corners_equipo_local = partidos_equipo_local['HC']

    X_train_corners_equipo_local, X_test_corners_equipo_local, y_train_corners_equipo_local, y_test_corners_equipo_local = train_test_split(X_corners_equipo_local, y_corners_equipo_local, test_size=0.2, random_state=42)

    return X_train_corners_equipo_local, X_test_corners_equipo_local, y_train_corners_equipo_local, y_test_corners_equipo_local

def prepare_data_corners_away(partidos_equipo_visitante):
    X_corners_equipo_visitante = partidos_equipo_visitante[['FTHG', 'FTAG', 'HY', 'AY']]
    y_corners_equipo_visitante = partidos_equipo_visitante['AC']

    X_train_corners_equipo_visitante, X_test_corners_equipo_visitante, y_train_corners_equipo_visitante, y_test_corners_equipo_visitante = train_test_split(X_corners_equipo_visitante, y_corners_equipo_visitante, test_size=0.2, random_state=42)

    return X_train_corners_equipo_visitante, X_test_corners_equipo_visitante, y_train_corners_equipo_visitante, y_test_corners_equipo_visitante
    
def prepare_data_cards_yellow(X_victoria, partidos_equipo_local):
    y_tarjetas = partidos_equipo_local['HY'] + partidos_equipo_local['AY']

    X_train_tarjetas, X_test_tarjetas, y_train_tarjetas, y_test_tarjetas = train_test_split(X_victoria, y_tarjetas, test_size=0.2, random_state=42)

    return X_train_tarjetas, X_test_tarjetas, y_train_tarjetas, y_test_tarjetas

def prepare_data_over_under(partidos_equipo_local):
    partidos_equipo_local.loc[:, 'OverUnder2.5'] = partidos_equipo_local['FTHG'] + partidos_equipo_local['FTAG']
    X_over_under = partidos_equipo_local[['FTHG', 'FTAG']]
    y_over_under = partidos_equipo_local['OverUnder2.5'] > 2.5

    X_train_over_under, X_test_over_under, y_train_over_under, y_test_over_under = train_test_split(X_over_under, y_over_under, test_size=0.2, random_state=42)

    return X_train_over_under, X_test_over_under, y_train_over_under, y_test_over_under

def prepare_data_goals_home(partidos_equipo_local):
    X_goals_local = partidos_equipo_local[['FTHG', 'FTAG', 'HY', 'AY']]
    y_goals_local = partidos_equipo_local['FTHG']

    X_train_goals_local, X_test_goals_local, y_train_goals_local, y_test_goals_local = train_test_split(X_goals_local, y_goals_local, test_size=0.2, random_state=42)

    return X_train_goals_local, X_test_goals_local, y_train_goals_local, y_test_goals_local

def prepare_data_goals_away(partidos_equipo_visitante):
    X_goals_away = partidos_equipo_visitante[['FTHG', 'FTAG', 'HY', 'AY']]
    y_goals_away = partidos_equipo_visitante['FTAG']

    X_train_goals_away, X_test_goals_away, y_train_goals_away, y_test_goals_away = train_test_split(X_goals_away, y_goals_away, test_size=0.2, random_state=42)

    return X_train_goals_away, X_test_goals_away, y_train_goals_away, y_test_goals_away

def prepare_data_btts(partidos_equipo_local):
    partidos_equipo_local.loc[:, 'AmbosMarcan'] = (partidos_equipo_local['FTHG'] > 0) & (partidos_equipo_local['FTAG'] > 0)
    X_ambos_marcan = partidos_equipo_local[['FTHG', 'FTAG', 'HY', 'AY']]
    y_ambos_marcan = partidos_equipo_local['AmbosMarcan']

    X_train_ambos_marcan, X_test_ambos_marcan, y_train_ambos_marcan, y_test_ambos_marcan = train_test_split(X_ambos_marcan, y_ambos_marcan, test_size=0.2, random_state=42)

    return X_train_ambos_marcan, X_test_ambos_marcan, y_train_ambos_marcan, y_test_ambos_marcan 

def prepare_data_over_corners(partidos_equipo_local, partidos_equipo_visitante, home_team, away_team):
    prom_corners_home = partidos_equipo_local['HC'].mean()
    prom_corners_away = partidos_equipo_visitante['AC'].mean()

    prob_corners_home = [poisson.pmf(i, prom_corners_home) for i in range(10)]
    prob_corners_away = [poisson.pmf(i, prom_corners_away) for i in range(10)]

    prob_home_over = sum(prob_corners_home[i] * sum(prob_corners_away[:i]) for i in range(10))
    prob_away_over = sum(prob_corners_away[i] * sum(prob_corners_home[:i]) for i in range(10))

    if prob_home_over > prob_away_over:
        prob_home = f'El {home_team} tendrá más saques de esquina que el {away_team} con una probabilidad del ' + str(round(prob_home_over * 100, 2)) + '%'
        
        return prob_home
    
    elif prob_home_over < prob_away_over:
        prob_away = f'El {away_team} tendrá más saques de esquina que el {home_team} con una probabilidad del ' + str(round(prob_away_over * 100, 2)) + '%'
        
        return prob_away
    
    else:
        prob_draw = 'Ambos equipos tendrán la misma cantidad de saques de esquina'
        return prob_draw
