# Buffer

Esta es una aplicación que gestiona la información al interior de un [buffer](https://www.geeknetic.es/Buffer/que-es-y-para-que-sirve]) a través de cache con la ayuda de [redis](https://redis.io/), esta permite la consulta, inserción y extracción utilizando [FIFO](https://www.noegasystems.com/blog/logistica/fifo-y-lifo-tecnicas-de-almacenaje) y [LIFO](https://www.noegasystems.com/blog/logistica/fifo-y-lifo-tecnicas-de-almacenaje)

## Documentación
1. Documentación en postman (colección): https://documenter.getpostman.com/view/6886787/2s93RTSYX7
2. Servidor: http://157.230.85.83:5000

## Uso
La app cuenta con 3 métodos:
1. Obtener el buffer: [Request en postman](https://documenter.getpostman.com/view/6886787/2s93RTSYX7#e9dc94bc-2d4e-4368-81f3-9d35b4364ec0)
2. Insertar un elemento al buffer: [Request en postman](https://documenter.getpostman.com/view/6886787/2s93RTSYX7#4f518ffc-9476-4df8-bb8d-101c0fbce1f6), acepta la inserción de elementos uno a uno, estos a través de la variable `message` aceptando los tipos = `int`, `float` o `str` 
3. Extraer un elemento del buffer: [Request en postman](https://documenter.getpostman.com/view/6886787/2s93RTSYX7#e411732c-d417-41d9-81f7-0138ca67b107), acepta dos posibles valores para `policy` = `FIFO` y `LIFO`, no es sensible a mayúsculas o minúsculas

## Despliegue en ambiente local
### Requerimientos
1. windows v11 64 bits
2. docker

### Instrucciones
1. Crear el archivo `.env` con la llave secreta
![env.png](app%2Fviews%2Fstatic%2Fenv.png)
2. Crear imagen y contenedor de docker con el comando `docker-compose up`


#### By Luis Santa