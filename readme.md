# Configuración del Entorno

## Crear y Activar un Entorno Virtual: 
En la raíz del proyecto, crea un entorno virtual y actívalo. Esto te permitirá tener un entorno de Python aislado para este proyecto.
    1. pip install virtualenv
    2. virtualenv venv
    3. .\venv\Script\activate.ps1 (utilizando la terminal power shell).

## Instalar los requerimientos:
Ejecuta el siguiente comando dentro del proyecto.
    1. pip install -r .\requirements.txt

# Dos formas de ejecutar fastapi
    1. uvicorn main:app
# O
    2. Agregar las lineas de codigo
        if __name__=="__main__":
            uvicorn.run("main:app",port=8000)
            
        Y luego correr main.py

# Documentacion y pruebas por SWAGGER
    Enlace: http://localhost:8000/docs