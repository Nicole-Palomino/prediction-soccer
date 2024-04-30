import pandas as pd

def load_data(file_1, file_2, file_3, file_4, file_5):
    """
    Loads the CSV file into a DataFrame.

    Parameters:
    file_path (str): CSV file path.

    Returns:
    pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    df1 = pd.read_csv(file_1, delimiter=',')
    df2 = pd.read_csv(file_2, delimiter=',')
    df3 = pd.read_csv(file_3, delimiter=',')
    df4 = pd.read_csv(file_4, delimiter=',')
    df5 = pd.read_csv(file_5, delimiter=',')

    df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

    return df

def clean_data(df, nombre_archivo):
    columnas = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']
    df = df[columnas]

    df.to_csv(nombre_archivo, index=False)

def get_data(file):
    df = pd.read_csv(file, delimiter=',')

    return df

def get_data_excel():
    file = './data/ligas.xlsx'
    df = pd.read_excel(file)

    return df

def get_leagues(df_league):
    array = df_league['ligas'].head(8).tolist()

    return array

def get_teams_for_league(league, df_league):
    if league == "Premier League":
        array = df_league[league].tolist()
        return array
    elif league == "LaLiga":
        array = df_league[league].tolist()
        return array
    elif league == "SerieA":
        array = df_league[league].tolist()
        return array
    elif league == "Bundesliga":
        array = df_league[league].head(18).tolist()
        return array
    elif league == "Eredivisie":
        array = df_league[league].head(18).tolist()
        return array
    elif league == "Ligue 1":
        array = df_league[league].head(18).tolist()
        return array
    elif league == "Jupiler Pro League":
        array = df_league[league].head(16).tolist()
        return array
    elif league == "Premiership":
        array = df_league[league].head(12).tolist()
        return array
    else:
        return 'Seleccione un equipo disponible'
    
def get_file_league(league):
    if league == "Premier League":
        file = './data/premier_league_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "LaLiga":
        file = './data/laliga_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "SerieA":
        file = './data/seriea_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "Bundesliga":
        file = './data/bundesliga_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "Eredivisie":
        file = './data/eredivisie_data.csv'
        df_premier_legaue = get_data(file)
        return df_premier_legaue
    elif league == "Ligue 1":
        file = './data/ligue1_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "Jupiler Pro League":
        file = './data/liga_belgica_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "Premiership":
        file = './data/liga_escocia_data.csv'
        df_data = get_data(file)
        return df_data
    else:
        return 'Seleccione una liga disponible'

def load_data_2(file_1):
    """
    Loads the CSV file into a DataFrame.

    Parameters:
    file_path (str): CSV file path.

    Returns:
    pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv(file_1, delimiter=',')

    return df