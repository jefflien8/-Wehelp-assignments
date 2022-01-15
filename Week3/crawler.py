import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
list=data['result']['results']
# for pic in list:
#      pic1=pic['file'].split('https')
#      #print('http'+pic1[1])
# for area in list:
#     areas=area['address']
#     #print(areas[5:8])
with open('data.csv','w', encoding='utf-8') as file:
     for spot in list:
         pic1=spot['file'].split('https')
         areas=spot['address']
         file.write(spot['stitle']+','+areas[5:8]+','+spot['longitude']
         +','+spot['latitude']+','+'http'+pic1[1]+'\n')