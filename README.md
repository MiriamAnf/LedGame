# LedGame
 Miniproject IOT

El proyecto consiste en lo siguiente:

	Parte 1 

	- Un juego donde, transcurrido un tiempo aleatorio, el led se enciende y se empieza a contar el tiempo.
	- Cuando se presiona el botón central, el led se apaga y se calcula el tiempo que ha transcurrido desde que 	se encendió.

	Parte 2

	- La mejor puntuación obtenida en 5 intentos, se publica mediante MQTT 
	- Se usa el broker hivemq.com y el topic "JuegoIOT"


**NOTAS**

El botón del dispositivo no funciona correctamente. Al conectarse a internet, la lógica empleada para pulsar el botón es negativa, mientras que, si no está conectado a internet, la lógica es positiva. 

Por ello, puede ser necesario realizar este cambio en la línea 10 de main.py. 

`if juego.button.get_pulsado() == False:` funciona si el dispositivo está conectado a internet

`if juego.button.get_pulsado():` funciona si el dispositivo **no** está conectado a internet

