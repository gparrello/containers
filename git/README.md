# Gitea_Drone_deploy

## Datos del sistema

Distribución: Ubuntu 20.04
IP del sistema anfitrion: 10.1.6.100/24

## Instalar docker
Desde la URL https://docs.docker.com/get-docker/ podemos ver las diferentes instalaciones para cada sistema operativo. Para este caso como tenemos Ubuntu (Linux) seguimos la guia oficial  https://docs.docker.com/engine/install/ubuntu/

## Instalar docker-compose
Otro requisito para desplegar según esta gui es Docker-compose.

Se puede instalar según la guia de instalación de docker-compose https://docs.docker.com/compose/install/  aunque si tienes python y pip instalado solo debes ejecutar <code>pip install docker-compose</code> en tu sistema y lo tendrás instalado.

## Descargar el fichero de docker-compose

```
git clone https://github.com/AprendeIT/Gitea_Drone_deploy.git
cd Gitea_Drone_deploy
```

## Configurar RPC secret

Para generarlo debes ejecutar:

```
root@dockertesting:~## openssl rand -hex 16
55f24eb3d61ef6ac5e83d550178638dc
```
En este caso `55f24eb3d61ef6ac5e83d550178638dc` es el codigo.


## Configurar

Para configurar correctamente drone debemos modificar el fichero `docker-compose.yml` y debemos incluir el *secreto* generado anteriormente en la clave:
```
    - DRONE_RPC_SECRET=55f24eb3d61ef6ac5e83d550178638dc
```
Por otro lado debemos seleccionar el usuario administrador:
```
- DRONE_ADMIN=gerardo.garcia
    - DRONE_USER_CREATE=username:gerardo.garcia,admin:true
```

Debemos modificar las claves 
```
    - DRONE_SERVER_HOST=10.1.6.100
    - DRONE_HOST=http://10.1.6.100:8080
```

Y el usuario admin, que esn mi caso es:

```
    - DRONE_USER_CREATE=username:gerardo.garcia,admin:true

```
## Levantar contenedores
Levantamos los contenedores
```
root@dockertesting:~/gitea-drone-mysql## docker-compose up -d
Creating network "giteanet" with the default driver
Creating volume "gitea-drone-mysql_gitea" with default driver
Creating volume "gitea-drone-mysql_db" with default driver
Creating volume "gitea-drone-mysql_drone" with default driver
Creating volume "gitea-drone-mysql_drone-agent" with default driver
Pulling db (mysql:5.7)...
5.7: Pulling from library/mysql
6ec7b7d162b2: Pull complete
fedd960d3481: Pull complete
7ab947313861: Pull complete
64f92f19e638: Pull complete
3e80b17bff96: Pull complete
014e976799f9: Pull complete
59ae84fee1b3: Pull complete
7d1da2a18e2e: Pull complete
301a28b700b9: Pull complete
979b389fc71f: Pull complete
403f729b1bad: Pull complete
Digest: sha256:d4ca82cee68dce98aa72a1c48b5ef5ce9f1538265831132187871b78e768aed1
Status: Downloaded newer image for mysql:5.7
Pulling gitea (gitea/gitea:latest)...
latest: Pulling from gitea/gitea
05e7bc50f07f: Pull complete
4d5756e732c2: Pull complete
41d094eec6a2: Pull complete
bdba2d120201: Pull complete
a563aa38e376: Pull complete
b3dc31533e3c: Pull complete
Digest: sha256:e2ce238836d32cd5be4586dbcec7541ccbfaf8e4840d8b761518bf8538234af1
Status: Downloaded newer image for gitea/gitea:latest
Pulling drone-server (drone/drone:1.2.1)...
1.2.1: Pulling from drone/drone
e7c96db7181b: Pull complete
de231fbdcaac: Pull complete
343cd29402df: Pull complete
Digest: sha256:9073d1aa1ef30e25e048c4b4d309c0abd16d3fed6d2eb258f9eb8e89b4085001
Status: Downloaded newer image for drone/drone:1.2.1
Pulling drone-agent (drone/agent:1.2.1)...
1.2.1: Pulling from drone/agent
e7c96db7181b: Already exists
3d5cf113237f: Pull complete
7c2212960ee8: Pull complete
Digest: sha256:f1fea9affd6a48626f7eb17b9cdf41f04d71881fd671c372129a488fa0438a96
Status: Downloaded newer image for drone/agent:1.2.1
Creating gitea ... done
Creating db           ... done
Creating drone-server ... done
Creating drone-agent  ... done
root@dockertesting:~/gitea-drone-mysql## 

```


## Añadir usuario a gitea

Nos registramos en gitea para poder crear repos y autenticar desde *drone*. Es importante crear el usuario que hemos especificado que será admin en la config de *Drone*, en las siguientes lineas de docker-compose.yml:

```
- DRONE_ADMIN=gerardo.garcia
    - DRONE_USER_CREATE=username:gerardo.garcia,admin:true
```

## Añadir repositorio de prueba en gitea

Añadimos un repo de prueba en gitea para verificar que podemos añadir repositorios y sincronizar *drone*


## Añadir fichero de drone al repo

fichero `.drone.yml`:

```
kind: pipeline
name: hello-world
type: docker

steps:
  - name: say-hello
    image: busybox
    commands:
     - echo hello-world
```

## Hacer login en drone

Hacer login en drone con el usuario que hemos creado en GITEA

## Activar CI/CD en el repo

Desde drone activamos el CI/CD en el repo

Añadir al `Readme.md` el codigo que te facilita drone durante la activación del repo

## Ejecutar un merge de prueba

Para verificar que los pipelines funcionan bien, ejecuta un merge de una rama a master o crea en master un fichero desde gitea, si todo está bien se ejecutará el pipeline y se realizará el merge o bien se creará el fichero.

## Troubleshotting 

Problemas al hacer login en Drone: Eliminar token desde el usuario que falla en el panel de gitea, para ello:

-  Accede a gitea con el usuario que falla
- Dirigete a configuracion de usuario
- Pincha en aplicaciones y borra el token *Drone*



Mas información en https://aprendeit.com/como-montar-un-gitea-con-ci-cd-con-drone


