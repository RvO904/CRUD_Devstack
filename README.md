# CRUD en instancia de Devstack

El presente proyecto consiste de la implementación de un CRUD básico en una instancia de Devstack

Para tales fines, los requisitos mínimos de la computadora que esté corriendo una instancia de Devstack idealmente serían 4 núcleos de procesador y 4 GB de RAM

En mi caso, para evitar un dual boot en mi computadora principal, preferí instalar una máquina virtual, a continuación las especificaciones de la máquina virtual y de la computadora anfitriona

## Especificaciones del host
- 32 GB de RAM
- Procesador Ryzen 5 5500 (6 núcleos, 12 hilos)
- NVidia GeForce RTX 4060
- S.O Windows 11

## Especificaiones de la máquina virtual
- 9 GB de RAM
- 5 núcleos de procesador
- 12 MB de Memoria de video
- S.O Ubuntu 20.04.6

El motivo principal del uso de Ubuntu 20.04.6 es por los problemas de compatibilidad de Devstack con otras versiones posteriores de Ubuntu

## Devstack Yoga
Esta es una versión de Devstack que ya no se encuentra en mantenimiento, pero que funciona perfectamente para Ubuntu 20.04.6

## Resumen de pasos para la instalación de Devstack
1. Después de instalar Ubuntu, de ser necesario, instalar vim y git
2. Clonar el repositorio de Git de Devstack sabor Yoga a través del siguiente comando: ```git clone https://opendev.org/openstack/devstack -b unmaintained/yoga```
3. Una vez clonado el repositorio, se deberá usar el siguiente comando: cd devstack. Esto es con el fin de entrar a la carpeta de Devstack
4. Usar el comando "ip a" con el fin de obtener la dirección IP asignada a la máquina virtual
5. Dentro de la carpeta de Devstack, se deberá crear con vim un archivo con el nombre "local.conf", los contenidos mínimos de este archivo son los siguientes
    ```
    [[local|localrc]]
    ADMIN_PASSWORD=**Poner una contraseña para acceder a devstack**
    DATABASE_PASSWORD=$ADMIN_PASSWORD
    RABBIT_PASSWORD=$ADMIN_PASSWORD
    SERVICE_PASSWORD=$ADMIN_PASSWORD
    HOST_IP=**Colocar aqui el IP obtenido en el paso anterior**
    ```
6. Una vez el archivo esté creado, se deberá ejecutar el siguiente comando para hacer la instalación de Devstack: ```. /stack.sh```
7. El proceso de instalación de Devstack puede tomar de 15 a 30 minutos, una vez termine, se podrá acceder al dashboard de Horizon con el usuario "admin" y la contraseña que se asignó en el archivo local.conf

## ¿Qué hacer después de la instalación de Devstack?
Lo primero que se debe de hacer es buscar una imagen minimal de ubuntu con el fin de instalarla en la instancia que se va a correr, la recomendación para el uso de programas en Python es que la imagen mínima 
de ubuntu sea como mínimo la 20.06, esto es porque en mi caso se cometió el error de instalar la versión 16.04, la cual tiene Python 3.2, lo cual generó múltiples problemas de compatibilidad con algunas de las 
dependencias que se intentaron utilizar y fue necesario instalar Python 3.8 de manera manual

### Recomendaciones para el CRUD
Si la aplicación web permite la asignación de la IP y puerto, **asignar siempre la IP "0.0.0.0"**, esto es con el fin de que para conectarnos al CRUD se utilice la IP flotante de nuestra instancia en el puerto 
especificado

Por parte del puerto, **siempre asegurarse de establecer una regla de seguridad** para que se establezca exitosamente una conexión hacia tal puerto desde el navegador, de tal manera que podamos establecer conexión
con nuestro CRUD poniendo en nuestro navegador por ejemplo "10.0.5.2:5000"

# Video tutorial para la instalación
Si se desean detalles extra sobre la instalación de Devstack o del CRUD en la instancia ya creada, por favor referirse al siguiente video tutorial: https://www.youtube.com/watch?v=6EwHSw-6Uoc
