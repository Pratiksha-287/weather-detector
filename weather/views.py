from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
  data={}
  photo_url=''
  if request.method=='POST':
    city=request.POST['city']

    #fetch weather data
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_WEATHER_API_KEY'
    res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5bf0b1aaacc04b745646c66c1c5864d6').read()
    json_data=json.loads(res)
    data={
      "country_code":str(json_data['sys']['country']),
      # "coordinate":str(json_data['coord']['lon'])+'  '+str(json_data['coord']['lat']),
      # "temp":str(json_data['main']['temp'])+'k',
      "coordinate": f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
      "temp": f"{json_data['main']['temp']}K",
      "pressure":str(json_data['main']['pressure']),
      "humidity":str(json_data['main']['humidity']),

    }

    # Fetch photo from Unsplash
    photo_url = fetch_photo(city)

  else:
    city=''
    data={}
  return render(request,'index.html',{'city':city,'data':data ,'photo_url': photo_url})

def fetch_photo(city):
    photo_api_key = 'C91ud7DvAxIzdHg1IqidOUEI9EStsh71kPK6bKJH9qU'
    search_url = f'https://api.unsplash.com/search/photos?query={city}&client_id={photo_api_key}'
    with urllib.request.urlopen(search_url) as response:
        photo_data = json.loads(response.read())
        if photo_data['results']:
            return photo_data['results'][0]['urls']['regular']
    return ''  # Return an empty string if no photo found