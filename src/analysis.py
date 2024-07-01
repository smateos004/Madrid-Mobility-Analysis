import pandas as pd

def analyze_transport_modes(df):
    """
    Analiza el tipo de transporte utilizado (público o privado).
    """
    transport_counts = df['transport_mode'].value_counts()
    return transport_counts

def analyze_trip_reasons(df):
    """
    Analiza los motivos de los desplazamientos.
    """
    trip_reasons = df['trip_reason'].value_counts()
    return trip_reasons

if __name__ == "__main__":
    processed_data_path = '../data/processed/clean_mobility_data.csv'
    
    data = pd.read_csv(processed_data_path)
    
    transport_modes = analyze_transport_modes(data)
    trip_reasons = analyze_trip_reasons(data)
    
    print("Transport Modes:")
    print(transport_modes)
    
    print("\nTrip Reasons:")
    print(trip_reasons)
