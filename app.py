from flask import Flask, render_template
from flask import request
import psycopg2
import re
import base64
import os, time, http.client
import requests
import urllib.request
import threading
import time

app = Flask(__name__)

@app.route('/')
def runpy():
    print("reloading....")
    return render_template('index.html')

@app.route('/uploaddata')
def uploaddata():
    print("uploading data....")
    people_counter = int(request.args.get('people'))
    isearthquake = int(request.args.get('earthquake'))
    try:
        # conn = psycopg2.connect(host="localhost",database="earthquake-detector", user="postgres", password="")
        # """
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # """
        cur = conn.cursor()
        query = "UPDATE housedata SET peoplein=%s, isearthquake=%s"
        values = (people_counter, isearthquake)
        cur.execute(query, values)
        conn.commit()
        count = cur.rowcount
        print(count)
        conn.close()
    except Exception as e:
        print(e)
    return '''{},{}'''.format(people_counter,isearthquake)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
