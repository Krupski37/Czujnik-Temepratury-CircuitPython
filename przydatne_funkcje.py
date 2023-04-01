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

def blink(led):
    led.value = not led.value
