import json       # Encode and Decode JSON
import mechanize  # HTML parser 
import re         # Regular expressions library
import urllib2    # Open URLs in python


prov_codes = {"alberta": "AB", "british columbia": "BC", "manitoba": "MB", "new brunswick": "NB", 
"newfoundland and labrador": "NL", "northwest territories": "NT", "nova scotia": "NS", "nunavut": "NU", 
"ontario": "ON", "prince edward island": "PE", "quebec": "QC", "saskatchewan": "SK", "yukon": "YT"}

# Load the province-city dictionary from json
f = open("sorted cities.json", "r")
data = json.load(f)
f.close()

br = mechanize.Browser()

i=0

results = {"city codes": [], "city names": [], "lat": [], "lon": []}

# Find the city codes for the coldest cities
for value in data["sorted cities"]:
   if i == 10:
      break
   l = value.split(",")
   city = l[0]
   province = l[1]
   try:
      maps_result = urllib2.urlopen(
      'http://maps.googleapis.com/maps/api/geocode/json?address=' +
      city + ',+' + province + ',+Canada&sensor=false&libraries=weather')
   except urllib2.HTTPError:
      pass
   print maps_result
   maps_result = json.loads(maps_result.read())
   lat = maps_result['results'][0]['geometry']['location']['lat']
   lon = maps_result['results'][0]['geometry']['location']['lng']

   # Add the city codes, their names and their coordinates
   # results["city codes"].append(city_code)
   results["city names"].append(value)
   results["lat"].append(lat)
   results["lon"].append(lon)

         #    i+=1
         # break

f = open('sencha_data.json', 'w')
json.dump(results, f)
f.close()