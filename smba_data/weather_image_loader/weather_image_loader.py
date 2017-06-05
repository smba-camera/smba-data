import urllib.request
from smba_data.Model import Image, WeatherData, loadImages, load_weather_data
from smba_data.configuration import open_weather_map_api_key

# position of weather cam

lat = "48.23"
long = "11.63"
api_key = open_weather_map_api_key
highway_cam_url = "http://www.bayerninfo.de/webcams/images/A9Munich-Nuremberg/a9-km522-brn.jpg"
weather_api_url = 'http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+long+'&units=metric&appid=' + api_key

def request_image_weather():
    pic_response = urllib.request.urlopen(highway_cam_url)
    weather_response = urllib.request.urlopen(weather_api_url)
    pic_data = pic_response.read()
    weather_data = weather_response.read()

    location = 1
    img = Image(pic_data, location)
    weather = WeatherData(weather_data, location)
    return [img, weather]

def request_save_image_weather():
    data = request_image_weather()
    data[0].save()
    data[1].save()

def download_all_data(path):
    imgs = loadImages({})
    weatherdata = load_weather_data({})
    for i in imgs:
        i.save_to_disk(path)
    for w in weatherdata:
        w.save_to_disk(path)