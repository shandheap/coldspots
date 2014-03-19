import urllib2    # Open URLs in python
import json       # Encode and Decode JSON

# Load the province-city dictionary from json
f = open("canadian cities.json", "r")
province_hash = json.load(f)
f.close()
temp_hash = {}

for province in province_hash:
   for city in province_hash[province]:
      print city
      print province
      try:
         # Use a weather API to fetch a JSON for the city
         result = urllib2.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q="+
            city + "," + province + ",Canada&units=metric")
      except urllib2.HTTPError:
         pass

      try:
         result = json.loads(result.read())
      # Parser returned a dict
      except AttributeError:
         pass

      # Check if API failed to return weather JSON
      if "message" in result:
         continue
      # Store important attributes
      temp = float(result["main"]["temp"])

      # Add values to dictionary
      if temp not in temp_hash:
         temp_hash[temp] = [city+","+province]
      else:
         temp_hash[temp].append(city+","+province)

# Sort all the temperatures in ascending order
sorted_keys = temp_hash.keys()
sorted_keys.sort()

results = {"sorted cities": []}

for k in sorted_keys:
   for v in temp_hash[k]:
      results["sorted cities"].append(v)

f = open('sorted cities.json', 'w')
json.dump(results, f)
f.close()