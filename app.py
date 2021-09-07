from flask import Flask
from flask_restful import Resource, Api, reqparse
import csv
import json


app = Flask(__name__)

#this is the data. I want to use it like -> If GET request name is in Data, return link to Philosophers Wiki
with open('philosophers.csv') as phil:
    read = csv.reader(phil)
    l = []
    a = input('Philosopher: ')   
    for name in read:
       b = {name[i]: name[i+1] for i in range(0, len(name), 2)}
       if a in b:
           l.append(b) 
    print(l)

class Hello(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    def get(self, name):
       pass
api = Api(app)

api.add_resource(Hello, '/home/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)