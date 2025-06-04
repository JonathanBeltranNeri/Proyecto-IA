# main.py — Proyecto IA con LSTM por empresa
# ==========================================

import yfinance as yf
import pandas as pd
import numpy as np
import os
import json
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# ========== Configuración ==========
empresas = ["AAPL", "TSLA", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "NFLX", "INTC", "AMD"]
os.makedirs("datos_empresas", exist_ok=True)
os.makedirs("web", exist_ok=True)
ventana = 60
margen = 1.0

# ========== Funciones reutilizables ==========

def crear_secuencias(data, ventana):
    X, y = [], []
    for i in range(ventana, len(data)):
        X.append(data[i-ventana:i, 0])
        y.append(data[i, 0])
    X = np.array(X).reshape(-1, ventana, 1)
    y = np.array(y)
    return X, y

def generar_senales(valores_reales, predicciones, margen):
    senales = []
    for i in range(1, len(predicciones)):
        precio_anterior = valores_reales[i-1][0]
        precio_predicho = predicciones[i][0]
        diferencia = precio_predicho - precio_anterior
        if diferencia > margen:
            senales.append("COMPRAR")
        elif diferencia < -margen:
            senales.append("VENDER")
        else:
            senales.append("MANTENER")
    senales.insert(0, "MANTENER")  # Primer día sin comparación
    return senales

# ========== Proceso por empresa ==========
for ticker in empresas:
    print(f"\n📈 Procesando empresa: {ticker}")

    # --- Descargar y preparar datos ---
    datos = yf.download(ticker, start="2020-01-01", end="2024-12-31")[['Close']].dropna()
    datos.to_csv(f"datos_empresas/{ticker}.csv")

    precios = datos['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    precios_norm = scaler.fit_transform(precios)

    # --- Crear secuencias ---
    X, y = crear_secuencias(precios_norm, ventana)
    X_ent, y_ent = X[:int(0.8*len(X))], y[:int(0.8*len(y))]
    X_pru, y_pru = X[int(0.8*len(X)):], y[int(0.8*len(y)):]

    # --- Modelo LSTM ---
    modelo = Sequential()
    modelo.add(LSTM(50, return_sequences=True, input_shape=(ventana, 1)))
    modelo.add(LSTM(50))
    modelo.add(Dense(1))
    modelo.compile(optimizer='adam', loss='mean_squared_error')
    modelo.fit(X_ent, y_ent, epochs=10, batch_size=32, verbose=0)

    # --- Predicciones y señales ---
    pred = modelo.predict(X_pru, verbose=0)
    pred = scaler.inverse_transform(pred)
    reales = scaler.inverse_transform(y_pru.reshape(-1, 1))
    senales = generar_senales(reales, pred, margen)

    # --- JSON final de los últimos 10 días ---
    valores_final = reales[-10:].flatten()
    pred_final = pred[-10:].flatten()
    senales_final = senales[-10:]

    salida = [
        {
            "dia": f"Día {i+1}",
            "precio_real": float(valores_final[i]),
            "precio_predicho": float(pred_final[i]),
            "senal": senales_final[i]
        }
        for i in range(10)
    ]

    # --- Guardar archivo ---
    ruta_json = f"web/predicciones_{ticker}.json"
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(salida, f, indent=4, ensure_ascii=False)
    print(f"✅ Archivo guardado: {ruta_json}")

print("\n🚀 Todo listo. Archivos exportados por empresa en la carpeta 'web'.")
