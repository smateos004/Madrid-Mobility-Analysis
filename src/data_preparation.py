import pandas as pd
import geopandas as gpd

def load_data(filepath):
    """
    Carga los datos desde un archivo CSV y los devuelve como un DataFrame.
    """
    return pd.read_csv(filepath)

def clean_data(df):
    """
    Realiza la limpieza de datos, eliminando filas y columnas innecesarias, y manejando valores nulos.
    """
    df = df.dropna()  # Ejemplo de limpieza
    return df

def save_clean_data(df, filepath):
    """
    Guarda el DataFrame limpio en un archivo CSV.
    """
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    raw_data_path = '../data/raw/mobility_data.csv'
    processed_data_path = '../data/processed/clean_mobility_data.csv'
    
    data = load_data(raw_data_path)
    clean_data = clean_data(data)
    save_clean_data(clean_data, processed_data_path)
