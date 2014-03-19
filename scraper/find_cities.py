import mechanize  # HTML parser
import re         # Regular expressions library
import urllib2    # Open URLs in python
import json       # Encode and Decode JSON

provinces = ["alberta", "british_columbia", "manitoba", "new_brunswick",
 "newfoundland_and_labrador", "nova_scotia", "ontario", "price_edward_island",
  "quebec", "saskatchewan", "northwest_territories", "nunavut", "yukon"]

br = mechanize.Browser()
canadian_cities = {}

# Parse links on each province page to find city names
for p in provinces:
   br.open("http://www.trailcanada.com/"+p.lower()+"/cities/")
   for link in br.links():
      m = re.search("url='../(\w+)/'", str(link))
      # Found a valid city
      if m:
         # Format the information before writing to file
         province = str(p.replace('_',' '))
         city = str(m.group(1)).replace('_',' ')
         # Add values to dictionary
         if province not in canadian_cities:
            canadian_cities[province] = [city]
         else:
            canadian_cities[province].append(city)

# Write to JSON file
f = open('canadian_cities.json', 'w')
json.dump(canadian_cities, f)
f.close()