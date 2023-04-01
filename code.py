from config import *
from przydatne_funkcje import *

#############USTAWIENIE CZUJNIKA#############
dht = config_dht()
temperature = dht.temperature
humidity = dht.humidity
#############USTAWIENIE EKRANU#############
splash = config_SSD1306()

TEXT1 = f'{"Temperatura":<{11}} {temperature}'
text_area_0 = label.Label(terminalio.FONT, text=TEXT1, color=0xFFFFFF, x=2, y=6)
splash.append(text_area_0)

TEXT2 = f'{"Wilgotnosc":<{11}} {humidity}{"%"}'
text_area_1 = label.Label(terminalio.FONT, text=TEXT2, color=0xFFFFFF, x=2, y=20)
splash.append(text_area_1)
#############USTAWIENIE GUZIKA#############
btn = config_port(board.GP15, in_or_out=True)
btn_last = False
#############USTAWIENIE LED#############
led = config_port(board.LED)


while True:
    temperature = dht.temperature
    humidity = dht.humidity
    text_area_0.text = f'{"Temperatura":<{11}} {temperature}'
    text_area_1.text = f'{"Wilgotnosc":<{11}} {humidity}{"%"}'
    if btn.value==True and btn_last==False:
        desc = "Na dworze jest "+checkTemperature(temperature)+" i "+checkHumidity(humidity)+"\n"
        saveToFile("dane.csv", temperature, humidity, desc)
    blink(led)
    btn_last = btn.value
    time.sleep(0.5)
