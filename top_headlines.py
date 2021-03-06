#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:42:45 2018

@author: nehabhomia
"""

from flask import Flask, render_template
from secrets import api_key
import requests

app = Flask(__name__)

@app.route('/')
def index():
    text = '''
    <h1>Welcome!</h1>
    '''    
    return text

@app.route('/user/<nm>')
def user_name(nm):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + 'technology' + '.json'
    params={'api-key': api_key}
    news_dict = requests.get(extendedurl, params).json()
    return render_template('users.html', name=nm, news = news_dict['results'][:5])

if __name__ == '__main__':
    app.run(debug=True)
    
#get stories

#print (news)

##get headlines
#results = news_dict['results']
#headlines = []
#for r in results:
#    headlines.append(r['title'])
#
#print (headlines[0] + '\n\n', headlines[1] + '\n\n', headlines[2] + '\n\n', headlines[3] + '\n\n', headlines[4] + '\n\n')
