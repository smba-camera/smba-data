import sys
import os
sys.path.append(os.path.abspath(os.path.join(".")))
import time
from smba_data.weather_image_loader import request_save_image_weather

while 1:

    request_save_image_weather()
    time.sleep(350) # every 5 minutes