import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL de la página de Wikipedia
url = "https://es.wikipedia.org/wiki/Anexo:Canciones_m%C3%A1s_reproducidas_en_Spotify"

# 1️. Recolectar los datos
response = requests.get(url)
tables = pd.read_html(response.text)   # Extrae todas las tablas de la página

# Normalmente la primera tabla contiene las canciones
df = tables[0]

print("Columnas originales:")
print(df.columns)

# 2️. Procesar los datos
# Renombramos las columnas (puede variar un poco según la versión de la tabla)
df.columns = ["Posición", "Canción", "Artista", "Reproducciones (miles de millones)", "Fecha de lanzamiento"]

# Convertimos la columna de reproducciones a número
df["Reproducciones (miles de millones)"] = (
    df["Reproducciones (miles de millones)"]
    .astype(str)
    .str.replace(",", ".")
    .astype(float)
)

# 3️. Visualizar los datos
# Mostramos el top 10 por reproducciones
top10 = df.sort_values(by="Reproducciones (miles de millones)", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top10["Canción"], top10["Reproducciones (miles de millones)"], color="skyblue")
plt.xlabel("Reproducciones (miles de millones)")
plt.ylabel("Canción")
plt.title("Top 10 canciones más reproducidas en Spotify (Wikipedia)")
plt.gca().invert_yaxis()  # Para que la canción más reproducida quede arriba
plt.tight_layout()
plt.show()
