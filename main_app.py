import requests
import datetime
import time
from time import strptime
from datetime import timedelta, datetime
import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def city_weather():
    if request.method == 'POST':
        city_name = request.form['city']
    else:
        city_name = 'Mumbai'

    api_key = os.environ['api_key']

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=%s' % api_key
    response = requests.get(url.format(city_name)).json()

    # Error-handling if invalid city name is entered:
    if response['cod'] != 200:
        return render_template('template_final.html', weather=None)
    
    
    print(response)

    # dictionary containing weather details obtained from json file
    newtime = datetime.utcnow() + timedelta(hours = (response['timezone']/3600))
    format = ('%I:%M %p %Z')
    weather = {
        'city': city_name,
        'country' : response['sys']['country'],
        'time' : newtime.strftime(format),
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    return render_template('template_final.html', weather=weather)



if __name__ == '__main__':
    app.run()
