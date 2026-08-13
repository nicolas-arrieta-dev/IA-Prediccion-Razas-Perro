import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from tkinter import Tk, filedialog, Button, Label, Frame, messagebox

# Cargar el modelo
model = load_model('modelo_perros.h5')

# Clases de perros
clases = ["Beagle", "Bulldog frances", "Chihuahua", "Dalmata", "Doberman", "Dogo argentino", "Golden retriever", "Lobo siberiano", "Pastor aleman", "Rottweiler"]

def clasificar_imagen(ruta_imagen):
    img = image.load_img(ruta_imagen, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predicciones = model.predict(img_array)[0]
    indice_prediccion = np.argmax(predicciones)
    
    if indice_prediccion < len(clases):
        raza_predicha = clases[indice_prediccion]
        confianza = predicciones[indice_prediccion] * 100
        #if confianza < 52:
         # raza_predicha = "No es posible predecir bien "
        
        mostrar_resultado(ruta_imagen, raza_predicha, confianza)

        
    else:
        messagebox.showerror("Error", "Predicción fuera de rango.")

def mostrar_resultado(ruta_imagen, raza, confianza):
    # Cargar la imagen
    img = cv2.imread(ruta_imagen)
    img = cv2.resize(img, (400, 400))

    # Agregar texto con saltos de línea
    texto = [f"Raza: {raza}", f"Confianza: {confianza:.2f}%"]
    y_offset = 30
    for linea in texto:
        cv2.putText(img, linea, (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        y_offset += 40

    # Mostrar imagen
    cv2.imshow('Resultado', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def seleccionar_imagen():
    ruta_imagen = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imágenes", "*.jpg;*.jpeg;*.png")])
    if ruta_imagen:
        clasificar_imagen(ruta_imagen)

# Interfaz con Tkinter
ventana = Tk()
ventana.title("Clasificación de Perros")
ventana.geometry("300x150")
ventana.configure(bg='#f0f0f0')

frame = Frame(ventana, bg='#ffffff', padx=20, pady=20)
frame.pack(expand=True)

label = Label(frame, text="Clasificador de Razas de Perros", font=("Arial", 12), bg='#ffffff')
label.pack(pady=10)

boton = Button(frame, text="Seleccionar Imagen", command=seleccionar_imagen, bg='#007bff', fg='white', font=("Arial", 10), padx=10, pady=5)
boton.pack()

ventana.mainloop()
