import subprocess
import requests
import time
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

def hostname():
    result = subprocess.run(['hostname'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def json_response(data):
    response = {
        '_version': 'BLUE',
        '_host': hostname(),
        '_ts': time.time(),
        'data': data
    }

    return jsonify(response)

@app.route('/')
@app.route('/index')
def index():
    data = {
        'msg': 'Hello World!',
    }

    return json_response(data)


@app.route('/ping')
def ping():

    return json_response('PONG')

@app.route('/news', defaults={'country_name': 'US'})
@app.route('/news/<country_name>')
def news(country_name):
    api_key = "2a056a1df05a4303a751fd698ad908a1"
    base_url = "http://newsapi.org/v2/top-headlines?"
    complete_url = base_url + "country=" + country_name + "&apiKey=" + api_key
    data = requests.get(complete_url)

    return json_response(data.json())

@app.route('/weather', defaults={'city_name': 'Chicago,IL,US'})
@app.route('/weather/<city_name>')
def weather(city_name):
    api_key = "0e6ef642f3eebfc3941318821feb01dd"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    data = requests.get(complete_url)

    return json_response(data.json())

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8000)
