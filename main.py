import time
from mygame import Game, scores


juego = Game('juego_led')
start = time.ticks_ms() 

while True:
    juego.switch_led_on()
    if juego.button.get_pulsado():
        juego.switch_led_off(start)
    if len(scores) > 5:
        break 

juego.publish_score()

