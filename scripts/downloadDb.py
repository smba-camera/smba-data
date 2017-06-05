import sys
import os
sys.path.append(os.path.abspath(os.path.join(".")))
from smba_data.weather_image_loader import download_all_data

download_all_data('data')