from publisher import Publisher as WeatherStation
from subscriber import WebUI, MobileUI


station = WeatherStation()


station.add_observer(WebUI())
station.add_observer(MobileUI())

station.set_temperature(12)
station.set_temperature(20)

webui2 = WebUI()
station.add_observer(webui2)
station.set_temperature(35)

station.remove_observer(webui2)
station.set_temperature(40)
