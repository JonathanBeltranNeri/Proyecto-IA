# preparar_datos.py

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

VENTANA = 60
RUTA_CSV = "datos_empresas"
RUTA_SALIDA = "datos_normalizados"
os.makedirs(RUTA_SALIDA, exist_ok=True)

def crear_secuencias(datos, ventana):
    X, y = [], []
    for i in range(ventana, len(datos)):
        X.append(datos[i - ventana:i, 0])
        y.append(datos[i, 0])
    return np.array(X), np.array(y)

for archivo in os.listdir(RUTA_CSV):
    if archivo.endswith(".csv"):
        nombre = archivo.replace(".csv", "")
        ruta_archivo = os.path.join(RUTA_CSV, archivo)

        df = pd.read_csv(ruta_archivo)

        if 'Close' not in df.columns:
            print(f"⚠️ {nombre} no tiene columna 'Close'. Saltando...")
            continue

        # 🔎 Eliminar filas con texto o errores en la columna 'Close'
        df = df[['Close']].copy()
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df = df.dropna()

        precios = df[['Close']].values

        scaler = MinMaxScaler(feature_range=(0, 1))
        precios_norm = scaler.fit_transform(precios)

        X, y = crear_secuencias(precios_norm, VENTANA)

        if len(X) == 0:
            print(f"⚠️ {nombre} no tiene suficientes datos tras normalizar. Saltando...")
            continue

        np.savez_compressed(os.path.join(RUTA_SALIDA, f"{nombre}.npz"),
                            X=X, y=y,
                            scaler_min=scaler.data_min_,
                            scaler_max=scaler.data_max_)

        print(f"✅ {nombre} — X: {X.shape}, y: {y.shape}")

print("🎯 Todos los datos fueron normalizados y convertidos a secuencias.")
