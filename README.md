# Proyecto-IA
# 📈 Predicción Bursátil con LSTM

Este proyecto utiliza un modelo LSTM (Long Short-Term Memory) para predecir precios de acciones de diferentes empresas tecnológicas y generar señales de compra, venta o mantener.

## 🧠 ¿Qué hace?

- Descarga datos históricos de precios (`Close`) de 10 empresas desde Yahoo Finance
- Entrena un modelo LSTM por empresa
- Genera predicciones de precios y señales de decisión
- Exporta los resultados en archivos JSON individuales
- Muestra todo en una página web moderna e interactiva

## 🏗 Estructura del proyecto

```
Proyecto-IA/
├── main.py                    # Script de entrenamiento y predicción
├── datos_empresas/           # Archivos CSV descargados por empresa
├── web/
│   ├── index.html            # Interfaz visual de resultados
│   ├── predicciones_*.json  # Archivos JSON por empresa (AAPL, TSLA, etc.)
```

## 🚀 Cómo ejecutar

1. Instala dependencias:
```bash
pip install yfinance pandas numpy scikit-learn tensorflow
```

2. Ejecuta el modelo:
```bash
python3.10 main.py
```

3. Lanza la interfaz web:
```bash
cd web
python3.10 -m http.server 8000
```

4. Abre en el navegador:
```
http://localhost:8000
```

## 📊 Empresas analizadas

- AAPL (Apple)
- TSLA (Tesla)
- MSFT (Microsoft)
- NVDA (NVIDIA)
- GOOGL (Google)
- AMZN (Amazon)
- META (Meta)
- NFLX (Netflix)
- INTC (Intel)
- AMD (AMD)

## ✨ Características visuales

- Selector dinámico de empresa
- Gráfica con colores personalizados
- Leyenda moderna con emojis
- Fondo animado tipo Flow Icons
- Estilo minimalista con Tailwind CSS

## 📌 Estado actual

✅ Funcional  
🚧 Mejoras pendientes: optimización del modelo, métricas de rendimiento, predicción multivariable

---
Desarrollado por Jonathan Beltran Neri 22310188 CETI