from weather_data import WeatherData
from display_element import DisplayElement

w = WeatherData()

d1 = DisplayElement('DisplayElement1')
w.registerObserver(d1)

w.updateValue()

d2 = DisplayElement('DisplayElement2')
w.registerObserver(d2)

w.updateValue()

w.removeObserver(d1)

w.updateValue()