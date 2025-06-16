Proyecto-IA
📈 Predicción Bursátil con LSTM

Este proyecto utiliza un modelo LSTM (Long Short-Term Memory) para predecir los precios de acciones de diferentes empresas tecnológicas y generar señales de compra, venta o mantener.
🧠 ¿Qué hace?

    Descarga datos históricos de precios (Close) de 10 empresas desde Yahoo Finance.

    Entrena un modelo LSTM de forma individual para cada empresa.

    Genera predicciones de precios y señales de decisión.

    Exporta los resultados en archivos .json por empresa.

    Visualiza los resultados en una página web moderna e interactiva.

🏗 Estructura del proyecto

Proyecto-IA/
├── main.py                    # Script de entrenamiento y predicción (ya no se utiliza)
├── datos_empresas/           # Archivos CSV descargados por empresa
├── web/
│   ├── index.html            # Interfaz visual con gráfico y tabla de señales
│   ├── predicciones_*.json  # Archivos JSON generados por empresa (AAPL, TSLA, etc.)

🚀 Cómo ejecutar

    Instala las dependencias:

pip install yfinance pandas numpy scikit-learn tensorflow

    Ejecuta el modelo de predicción:

python3.10 main.py

    Lanza el servidor web:

cd web
python3.10 -m http.server 8000

    Abre en el navegador:

http://localhost:8000

📊 Empresas analizadas

    AAPL (Apple)

    TSLA (Tesla)

    MSFT (Microsoft)

    NVDA (NVIDIA)

    GOOGL (Google)

    AMZN (Amazon)

    META (Meta)

    NFLX (Netflix)

    INTC (Intel)

    AMD (AMD)

✨ Características visuales

    Selector dinámico de empresa

    Gráfica de precios con diseño elegante y colores personalizados

    Tabla de señales con colores modernos

    Fondo animado estilo Flow Icons

    Diseño minimalista con Tailwind CSS y tipografía moderna

📌 Estado actual

✅ Funcional y visualmente atractivo
🚧 Mejoras pendientes:

    Optimización del modelo LSTM

    Evaluación con métricas (RMSE, MAE)

    Predicción multivariable (Open, High, Volume, etc.)

🌐 Proyecto en línea

Puedes ver la versión en línea del proyecto aquí:
🔗 https://proyecto-ia-jonathanbeltranneris-projects.vercel.app/

Desarrollado por: Jonathan Beltrán Neri
Centro de Enseñanza Técnica Industrial (CETI)
