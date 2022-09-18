import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

from opencage.geocoder import OpenCageGeocode

number = "+919555576605"
key = 'ec02fd725d004c18a2a9424e616c0ecd'

pepnumber = phonenumbers.parse(number)

country = geocoder.description_for_number(pepnumber, 'en')
carrier_name = carrier.name_for_number(pepnumber, 'en')


geocoder = OpenCageGeocode(key)
query = str(country)

result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']


print(country, carrier_name)
print(result)
# print(lat, lng)
