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