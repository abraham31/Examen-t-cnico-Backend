## Forma de consumo.

# Requisitos Previos:
Docker y Git

# Instalacion y uso.
1. Clona este repositorio en tu máquina local:
2. Entra al directorio del proyecto "pyCoppel-AbrahamSoto"
3. Construye la imagen del contenedor Docker:
       docker build -t nombre-imagen .
4. verifica que se creo y el nombre de la imagen.
       docker images
6. Ejecuta el contenedor Docker:
       docker run -it -p 8000:8000 nombre-imagen
7. Abre tu navegador web y accede a la aplicación en la siguiente dirección:
        http://localhost:8000/docs
8. Comprueba los endpoint     
