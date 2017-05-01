import os
api_key=os.environ['APIKEY']
import googlemaps

gm=googlemaps.Client(key=api_key)
geocode_result=gm.geocode('Bogota')[0]
print(geocode_result['geometry']['location'])