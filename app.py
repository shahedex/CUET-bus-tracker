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
    try:
        # conn = psycopg2.connect(host="localhost",database="cuetbus", user="postgres", password="")
        # """
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # """
        cur = conn.cursor()
        query = "SELECT * FROM padmalatlong"
        cur.execute(query)
        results = cur.fetchall()
        #"""
        for res in results:
            print(res)
        #"""
        conn.close()
    except Exception as e:
        print(e)
    return render_template('index.html', results=results)

@app.route('/sendlatlong')
def uploaddata():
    print("uploading data....")
    lattitude = request.args.get('lat')
    longitude = request.args.get('long')
    try:
        # conn = psycopg2.connect(host="localhost",database="cuetbus", user="postgres", password="")
        # """
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # """
        cur = conn.cursor()
        query = "UPDATE padmalatlong SET lat=%s, long=%s"
        values = (lattitude, longitude)
        cur.execute(query, values)
        conn.commit()
        count = cur.rowcount
        print(count)
        conn.close()
    except Exception as e:
        print(e)
    return '''{},{}'''.format(lattitude,longitude)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
