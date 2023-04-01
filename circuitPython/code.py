from config import *
from przydatne_funkcje import *
from Interval import Interval
import asyncio
#############KONFIGURACJA#########################################################
#############USTAWIENIE CZUJNIKA#############
dht = config_dht()
#############USTAWIENIE EKRANU#############
splash = config_SSD1306()

TEXT1 = f'{"Temperatura":<{11}} {0}C'
text_area_0 = label.Label(terminalio.FONT, text=TEXT1, color=0xFFFFFF, x=2, y=6)
splash.append(text_area_0)

TEXT2 = f'{"Wilgotnosc":<{11}} {0}{"%"}'
text_area_1 = label.Label(terminalio.FONT, text=TEXT2, color=0xFFFFFF, x=2, y=20)
splash.append(text_area_1)
#############USTAWIENIE GUZIKA#############
btn = config_port(board.GP15, in_or_out=True)
btn_last = False
#############USTAWIENIE LED#############
led = config_port(board.LED)
#################################################################################

async def main():
    interval_1 = Interval(0.5)  # Do obsługi Wilgotności
    interval_2 = Interval(1)    # Do obsługi Temperatury
    interval_3 = Interval(0.25) # Do obsługi diody
    count = 5

    hum_task = asyncio.create_task(calculate_value(dht, count, interval_1, "hum"))
    temp_task = asyncio.create_task(calculate_value(dht, count, interval_2, "temp"))
    led_task = asyncio.create_task(blink(led, interval_3, 20))

    hum = await hum_task
    temp = await temp_task

    await led_task

    print("Temperatura: {}C  Wilgotność: {}%".format(temp, hum))

    desc = "Na dworze jest "+checkTemperature(temp)+" i "+checkHumidity(hum)+"\n"
    try:
        saveToFile("dane.csv", temp, hum, desc)
    except:
        print("Nie można zapisać plików na urządzeniu!")

    return temp, hum


while True:
    temperature, humidity = asyncio.run(main())
    text_area_0.text = f'{"Temperatura":<{11}} {temperature}C'
    text_area_1.text = f'{"Wilgotnosc":<{11}} {humidity}{"%"}'
