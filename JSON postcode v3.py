import json
import http.client
import urllib.request
#import requests

def postcode(postcode):
    #userinput='tw10 6hw'# input(str("Please enter your postcode of your current location"))
    urlData = 'http://api.postcodes.io/postcodes/'+postcode  #'+?callback=foo'
    #urlData = "http://api.openweathermap.org/data/2.5/weather?q=Boras,SE"

    try:
        uh = urllib.request.urlopen(urlData)
        #print('web status:',uh.status)
        data = uh.read()
        #print ('Retrieved',len(data),'characters')
        #print(data)
        js = json.loads(data.decode("utf-8"))
        #print(js)
        print('Postcode',postcode.upper(),' has')
        #print('longitude:',js['result']['longitude'])
        #print('latitude:',js['result']['latitude'])
        Long_and_Lat(str(js['result']['longitude']),str(js['result']['latitude']))
        
    except  urllib.request.HTTPError:
            print('Could not find postcode '+userinput+' \ncheck it is a valid postcode')

def Long_and_Lat(Lg, Lt):
    #Long=Lg#'51.4386470'#input('Please enter the longitude: ')
    #Lat=Lt#'-0.3189160'#input('Please enter the latitude: ')

    Long=Lg
    Lat=Lt
    urlData = 'http://api.sunrise-sunset.org/json?lat='+Lat+'&lng='+Long

    try:
        uh = urllib.request.urlopen(urlData)
        #print('web status:',uh.status)
        data = uh.read()
        #print ('Retrieved',len(data),'characters')
        #print(data)
        js = json.loads(data.decode("utf-8"))
        #print(js)
        print('Longitude:', Long,'and latitude', Lat)
        print('Has sunrise:',js['results']['sunrise'],' and sunset:',js['results']['sunset'])
    except  urllib.request.HTTPError:
            print('Could not find sunrise & sunset times for longitude'+Long+' and latitude'+Lat)
    


print('*'*29)
print('*'*10+' Welcome '+'*'*10)
print('*'*29)

print('You can enter a postcode or longitude & latitude')
print('and the program will return the sunrise & sunset \ntimes for that location')
print('')
print('The program uses a web service to \'calculate\' the \nlongitude & latitude from a postcode')
print('Once the longitude & latitude are know \nit uses another webservice to find the sunrise & sunsets time')
print()
print('Make your choice below')
print('Postcodes enter P')
print('Longitude & Latitude enter L')

choice = input('\nPlease enter your choice L or P: ')
if choice.upper() == 'P':
    pcode='tw10 6hw'# input(str("Please enter your postcode of your current location"))    
    postcode(pcode)
elif choice.upper() == 'L':
    #lg ='-0.288201665927763'# input('Please enter the longitude: ')
    #lt ='51.4587556098985'#input('Please enter the latitude: ')
    lg =input('Please enter the longitude: ')
    lt =input('Please enter the latitude: ')
    Long_and_Lat(lg,lt)



##userinput='tw10 6hw'# input(str("Please enter your postcode of your current location"))
##urlData = 'http://api.postcodes.io/postcodes/'+userinput  #'+?callback=foo'
###urlData = "http://api.openweathermap.org/data/2.5/weather?q=Boras,SE"
##
##try:
##    uh = urllib.request.urlopen(urlData)
##    #print('web status:',uh.status)
##    data = uh.read()
##    #print ('Retrieved',len(data),'characters')
##    #print(data)
##    js = json.loads(data.decode("utf-8"))
##    #print(js)
##    print('longitude:',js['result']['longitude'])
##    print('latitude:',js['result']['latitude'])
##except  urllib.request.HTTPError:
##        print('Could not find postcode '+userinput+' \ncheck it is a valid postcode')




##webURL = urllib.request.urlopen(urlData)
##data = webURL.read()
##encoding = webURL.info().get_content_charset('utf-8')
##print(json.loads(data.decode(encoding)))
#{'coord': {'lat': 57.72, 'lon': 12.94}, 'visibility': 10000, 'name': 'Boras', 'main': {'pressure': 1021, 'humidity': 71, 'temp_min': 285.15, 'temp': 286.39, 'temp_max': 288.15}, 'id': 2720501, 'weather': [{'id': 802, 'description': 'scattered clouds', 'icon': '03d', 'main': 'Clouds'}], 'wind': {'speed': 5.1, 'deg': 260}, 'sys': {'type': 1, 'country': 'SE', 'sunrise': 1443243685, 'id': 5384, 'message': 0.0132, 'sunset': 1443286590}, 'dt': 1443257400, 'cod': 200, 'base': 'stations', 'clouds': {'all': 40}}




##
##conn = http.client.HTTPConnection('api.postcodes.io',80)
##conn.request("GET", url)
##r1 = conn.getresponse()
##if r1.status == 200:
##    print (r1.status, r1.reason)
##    data1 = r1.read()
##    json.loads(data.decode(encoding))
##    #my_dict = json.loads(str(data1))
##    
##    print(data1)
##    print('longitude:',my_dict['longitude'])
##    #json.loads(str(data1))
##    #print(json.dumps("result"))
##
##print('connection closed')
##conn.close()

