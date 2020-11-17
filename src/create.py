from pymongo import MongoClient
from pymongo import GEOSPHERE
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def create_dic (x):
    list1=[]
    for i in x:
        dict_comp_software={}
        dict_comp_software2={}
        dict_comp_software2['coordinates']=[]
        if i['offices'][0]['longitude'] != None or i['offices'][0]['latitude'] != None:
            dict_comp_software2['coordinates'].append(i['offices'][0]['longitude'])
            dict_comp_software2['coordinates'].append(i['offices'][0]['latitude'])
            dict_comp_software2['type'] = 'Point'
            dict_comp_software['location'] = dict_comp_software2.copy()
            dict_comp_software['name'] = i['name']    
            list1.append(dict_comp_software.copy())

    return list1


def create_collection (x, y):
    conn = MongoClient("localhost:27017")
    db = conn.get_database("ironhack")
    collec = db[x]
    for i in y:
        collec.insert_one(i)
        

def create_index(x, y, z):
    x.create_index([("location", GEOSPHERE)])
    compr2=[]
    for i in y:
        compr={}
        list2=[]
        f= x.find(
            {"location": {
                "$nearSphere": {
                    "$geometry": i['location'],
                    "$maxDistance": z * 1000
                } 
            }},
            {"name": 1, "_id": 0}
        )
        t=list(f)
        if t != []:
            compr['name']= i['name']
            list2=[c['name'] for c in t]    
            compr['comp_near'] = list2
            compr2.append(compr.copy())
    return compr2

def dic_ini (x, p):
    list2=[]
    for y in x:
        list3=[]
        if y != {}:
            for i in y['groups'][0]['items']:
                dict1={}
                dict1['name'] = i['venue']['name']
                dict1['address'] = i['venue']['location']['formattedAddress']
                dict1['longitud'] = i['venue']['location']['lng']
                dict1['latitud'] = i['venue']['location']['lat']
                dict1['type'] = p
                list3.append(dict1.copy())
            list2.append(list3)
    return list2


def dic_final(x):
    list5=[]
    list4=[]
    for y in x:
        for i in y:
            dict1={}
            dict2={}
            list3=[]
            if i['name'] not in list5:
                list5.append(i['name'])
                list3.append(i['longitud'])
                list3.append(i['latitud'])
                dict2['coordinates']= list3
                dict2['type'] = 'Point'
                dict1['location'] = dict2.copy()
                dict1['name'] = i['name']
                dict1['address'] = i['address']
                dict1['type'] = i['type']
                list4.append(dict1.copy())
    return list4


def call_url(x,y, z, t):
    list1=[]
    call={'High_School' : "4bf58dd8d48988d13b941735", 
           'Airport' : '4bf58dd8d48988d1eb931735',
           'vegan' : "4bf58dd8d48988d1d3941735",
            'Basketball' : '4bf58dd8d48988d1e1941735',
             'Cafeteria': '4bf58dd8d48988d128941735',
              'Veterinarian': '4d954af4a243a5684765b473',
         'Preschool': '52e81612bcbc57f1066b7a45',
          'Middle School':'4f4533814b9074f6e4fb0106'}
      
    
    for i in x:
        i['location']
        tok1 = os.getenv("tok1")
        tok2 = os.getenv("tok2")
        enlace = 'https://api.foursquare.com/v2/venues/explore'

        parametros = { "client_id" : tok1,
                  "client_secret" : tok2,
                  "v" : "20180323",
                  "ll": f"{i['location'].get('coordinates')[1]},{i['location'].get('coordinates')[0]}",
                  "categoryId": f"{call[y]}",
                  'radius': z*1000,
                  "limit" : t} 
        resp = requests.get (url = enlace, params = parametros)
        data = json.loads(resp.text)
        decoding_data = data.get("response")
        list1.append(decoding_data)

    return list1


def count_items(x):
    for i in x:
        i['Total'] = len(i['comp_near'])
    return x



