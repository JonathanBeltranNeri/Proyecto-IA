# entrenar_modelos.py

import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Configuración
VENTANA = 60
RUTA_DATOS = "datos_normalizados"
RUTA_MODELOS = "modelos_lstm"
os.makedirs(RUTA_MODELOS, exist_ok=True)

# Función para entrenar un modelo LSTM
for archivo in os.listdir(RUTA_DATOS):
    if archivo.endswith(".npz"):
        nombre = archivo.replace(".npz", "")
        ruta = os.path.join(RUTA_DATOS, archivo)
        datos = np.load(ruta)

        X = datos['X']
        y = datos['y']

        # Dividir en entrenamiento y prueba
        split = int(len(X) * 0.8)
        X_train, y_train = X[:split], y[:split]
        X_test, y_test = X[split:], y[split:]

        # Crear el modelo
        modelo = Sequential()
        modelo.add(LSTM(50, return_sequences=True, input_shape=(VENTANA, 1)))
        modelo.add(LSTM(50))
        modelo.add(Dense(1))
        modelo.compile(optimizer='adam', loss='mean_squared_error')

        # Entrenar el modelo
        print(f"⏳ Entrenando modelo para {nombre}...")
        modelo.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)

        # Guardar modelo
        modelo.save(os.path.join(RUTA_MODELOS, f"{nombre}.h5"))
        print(f"✅ Modelo guardado: {nombre}.h5")

print("🎯 Todos los modelos fueron entrenados.")
