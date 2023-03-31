# Buffer

Esta aplicación implementa un [buffer](https://www.geeknetic.es/Buffer/que-es-y-para-que-sirve]) para la inserción, extracción y consulta del mismo

## Documentación
1. Documentación: https://documenter.getpostman.com/view/6886787/2s93RTSYX7
2. Servidor: http://157.230.85.83:5000

## Uso
La app cuenta con 3 métodos:
1. Obtener el buffer: [documentación](https://documenter.getpostman.com/view/6886787/2s93RTSYX7#e9dc94bc-2d4e-4368-81f3-9d35b4364ec0)
2. Insertar un elemento al buffer: [documentación](https://documenter.getpostman.com/view/6886787/2s93RTSYX7#4f518ffc-9476-4df8-bb8d-101c0fbce1f6), acepta la inserción de elementos uno a uno, estos a travez de la variable `message` aceptando los tipos = `int`, `float` o `str` 
3. Extraer un elemento del buffer: [documentación](https://documenter.getpostman.com/view/6886787/2s93RTSYX7#e411732c-d417-41d9-81f7-0138ca67b107), acepta dos posibles valores para `policy` = `FIFO` y `LIFO`, es agnóstico a mayusculas o minusculas

## Despliegue en ambiente local
### Requerimientos
1. windows v11 64 bits
2. python v3.10
3. flask latest 
4. flask-cors latest 
5. python-dotenv v1.0.0

### Instrucciones
1. Crear el archivo `.env` con la llave secreta
![env.png](app%2Fviews%2Fstatic%2Fenv.png)
2. Crear entorno virtual con el comando `py -m venv venv`  
3. Activar entorno virtual con el comando `venv\Scripts\active`
4. Instalar dependencias con el comando `pip install -r requirements.txt`
5. Iniciar el proyecto con el comando `flask run`

#
#### By Luis Santa