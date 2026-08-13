import cv2
import numpy as np
from keras.models import load_model
from tkinter import Tk, Button
from PIL import Image, ImageTk

# Cargar el modelo
model = load_model('modelo_perros.h5')

# Clases de perros
clases = ["Beagle", "Bulldog frances", "Chihuahua", "Dalmata", "Doberman", "Dogo argentino", "Golden retriever", "Lobo siberiano", "Pastor aleman", "Rottweiler"]

def clasificar_imagen(frame):
    img = cv2.resize(frame, (150, 150))
    img_array = img / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predicciones = model.predict(img_array)[0]
    indice_prediccion = np.argmax(predicciones)
    confianza = predicciones[indice_prediccion] * 100

    if confianza < 80:
        return "imposible reconocer", confianza
    else:
        raza_predicha = clases[indice_prediccion]
        return raza_predicha, confianza

def capturar_desde_camara():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return
 
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo capturar el cuadro.")
            break
        frame = cv2.flip(frame, 1)
        raza, confianza = clasificar_imagen(frame)
        texto_raza = f"Raza: {raza}"
        texto_confianza = f"Confianza: {confianza:.2f}%"
        
        # Mostrar información en la ventana
        cv2.putText(frame, texto_raza, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.putText(frame, texto_confianza, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        cv2.imshow('Clasificación en Tiempo Real', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Interfaz gráfica con Tkinter
ventana = Tk()
ventana.title("Clasificación de Perros en Tiempo Real")
ventana.geometry("300x150")
ventana.configure(bg='#f0f0f0')

boton = Button(ventana, text="Abrir Cámara", command=capturar_desde_camara, bg='#007bff', fg='white', font=("Arial", 12), padx=10, pady=5)
boton.pack(pady=20)

ventana.mainloop()
