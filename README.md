# practica-pantalla-oled
## **Autores: ** Santiago Patricio Gómez Ochoa A01735171 | Darío Alberto Sánchez Perzabal A01738266
Ejercicio de práctica con las siguientes especificaciones:

Siguiendo el análisis de los puertos de comunicación, vamos a estudiar la funcionalidad y configuración del puerto I2C. Para ello, se requiere de una pantalla OLED de 128x64 píxeles con comunicación I2C.

Es necesario instalar las siguientes librerías en la Raspberry Pi:

```bash
pip3 install adafruit-circuitpython-ssd1306
sudo apt-get install python3-pil
```

Desde la Raspberry Pi, deberá enviarse a la pantalla el nombre completo de los integrantes del equipo de trabajo, y habilitar una opción en la que el usuario, a través del teclado de la computadora conectada a la Raspberry, pueda enviar un mensaje para ser mostrado en la pantalla OLED (no mayor a 50 caracteres).
Es importante que, antes de realizar esta actividad, se hayan revisado los códigos de ejemplo que se incluyen al momento de instalar los drivers para el manejo de la memoria del dispositivo OLED.
