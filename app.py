from flask import (Flask, g, render_template, flash, redirect, url_for,
                  abort)
from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user,
                             login_required, current_user)

import geocoder,requests,json
import googleapiclient
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools



app = Flask(__name__)

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'
FLASK_DEBUG=1
te = "hello more "
tert = " hello {}".format(te)
@app.route('/')
def hello_world():
    g = geocoder.ip('me')
    print(g.latlng)
    """r = r = requests.get('127.0.0.1:5000/api/v1/todos')
    print(r)"""
    test = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name&key=AIzaSyDxNK_Fu4JuEcP6Elc1v28nZmteG64nDyI')
    print(json.dumps(test.json()))
    print(tert)

    test2 = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Banks&circle:200@{},{}&feilds=formatted_address,name&key=AIzaSyDxNK_Fu4JuEcP6Elc1v28nZmteG64nDyI'.format(g.latlng[0], g.latlng[1]))
    test3 = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=1500&feilds=formatted_address,name&type=shop&keyword=food&key=AIzaSyDxNK_Fu4JuEcP6Elc1v28nZmteG64nDyI'.format(g.latlng[0], g.latlng[1]))
    test4 = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Waitrose&inputtype=textquery&fields=photos,formatted_address,name,opening_hours,rating&locationbias=circle:1500@{},{}&key=AIzaSyDxNK_Fu4JuEcP6Elc1v28nZmteG64nDyI'.format(g.latlng[0], g.latlng[1]))
    res = test3.json()
    print(test3.json())
    testArr = []
    for results in res['results']:
        for info in results:
            if info == 'name' or info:
                testArr.append(results[info])

    for shop in testArr:
        test4 = requests.get(
            'https://maps.googleapis.com/maps/api/place/findplacefromtext/'
            'json?input={}&inputtype=textquery&fields=photos,formatted_'
            'address,name,opening_hours,rating&locationbias=circle:1500@{},{}&'
            'key=AIzaSyDxNK_Fu4JuEcP6Elc1v28nZmteG64nDyI'.format(shop,
                g.latlng[0], g.latlng[1]))

    


    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=80)

