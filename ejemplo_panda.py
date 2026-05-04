import pandas as pd

# Creamos una lista de ventas rápida
ventas = {'Producto': ['Manzanas', 'Peras'], 'Cantidad': [10, 5]}
df = pd.DataFrame(ventas)

print("¡Hola! Tu DataFrame de Pandas funciona:")
print(df)
