**Valencia 20 de Sept de 2016**
# Practica de t2d con openacademy


Paso 1: Generar los scripts de t2d

> $t2d git@github.com:jorgescalona/openacademy-project.git master

lo que resulta en:

['/home/jorgeluis/.t2d/script/git_github.com_jorgescalona_openacademy-project.git/master/1', 
'/home/jorgeluis/.t2d/script/git_github.com_jorgescalona_openacademy-project.git/master/2']

luego entrando al path para generar las pruebas de lint y se ejecuta:

> $./10-build.sh --no-cache

esté ultimo genera la imagen docker tal cual se ve en la imagén:

![Construyendo la docker images con 10-build](https://attakatara.files.wordpress.com/2016/09/t2d_img11.png "Construyendo la docker image con 10-build")

Seguidamente podemos verificar la correcta creación de la docker images con:

>$docker images

![listando las imagenes docker la nuestra con el tag master_1](https://attakatara.files.wordpress.com/2016/09/t2d_img21.png "Listando las imagenes docker la muestra con el master_1")

Luego si hacemos cat sobre 20-run.sh, podemos observar que el script convierte el nombre de la docker image en una variable de entorno llamada IMAGE y luego ejecuta un docker run sobre la misma es allí donde podemos editar el parámetro $1 con la finalidad de inyectar configuraciones deseadas en nuestro caso --name="name_description" y --entrypoint=bash para que ejecute una consola interactiva y modo attach sobre el contenedor como se muestra:

![docker run con name=test_openaca_jlescalona y entrypoint=bash](https://attakatara.files.wordpress.com/2016/09/t2d_img31.png "docker run con name=test_openaca_jlescalona y entrypoint=bash")

una vez dentro del contenedor ejecutamos:

>$/entrypoint.sh

con lo que corren las pruebas de lint una vez culminadas las mismas deben aparecer Sucssess en verde como se muestra:

![Pruebas LINT Sucsess jorgescalona/openacademy-project](https://attakatara.files.wordpress.com/2016/09/t2d_img41.png "Pruebas LINT Sucsess jorgescalona/openacademy-project")


Para la siguientes pruebas de Odoo se siguen pasos similes a los arriba expuestos cambiandonos al segundo path generado: ~/.t2d/script/git_github.com_jorgescalona_openacademy-project.git/master/2 y corriendo 10-build.sh y 20-run.sh respectivamente, con lo que se obtiene de forma ideal el siguiente, resultado:


![Pruebas Odoo Sucsess jorgescalona/openacademy-project](https://attakatara.files.wordpress.com/2016/09/t2d_img51.png "Pruebas Odoo Sucsses jorgescalona/openacademy-project")

