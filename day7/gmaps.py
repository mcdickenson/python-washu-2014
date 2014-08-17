# pip install googlemaps
from googlemaps import GoogleMaps 
api_key = 'your api key from developers.google.com'
gmaps = GoogleMaps(api_key)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
lat, lng = gmaps.address_to_latlng(whitehouse)
print lat, lng

destination = gmaps.latlng_to_address(38.897096, -77.036545)
print destination 

dlat, dlng = gmaps.address_to_latlng('326 Perkins Library, Durham, NC 27708')
print dlat, dlng 
duke = gmaps.latlng_to_address(dlat, dlng)
print duke 

local = gmaps.local_search('restaurant near ' + duke)
print local['responseData']['results'][0]['titleNoFormatting']

directions = gmaps.directions(duke, whitehouse)
print directions['Directions']['Distance']['meters']

for step in directions['Directions']['Routes'][0]['Steps']:
	print step['descriptionHtml']

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
# what is its address? 
# if I wanted to hold a morning meeting there, which cafe would you suggest?
# if I wanted to hold an evening meeting there, which bar would you suggest? 

