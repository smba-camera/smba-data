import sys
import os
sys.path.append(os.path.abspath(os.path.join(".")))
import time
from smba_data.weather_image_loader import request_save_image_weather

# run this script in a loop to download multiple images

request_save_image_weather()