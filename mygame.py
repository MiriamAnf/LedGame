import time
import random
from umqtt.simple import MQTTClient
from miscelanea import LedRGB, Button

''' 
El juego consiste en lo siguiente:
    - El led se encenderá después de un tiempo que varía entre 1 y 5 segundos. Cada vez lo hará de un color diferente, de manera aleatoria (función en miscelánea.py)
    - Se cuenta el tiempo desde que el led se enciende (start) hasta que se pulsa el botón (stop).
    - Hay 5 intentos. Las puntuaciones de los 5 aparcen en la terminal.
    - La mejor puntuación de las 5 obtenida se publica en hivemq.com 
'''

USER = 'dga3ha2'
BROKER = 'broker.hivemq.com'
GROUP_NAME = b'JuegoIOT'
scores = []
real_scores = []

class Game:
    def __init__(self, name):
        self.name = name
        self.led = LedRGB()
        self.button = Button(39)
        self.client = MQTTClient(USER, BROKER)
        self.client.connect()
                       
    def switch_led_on(self):
        ''' Enciende el led de un color elegido aleatoriamente después de pasar entre 1 y 5 segundos ''' 
        random_time = random.randrange(1000, 5000)
        time.sleep_ms(random_time)
        self.led.encender()

    def switch_led_off(self, start):
        ''' Guarda el tiempo que se ha tardado en pulsar el botón y apaga el led, guardando el tiempo en la lista scores '''
        stop = time.ticks_ms()
        self.led.apagar()
        score = stop - start
        scores.append(score/1000)   
        
    def publish_score(self):
        ''' Guarda los tiempos reales en la lista real_scores y publica la mejor puntuación '''
        for i in range(len(scores)-1):
            real_scores.append(scores[i+1]-scores[i])
        print(real_scores)    
        self.client.publish(GROUP_NAME, self.scores_to_json())

    @staticmethod
    def scores_to_json():
        ''' Ordena las puntuaciones reales de menor a mayor tiempo y formatea la primera para que sea el mensaje publicado '''
        real_scores.sort()
        best_score = real_scores[0]
        json = '{"score":' + str(best_score) + '}'
        return json


