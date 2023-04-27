#Quiero crear un dockerfile para dockerizar mi aplicación

#1. Seleccionar la imagen base
FROM python:3.8

#2. Definir el directorio de trabajo
WORKDIR /app

#3. Copiar el archivo de requerimientos
COPY requirements.txt .

#4. Instalar los requerimientos
RUN pip install -r requirements.txt

#5. Copiar el código de la aplicación
COPY . .

#7. Definir el comando de ejecución
CMD bash -c "while true; do sleep 3600; done"

