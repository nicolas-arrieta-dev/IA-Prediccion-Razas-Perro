# IA-Prediccion-Razas-Perro

Sistema de inteligencia artificial capaz de analizar imágenes de perros y predecir su raza mediante un modelo de visión por computadora entrenado durante el desarrollo del proyecto.

El modelo fue desarrollado y entrenado utilizando un dataset de imágenes recopilado y preparado durante el desarrollo del proyecto. La aplicación integra el modelo de IA con una interfaz web moderna desarrollada con Next.js, permitiendo al usuario cargar imágenes y obtener una predicción de la raza del perro.

## Descripción

El proyecto combina un frontend desarrollado con Next.js y un backend de inteligencia artificial desarrollado en Python.

El modelo de IA fue entrenado utilizando imágenes de diferentes razas de perros. El dataset fue recopilado, organizado y preparado para posteriormente realizar el entrenamiento del modelo.

La aplicación permite enviar una imagen de un perro al servicio de inteligencia artificial, procesarla mediante el modelo entrenado y obtener como resultado la raza predicha.

## Características

- Predicción automática de razas de perros mediante inteligencia artificial.
- Modelo entrenado desde cero durante el desarrollo del proyecto.
- Dataset recopilado y preparado específicamente para el entrenamiento.
- Procesamiento de imágenes mediante Python.
- API desarrollada con Flask para comunicarse con el modelo de IA.
- Integración entre el frontend y el backend mediante API.
- Interfaz web moderna y responsive.
- Animaciones y efectos visuales mediante partículas.
- Carga de imágenes para realizar predicciones.
- Visualización del resultado de la predicción.

## Arquitectura del proyecto

El proyecto está dividido principalmente en dos componentes:

```text
IA-Prediccion-Razas-Perro
│
├── Frontend
│   └── Next.js + React
│
└── IA
    ├── Modelo de inteligencia artificial
    ├── API Flask
    ├── Dataset
    └── Scripts de entrenamiento
```

##Frontend

El frontend fue desarrollado utilizando Next.js, React y TypeScript.

La interfaz incorpora diferentes efectos visuales y animaciones para mejorar la experiencia del usuario, incluyendo un sistema de partículas para la presentación visual de la aplicación.

##Backend de Inteligencia Artificial

El backend de IA fue desarrollado utilizando Python.

El sistema utiliza TensorFlow y Keras para cargar y ejecutar el modelo entrenado.

La comunicación entre la aplicación web y el modelo se realiza mediante una API desarrollada con Flask.

Tecnologías
Frontend
Next.js 15
React 19
TypeScript
Tailwind CSS
Framer Motion
tsparticles
Lucide React
@hello-pangea/dnd
Inteligencia Artificial
Python
TensorFlow
Keras
OpenCV
NumPy
Pillow
Flask
Flask-CORS
Modelo

El modelo de inteligencia artificial fue desarrollado utilizando redes neuronales convolucionales (CNN) para realizar la clasificación de imágenes.

Durante el desarrollo se utilizaron componentes de TensorFlow/Keras como:

Conv2D
MaxPooling2D
Flatten
Dense
Dropout
Adam
ImageDataGenerator

Dataset

Uno de los principales componentes del proyecto fue la creación y preparación del dataset utilizado para entrenar el modelo.

Las imágenes fueron recopiladas y organizadas según las diferentes razas de perros que se querían identificar.

El proceso incluyó:

Recopilación de imágenes.
Organización de las imágenes por categorías.
Preparación del dataset.
Procesamiento de imágenes.
Generación de datos para el entrenamiento.
Entrenamiento y evaluación del modelo.

Debido al tamaño del dataset, las imágenes utilizadas para el entrenamiento no se incluyen directamente en este repositorio.

API de Inteligencia Artificial

El proyecto utiliza Flask para crear una API que permite utilizar el modelo desde el frontend.

La API recibe una imagen, realiza el procesamiento necesario y utiliza el modelo entrenado para obtener la predicción.
se encuentra en el archivo Api_IA.py ese ejecuta ese archivo y esta listo para escuchar las peticiones de la vista
en la carpeta /ia también se encuentran odas los archivos de prueba y los archivos con las instrucciones con las que se entreno el modelo


Instalación
Requisitos

Para ejecutar el proyecto se recomienda tener instalado:

Node.js
npm
Python 3
Git
1. Clonar el repositorio
2. Configurar el frontend
3. npm install
4. npm run dev

Luego en consola
1. cd ia
2. python Api_IA.py

Objetivo del proyecto

El objetivo del proyecto es desarrollar y entrenar un modelo de inteligencia artificial capaz de reconocer diferentes razas de perros a partir de imágenes.

El proyecto busca aplicar conocimientos de inteligencia artificial, visión por computadora, procesamiento de imágenes y desarrollo web, integrando un modelo de aprendizaje automático dentro de una aplicación web.

Además de utilizar un modelo previamente entrenado, una parte importante del proyecto fue la recopilación, organización y preparación del dataset utilizado para realizar el entrenamiento.


The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
