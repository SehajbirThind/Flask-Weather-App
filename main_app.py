import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def city_weather():
    if request.method == 'POST':
        city_name = request.form['city']
    else:
        city_name = 'Mumbai'

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID='
    response = requests.get(url.format(city_name)).json()

    # dictionary containing weather details obtained from json file
    weather = {
        'city': city_name,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    return render_template('template_final.html', weather=weather)



if __name__ == '__main__':
    app.run(debug=True)
