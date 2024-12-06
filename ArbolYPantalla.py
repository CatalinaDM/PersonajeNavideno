from machine import SoftSPI, Pin, PWM
from max7219 import Matrix8x8
import time
import network
from umqtt.simple import MQTTClient
import _thread

# Configuración de los pines para SPI y la pantalla MAX7219
max_clk = const(23)
max_cs = const(22)
max_din = const(17)

# Inicializar el SPI con SoftSPI
spi = SoftSPI(sck=Pin(max_clk), mosi=Pin(max_din), miso=Pin(14))

# Inicializar la matriz MAX7219 (8 dispositivos en cascada para una matriz de 64x8)
display = Matrix8x8(spi, Pin(max_cs), 4)  # 8 módulos en cadena para una matriz 64x8
display.brightness(5)  # Ajustar el brillo

# Configuración de los LEDs RGB en cascada
rgb_pins = [
    [Pin(5, Pin.OUT), Pin(4, Pin.OUT), Pin(2, Pin.OUT)],
    [Pin(14, Pin.OUT), Pin(13, Pin.OUT), Pin(12, Pin.OUT)],
    [Pin(16, Pin.OUT), Pin(16, Pin.OUT), Pin(15, Pin.OUT)],
    [Pin(21, Pin.OUT), Pin(19, Pin.OUT), Pin(18, Pin.OUT)],
    [Pin(27, Pin.OUT), Pin(26, Pin.OUT), Pin(25, Pin.OUT)],
]

rgb_pwm = []
for pins in rgb_pins:
    rgb_pwm.append([PWM(pins[0]), PWM(pins[1]), PWM(pins[2])])

# Rango de colores en formato RGB (en niveles PWM)
colors = [
    (1023, 0, 0),      # Rojo
    (0, 1023, 0),      # Verde
    (0, 0, 1023),      # Azul
    (1023, 1023, 0),   # Amarillo
    (0, 1023, 1023),   # Cyan
    (1023, 0, 1023),   # Magenta
    (512, 512, 512),   # Blanco tenue
]

# Función para establecer el color de un LED RGB específico
def set_rgb_color(led, color):
    rgb_pwm[led][0].duty(color[0])
    rgb_pwm[led][1].duty(color[1])
    rgb_pwm[led][2].duty(color[2])

# Función para el efecto de cascada en los LEDs RGB de abajo hacia arriba
def cascada_rgb():
    color_index = 0
    while True:
        for j in range(len(rgb_pwm)):
            set_rgb_color(j, (0, 0, 0))
        
        for i in reversed(range(len(rgb_pwm))):
            set_rgb_color(i, colors[color_index])
            time.sleep(0.1)  # Delay de un segundo entre cada paso de la cascada
            set_rgb_color(i, (0, 0, 0))  # Apagar el LED después de encender el siguiente
        
        color_index = (color_index + 1) % len(colors)

# Función personalizada para desplazar el texto
def scroll_text(text, delay=0.1):
    length = len(text) * 8  # Calcular el tamaño total del texto en píxeles
    for i in range(length + 8):  # Desplazar a través de la matriz
        display.fill(0)  # Limpiar pantalla
        display.text(text, 8 - i, 0, 1)  # Mostrar texto desplazado
        display.show()  # Actualizar pantalla
        time.sleep(delay)

# Configuración de conexión WiFi
def conectar_wifi():
    print("Conectando a WiFi...")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('UTNG_GUEST', 'R3d1nv1t4d0s#UT')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.5)
    print("\nWiFi Conectada!")
    

# Configuración MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = "NeoPixelClient"
MQTT_TOPIC = "gds0643/jfrg/texto"
MQTT_PORT = 1883

# Manejar mensajes MQTT
def llegada_mensaje(topic, msg):
    global texto
    texto = msg.decode()  # Actualiza el texto con el mensaje recibido
    print("Mensaje recibido:", texto)

# Subscribir al broker MQTT
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado a MQTT Broker:", MQTT_BROKER)
    return client

# Iniciar la cascada de LED RGB en un hilo separado
_thread.start_new_thread(cascada_rgb, ())

# Conectar a WiFi
conectar_wifi()

# Iniciar conexión MQTT
client = subscribir()

# Variable global para el texto
texto = "Feliz Navidad!!!"  # Texto inicial

# Iniciar el desplazamiento del texto en un hilo separado
def start_scroll_thread():
    while True:
        scroll_text(texto, 0.08)  # Desplazar el texto actual

_thread.start_new_thread(start_scroll_thread, ())

# Ciclo principal para manejar mensajes MQTT
while True:
    client.wait_msg()
