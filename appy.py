import math
import requests


def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(meteor):
    return meteor.get('distance',math.inf)
 
my_location = (-33.93009,18.424068)


meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')

meteor_resp.status_code
 
meteor_resp.json()
 
data_meteor = meteor_resp.json()
 
 
for meteor in data_meteor:
    if not('reclat' in meteor and 'reclong' in meteor): continue
    meteor['dist'] = calc_dist(float(meteor['reclat']),float(meteor['reclong']),my_location[0],my_location[1])

data_meteor.sort(key=get_dist)
print(data_meteor[0:10])
 