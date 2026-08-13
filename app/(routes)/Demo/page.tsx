"use client";
import React, { useState } from 'react';
import MotionTransition from '@/components/transition-component';
import TransitionPage from '@/components/transition-page';
import CoverParticles from "@/components/cover-particles";

const DragDropImage = () => {
  const [imagen, setImagen] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [resultado, setResultado] = useState<string>('');
  const [porcentaje, setPorcentaje] = useState<number>(0);

  // Manejar el drop de archivo
  const manejarDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];

    if (file && file.type.startsWith('image/')) {
      setImagen(file);
      setPreview(URL.createObjectURL(file));
    } else {
      alert('Solo se permiten archivos de imagen.');
    }
  };

  // Prevenir el comportamiento por defecto del dragover
  const manejarDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
  };

  // Abre el explorador de archivos al hacer clic
  const abrirExploradorArchivos = () => {
    document.getElementById('fileInput')?.click();
  };

  // Manejar la selección de archivo desde el explorador
  const manejarArchivoSeleccionado = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files ? e.target.files[0] : null;
    if (file && file.type.startsWith('image/')) {
      setImagen(file);
      setPreview(URL.createObjectURL(file));
    } else {
      alert('Solo se permiten archivos de imagen.');
    }
  };

  // Enviar la imagen al backend para su análisis
  const analizarImagen = async () => {
    if (imagen) {
      const formData = new FormData();
      formData.append('file', imagen);

      const response = await fetch('http://127.0.0.1:5000/analizar', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data);
        setResultado(data.raza);         
        setPorcentaje(data.porcentaje);  
      } else {
        alert('Error en la predicción');
      }
    } else {
      alert('Por favor, selecciona una imagen primero.');
    }
  };

  return (
    
    <div
      className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white"
      style={{
        background:
          'linear-gradient(90.21deg, rgba(246, 108, 191, 0.345) -5.91%, rgba(9, 0, 48, 0.998) 111.58%)',
      }}
    >
      <TransitionPage />
      
      <MotionTransition position="right">
        <br />
        <div className="text-2xl leading-tight text-center md:text-2xl mt-35">
          <h1>Cargue o arrastre una imagen para empezar con el análisis</h1>
        </div>

        <div
          onDrop={manejarDrop}
          onDragOver={manejarDragOver}
          onClick={abrirExploradorArchivos} // Al hacer clic, abrirá el explorador
          className="border-4 border-dashed border-white w-175 h-140 flex items-center justify-center rounded-lg cursor-pointer hover:bg-white/10 transition mt-20"
        >
          {preview ? (
            <img
              src={preview}
              alt="Previsualización"
              className="object-cover w-full h-full rounded"
            />
          ) : (
            <p className="text-center">Arrastra una imagen aquí</p>
          )}
        </div>
      </MotionTransition>

      {imagen && (
        <p className="mt-4 text-sm text-gray-300">
          Archivo: <strong>{imagen.name}</strong>
        </p>
      )}

      <input
        id="fileInput"
        type="file"
        accept="image/*"
        className="hidden"
        onChange={manejarArchivoSeleccionado} // Maneja la selección de archivos desde el explorador
      />

      {resultado && (
        <div className="mt-4 text-sm text-gray-300">
          <p>Raza predicha: <strong>{resultado}</strong></p>
          <p>Certeza: <strong>{porcentaje.toFixed(2)}%</strong></p>
        </div>
      )}

      <br />
      <br />
      <br />
      <div className="flex item-center justify-center gap-3 md:justify-start md:gap-10">
        <button
          onClick={analizarImagen}
          className="px-3 py-2 transition-all border-2 cursor-pointer text-md w-fit rounded-xl hover:shadow-xl hover:shadow-white/50"
        >
          Analizar
        </button>
      </div>
      <br />
      <a href="/" className= "text-grey">Regresar</a>
      <br />
      <br />
      <br />
    </div>
    
  );
};

export default DragDropImage;
