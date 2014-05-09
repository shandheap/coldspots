import json       # Encode and Decode JSON
import urllib2    # Open URLs in python


prov_codes = {"alberta": "AB", "british columbia": "BC", "manitoba": "MB", "new brunswick": "NB", 
"newfoundland and labrador": "NL", "northwest territories": "NT", "nova scotia": "NS", "nunavut": "NU", 
"ontario": "ON", "prince edward island": "PE", "quebec": "QC", "saskatchewan": "SK", "yukon": "YT"}

# Load the province-city dictionary from json
f = open("sorted_cities.json", "r")
data = json.load(f)
f.close()

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
      city + ',+' + province + ',+Canada&sensor=false')
   except urllib2.HTTPError:
      continue
   try:
      maps_result = json.loads(maps_result.read())
   except AttributeError:
      # If there is valid location data then continue
      if maps_result['results'][0]['geometry']['location']:
         continue
   if maps_result == []:
      continue
   print maps_result
   lat = maps_result['results'][0]['geometry']['location']['lat']
   lon = maps_result['results'][0]['geometry']['location']['lng']

   results["city names"].append(value)
   results["lat"].append(lat)
   results["lon"].append(lon)


f = open("sencha_data.json", 'w')
json.dump(results, f)
f.close()