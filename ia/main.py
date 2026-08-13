import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Rutas al modelo guardado
model_path = 'modelo_perros.h5'

# Preguntar al usuario si quiere usar el modelo o entrenarlo
opcion = input("¿Deseas usar el modelo entrenado o entrenarlo nuevamente? (usar/entrenar): ").strip().lower()

# Función para cargar y preprocesar una nueva imagen para hacer predicciones
def cargar_imagen(imagen_path):
    img = image.load_img(imagen_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Clases de razas de perro
razas = ['Beagle', 'Bulldog frances', 'Chihuahua', 'Dalmata', 'Doberman', 'Dogo argentino', 'Golden retriever', 'Lobo siberiano', 'Pastor aleman', 'Rottweiler']

if opcion == 'usar':
    if os.path.exists(model_path):
        print("Cargando el modelo previamente entrenado...")
        model = load_model(model_path)
        
        # Pedir la ruta de la imagen
        img_path = input("Por favor, ingresa la ruta de la imagen para clasificar: ")
        img = cargar_imagen(img_path)
        
        # Hacer predicción
        predicciones = model.predict(img)
        prediccion_razon = razas[np.argmax(predicciones)]
        porcentaje = np.max(predicciones) * 100
        
        print(f'La raza predicha es: {prediccion_razon} con una certeza del {porcentaje:.2f}%')
    else:
        print("El modelo no existe. Debes entrenarlo primero.")
elif opcion == 'entrenar':
    # Rutas a las carpetas con las imágenes
    train_dir = 'dataset/train'
    validation_dir = 'dataset/validation'
    
    # Preprocesamiento y augmentación de imágenes para entrenamiento
    train_datagen = ImageDataGenerator(
        rescale=1./255,         
        rotation_range=40,     
        width_shift_range=0.2, 
        height_shift_range=0.2, 
        shear_range=0.2,       
        zoom_range=0.2,        
        horizontal_flip=True,  
        fill_mode='nearest'    
    )

    validation_datagen = ImageDataGenerator(rescale=1./255)

    # Generadores de imágenes
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150),  
        batch_size=32,
        class_mode='categorical' 
    )

    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical'
    )

    # Crear el modelo
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')  
    ])

    # Compilar el modelo
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(),
                  metrics=['accuracy'])

    # Entrenamiento del modelo
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // train_generator.batch_size,
        epochs=20,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // validation_generator.batch_size
    )

    # Guardar el modelo
    model.save(model_path)
    print(f"Modelo entrenado y guardado en {model_path}")

else:
    print("Opción no válida. Por favor, selecciona 'usar' o 'entrenar'.")
