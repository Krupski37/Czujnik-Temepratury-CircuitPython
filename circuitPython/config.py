import adafruit_displayio_ssd1306, adafruit_dht
import board, busio, displayio, os, terminalio, time, digitalio
from adafruit_display_text import label

def config_dht():
    dht = adafruit_dht.DHT11(board.GP28)
    return dht

def config_SSD1306():
    displayio.release_displays()

    SDA, SCL = board.GP4, board.GP5
    I2C = busio.I2C(SCL, SDA)
    display_bus = displayio.I2CDisplay(I2C, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

    splash = displayio.Group()
    display.show(splash)

    color_bitmap = displayio.Bitmap(128, 64, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    ## Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(126, 62, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black

    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=1)
    splash.append(inner_sprite)
    return splash

def config_port(pin, in_or_out=False):
    port = digitalio.DigitalInOut(pin)
    if in_or_out:
        port.direction = digitalio.Direction.INPUT
    else:
        port.direction = digitalio.Direction.OUTPUT

    return port
