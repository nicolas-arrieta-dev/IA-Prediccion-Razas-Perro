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
IA-Prediccion-Razas-Perro/
│
├── Frontend/
│   └── Next.js + React
│
└── ia/
    ├── Modelo de inteligencia artificial
    ├── API Flask
    ├── Dataset
    └── Scripts de entrenamiento
```

## Frontend

El frontend fue desarrollado utilizando **Next.js, React y TypeScript**.

La interfaz incorpora diferentes efectos visuales y animaciones para mejorar la experiencia del usuario, incluyendo un sistema de partículas para la presentación visual de la aplicación.

## Backend de Inteligencia Artificial

El backend de IA fue desarrollado utilizando **Python**.

El sistema utiliza **TensorFlow y Keras** para cargar y ejecutar el modelo entrenado.

La comunicación entre la aplicación web y el modelo se realiza mediante una API desarrollada con **Flask**.

## Tecnologías utilizadas

### Frontend

- Next.js 15
- React 19
- TypeScript
- Tailwind CSS
- Framer Motion
- tsParticles
- Lucide React
- @hello-pangea/dnd

### Inteligencia Artificial y Backend

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pillow
- Flask
- Flask-CORS

## Modelo de Inteligencia Artificial

El modelo de inteligencia artificial fue desarrollado utilizando **redes neuronales convolucionales (CNN)** para realizar la clasificación de imágenes.

Durante el desarrollo se utilizaron diferentes componentes de TensorFlow/Keras, entre ellos:

- Conv2D
- MaxPooling2D
- Flatten
- Dense
- Dropout
- Adam
- ImageDataGenerator

El modelo recibe una imagen como entrada, realiza el procesamiento correspondiente y genera una predicción sobre la raza del perro.

## Dataset

Uno de los principales componentes del proyecto fue la creación y preparación del dataset utilizado para entrenar el modelo.

Las imágenes fueron recopiladas y organizadas según las diferentes razas de perros que se querían identificar.

El proceso incluyó:

1. Recopilación de imágenes.
2. Organización de las imágenes por categorías.
3. Preparación del dataset.
4. Procesamiento de imágenes.
5. Generación de datos para el entrenamiento.
6. Entrenamiento y evaluación del modelo.

Debido al tamaño del dataset, las imágenes utilizadas para el entrenamiento no se incluyen directamente en este repositorio.

## API de Inteligencia Artificial

El proyecto utiliza **Flask** para crear una API que permite utilizar el modelo de inteligencia artificial desde el frontend.

La API recibe una imagen, realiza el procesamiento necesario y utiliza el modelo entrenado para obtener la predicción.

El servicio se encuentra en:

```text
ia/Api_IA.py
```

El archivo `Api_IA.py` es el punto de entrada de la API. Al ejecutarlo, el servicio queda disponible para recibir las peticiones realizadas desde la aplicación web.

Dentro de la carpeta `ia/` también se encuentran los archivos utilizados durante el desarrollo del proyecto, incluyendo archivos de prueba, scripts y archivos con las instrucciones y configuraciones utilizadas para entrenar el modelo.

## Instalación

### Requisitos

Para ejecutar el proyecto se recomienda tener instalado:

- Node.js
- npm
- Python 3
- Git

## 1. Clonar el repositorio

```bash
git clone https://github.com/nicolas-arrieta-dev/IA-Prediccion-Razas-Perro.git
```

Ingresar a la carpeta del proyecto:

```bash
cd IA-Prediccion-Razas-Perro
```

## 2. Configurar el Frontend

Instalar las dependencias:

```bash
npm install
```

Ejecutar el proyecto:

```bash
npm run dev
```

El frontend estará disponible normalmente en:

```text
http://localhost:3000
```

## 3. Ejecutar la API de Inteligencia Artificial

Abrir otra terminal y dirigirse a la carpeta `ia`:

```bash
cd ia
```

Ejecutar la API:

```bash
python Api_IA.py
```

Una vez ejecutado `Api_IA.py`, el backend de inteligencia artificial queda disponible para recibir las peticiones realizadas por el frontend.

## Flujo de funcionamiento

El funcionamiento general de la aplicación es:

```text
┌────────────────────────────┐
│      Usuario               │
│   Carga una imagen         │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│      Next.js Frontend      │
│       localhost:3000       │
└─────────────┬──────────────┘
              │
              │ HTTP / API
              ▼
┌────────────────────────────┐
│       Flask API            │
│       Api_IA.py            │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│      Modelo CNN            │
│    TensorFlow / Keras      │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│   Raza predicha            │
└────────────────────────────┘
```

## Objetivo del proyecto

El objetivo del proyecto es desarrollar y entrenar un modelo de inteligencia artificial capaz de reconocer diferentes razas de perros a partir de imágenes.

El proyecto busca aplicar conocimientos de:

- Inteligencia artificial.
- Aprendizaje automático.
- Visión por computadora.
- Procesamiento de imágenes.
- Redes neuronales convolucionales.
- Desarrollo de APIs.
- Desarrollo web.
- Integración entre modelos de IA y aplicaciones web.

Además de utilizar el modelo entrenado, una parte importante del proyecto fue la recopilación, organización y preparación del dataset utilizado para realizar el entrenamiento.

