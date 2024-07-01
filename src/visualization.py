import pandas as pd
import folium
import geopandas as gpd

def create_heatmap(df, output_path):
    """
    Crea un mapa de calor basado en los datos de rutas.
    """
    madrid_map = folium.Map(location=[40.4168, -3.7038], zoom_start=12)
    
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            weight=2,
            color='blue'
        ).add_to(madrid_map)
    
    madrid_map.save(output_path)

if __name__ == "__main__":
    processed_data_path = '../data/processed/clean_mobility_data.csv'
    heatmap_output_path = '../data/processed/madrid_heatmap.html'
    
    data = pd.read_csv(processed_data_path)
    
    create_heatmap(data, heatmap_output_path)
