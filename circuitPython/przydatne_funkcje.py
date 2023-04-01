import asyncio

def checkHumidity(humidity):
    if humidity > 70:
        return "weź parasol"
    elif humidity > 40:
        return "nie potrzebny ci parasol"
    else:
        return "pamiętaj aby pic wode"

def checkTemperature(temperature):
    if temperature > 25:
        return "goraco"
    elif temperature > 15:
        return "przyjemnie"
    else:
        return "zimno"

def saveToFile(fileName, temperature, humidity, desc):
    with open(fileName, "a") as file:
        separator = ";"
        text = f'{temperature}{separator}{humidity}{separator}{desc}'
        file.write(text)
        file.flush()

async def blink(led, interval, count):
    for _ in range(count):
        led.value = not led.value
        await asyncio.sleep(interval.value)

async def calculate_value(dht, count, interval, temp_or_hum):
    tmp = 0
    for _ in range(count):
        if temp_or_hum=="temp":
            tmp += dht.temperature
        elif temp_or_hum=="hum":
            tmp += dht.humidity
        await asyncio.sleep(interval.value)

    return tmp/count




