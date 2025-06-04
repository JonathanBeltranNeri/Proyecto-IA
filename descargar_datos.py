# descargar_datos.py

import yfinance as yf
import os
from datetime import date

# Crear carpeta donde se guardarán los CSV
os.makedirs("datos_empresas", exist_ok=True)

# Lista de empresas a analizar
empresas = ["AAPL", "TSLA", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "NFLX", "INTC", "AMD"]

# Definir fechas de descarga: desde 2020 hasta hoy
fecha_inicio = "2020-01-01"
fecha_fin = str(date.today())  # Fecha actual

# Descargar y guardar CSV por empresa
for ticker in empresas:
    print(f"📥 Descargando datos de {ticker}...")
    df = yf.download(ticker, start=fecha_inicio, end=fecha_fin)[['Close']].dropna()
    df.to_csv(f"datos_empresas/{ticker}.csv")

print("✅ Todos los datos fueron descargados y guardados en /datos_empresas/")
