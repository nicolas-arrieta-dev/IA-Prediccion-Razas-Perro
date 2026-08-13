from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permite todas las conexiones por ahora


# Cargar el modelo
model_path = 'modelo_perros.h5'
model = load_model(model_path)

razas = ['Beagle', 'Bulldog frances', 'Chihuahua', 'Dalmata', 'Doberman', 'Dogo argentino', 'Golden retriever', 'Lobo siberiano', 'Pastor aleman', 'Rottweiler']

# Función para cargar la imagen
def cargar_imagen(imagen):
    img = image.load_img(imagen, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/analizar', methods=['POST'])
def analizar():
    # Obtener la imagen desde la solicitud
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Guardar el archivo temporalmente
    img_path = 'temp_image.jpg'
    file.save(img_path)

    # Realizar la predicción
    img = cargar_imagen(img_path)
    predicciones = model.predict(img)
    prediccion_razon = razas[np.argmax(predicciones)]
    porcentaje = float(np.max(predicciones) * 100)  # 👈 Conversión a tipo float nativo

    return jsonify({
        'raza': prediccion_razon,
        'porcentaje': porcentaje
    })


if __name__ == '__main__':
    app.run(debug=True)
