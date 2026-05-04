import pandas as pd
import matplotlib.pyplot as plt

# 1. CARGA (Asegúrate de que el CSV esté en la misma carpeta)
try:
    df = pd.read_csv(r'C:\Users\taty_\OneDrive\Documentos\TATIANA\JOSUE\MyPygame\googleplaystore.csv')
    
    # 2. LIMPIEZA RÁPIDA (Necesaria para que 'Installs' sea número)
    df.dropna(inplace=True)
    df['Installs'] = df['Installs'].str.replace('+', '', regex=False).str.replace(',', '', regex=False)
    df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce').fillna(0)

    # 3. PROCESAMIENTO (Filtrado y agrupamiento)
    top_categorias = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(10)

    # 4. VISUALIZACIÓN
    top_categorias.plot(kind='bar', figsize=(10, 5), color='skyblue')
    plt.title('Top 10 Categorías con más Instalaciones')
    plt.ylabel('Cantidad de Instalaciones')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    print("Generando gráfico...")
    plt.show()

except FileNotFoundError:
    print("Error: No encontré el archivo 'googleplaystore.csv' en esta carpeta.")