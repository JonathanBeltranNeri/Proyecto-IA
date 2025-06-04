# generar_predicciones.py

import os
import numpy as np
import json
from datetime import datetime, timedelta
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

VENTANA = 60
RUTA_MODELOS = "modelos_lstm"
RUTA_DATOS = "datos_normalizados"
RUTA_SALIDA = "web"
os.makedirs(RUTA_SALIDA, exist_ok=True)

# Función para desnormalizar correctamente
def desnormalizar(valores, min_, max_):
    return valores * (max_ - min_) + min_

# Función para generar señales
def generar_senales(real, predicho, margen=1.0):
    senales = []
    for i in range(1, len(predicho)):
        diff = predicho[i] - real[i - 1]
        if diff > margen:
            senales.append("COMPRAR")
        elif diff < -margen:
            senales.append("VENDER")
        else:
            senales.append("MANTENER")
    senales.insert(0, "MANTENER")
    return senales

# Generar predicciones para cada archivo .npz
for archivo in os.listdir(RUTA_DATOS):
    if archivo.endswith(".npz"):
        nombre = archivo.replace(".npz", "")
        modelo_path = os.path.join(RUTA_MODELOS, f"{nombre}.h5")
        datos_path = os.path.join(RUTA_DATOS, archivo)

        if not os.path.exists(modelo_path):
            print(f"❌ Modelo no encontrado para {nombre}")
            continue

        modelo = load_model(modelo_path)
        datos = np.load(datos_path)

        X = datos['X']
        y = datos['y']
        min_ = datos['scaler_min']
        max_ = datos['scaler_max']

        # Predicción y desnormalización
        pred = modelo.predict(X).reshape(-1, 1)
        reales = y.reshape(-1, 1)

        reales_desnorm = desnormalizar(reales, min_, max_).flatten()
        pred_desnorm = desnormalizar(pred, min_, max_).flatten()

        reales_desnorm = np.maximum(reales_desnorm, 0)  # Eliminar negativos
        pred_desnorm = np.maximum(pred_desnorm, 0)

        # Generar fechas reales
        fecha_base = datetime.today() + timedelta(days=1)
        fechas = [(fecha_base + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(len(pred_desnorm))]

        # Generar señales
        senales = generar_senales(reales_desnorm, pred_desnorm)

        # Armar estructura JSON
        salida = [
            {
                "fecha": fechas[i],
                "precio_real": round(float(reales_desnorm[i]), 2),
                "precio_predicho": round(float(pred_desnorm[i]), 2),
                "senal": senales[i]
            }
            for i in range(len(pred_desnorm))
        ]

        # Guardar archivo
        ruta_json = os.path.join(RUTA_SALIDA, f"predicciones_{nombre}.json")
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(salida, f, indent=4, ensure_ascii=False)

        print(f"✅ JSON generado: {ruta_json}")

print("🎯 Todos los archivos .json fueron generados con fechas reales y precios limpios.")
