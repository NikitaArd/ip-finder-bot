from datetime import date
from email import message
from urllib import response
import folium
import socket
import requests
from html2image import Html2Image
import os
import time

TOKEN = ''

def host_ip_recognize(name):
    try:
        adress = socket.gethostbyname(name)
        return adress
    except socket.gaierror as error:
        error_message = 'Ops, It looks like this domain does not exist.'
        return False, error_message

def ip_location(adress):
    try:
        req = requests.get(f'http://ip-api.com/json/{adress}').json()
        data = {
            'IP': req['query'],
            'COUNTRY': req['country'],
            'CITY': req['city'],
            'ZIP': req['zip'],
            'ORG': req['org'],
        }
        lat = float(req['lat'])
        lon = float(req['lon'])
        m = folium.Map(location=[lat, lon])
        folium.Marker([lat, lon]).add_to(m)

        htmllink = req['query'] + '-' + req['country'] + '.html'
        pnglink = req['query'] + '-' + req['country'] + '.png'
        response = f"[IP] : {data['IP']}\n[COUNTRY] : {data['COUNTRY']}\n[CITY] : {data['CITY']}\n[ZIP] : {data['ZIP']}\n[ORG] : {data['ORG']}"

        m.save(htmllink)

        hti = Html2Image()
        with open(htmllink) as f:
            hti.screenshot(f.read(), size=(400, 400) ,save_as=pnglink)

        return response, htmllink, pnglink
    except:
        error_message = 'Ops, It looks like this adress is invalid.'
        return False, error_message

def recoup(line, par):
    line = line.replace(par, '')
    return line

def cleaner(file1, file2):
    os.remove(file1)
    os.remove(file2)