import pandas as pd

# 1. Creamos el DataFrame inicial
ventas = {'Producto': ['Manzanas', 'Peras'], 'Cantidad': [10, 5]}
df = pd.DataFrame(ventas)

# 2. Creamos una nueva fila (Plátanos)
nueva_fila = pd.DataFrame({'Producto': ['Plátanos'], 'Cantidad': [12]})

# 3. Agregamos la fila al DataFrame original
df = pd.concat([df, nueva_fila], ignore_index=True)

# 4. Creamos nueva fila no.2(Naranjas)
nueva_fila2 = pd.DataFrame({'Producto': ['Naranjas'], 'Cantidad': [18]})

# 5. Agregamos la fila al Dataframe original
df = pd.concat([df, nueva_fila2], ignore_index=True)

# 6. Agregamos la nueva columna de Precio
# (Asegúrate de que la lista tenga 4 valores, uno para cada fila)
df['Precio'] = [1.5, 2.0, 1.2, 1.8]

# 7. Agregamos la nueva columna Descripción
df['Descripcion'] = ['Fruta', 'Fruta', 'Fruta', 'Fruta']
print("¡DataFrame actualizado!")

nueva_fila3 = pd.DataFrame({'Producto': ['Sandía'], 'Cantidad': [10]})
df = pd.concat([df, nueva_fila3], ignore_index=True)

df['color'] = ['Rojo', 'Verde', 'Amarillo', 'Naranja', 'Verde']
print(df)
