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

sections_list = ['home', 'opinion', 'world', 'national', 'politics', 'upshot', 'nyregion', 'business', 'technology', 'science', 'health', 'sports', 'arts', 'books', 'movies', 'theatre', 'sundayreview', 'fashion', 'tmagazine', 'food', 'travel', 'magazine', 'realestate', 'automobiles', 'obituaries', 'insider']

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
    return render_template('users_ec1.html', name=nm, news = news_dict['results'][:5], sections_list = sections_list)

@app.route('/user/<nm>/<section>')
def section_page(nm, section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': api_key}
    news_dict = requests.get(extendedurl, params).json()
    return render_template('sections.html', name=nm, section=section, news = news_dict['results'][:5])

if __name__ == '__main__':
    app.run(debug=True)