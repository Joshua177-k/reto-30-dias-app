import pandas as pd

# Ejemplo de ruta completa (ajusta a tu ubicación real)
df = pd.read_csv(r"C:\Users\taty_\OneDrive\Documentos\TATIANA\JOSUE\MyPygame\GoogleApps.csv")


# 1. ¿Cuál es el nombre de la primera aplicación?
# Usamos .iloc[0] para la primera fila y el nombre de la columna (ajusta si se llama 'App')
print("Primera aplicación:", df.iloc[0]['App'])

# 2. ¿Categoría de la última aplicación?
# .iloc[-1] accede al último registro
print("Categoría de la última:", df.iloc[-1]['Category'])

# 3. ¿Cuántas columnas hay y qué tipos de datos?
print(f"Número de columnas: {df.shape[1]}")
print(df.dtypes) # O puedes usar df.info()

# 4. Media y Mediana del Tamaño (Size)
# Nota: Esto funciona si 'Size' ya es numérico
print(f"Media Tamaño: {df['Size'].mean()}")
print(f"Mediana Tamaño: {df['Size'].median()}")

# 5. ¿Cuánto cuesta la más cara? (Price)
print(f"Precio máximo: {df['Price'].max()}")

# 6. Media y Mediana de Instalaciones (Installs)
print(f"Media Instalaciones: {df['Installs'].mean()}")
print(f"Mediana Instalaciones: {df['Installs'].median()}")