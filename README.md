# ci-cd-flask

## Creamos un virtualenv en Python

```
python3 -m venv venv
```

Lo activamos.

```
source venv/bin/activate
```
Asi tiene que aparecer

![alt text](img/image1.png)

Instalamos las dependencias que estas en `requirements.txt`.

```
pip install -r requirements.txt
```
Asi tiene que aparecer

![alt text](img/image2.png)

Para desactivar el entorno.

```
deactivate
```

## Hacemos el Test

En nuestro repositorio de `GitHub`, en la opción actions, le damos en `New workflow` para hacer el test.

![alt text](img/image3.png)


### build 
Y asi debería de salir  con el check en verde para tenerlo bien.

![alt text](img/image.png)
