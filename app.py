from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import csv
import json


app = Flask(__name__)

#this is the data. I want to use it like -> If GET request name is in Data, return link to Philosophers Wiki
# def csvfile(name):
#     with open('philosophers.csv') as phil:
#         read = csv.reader(phil)
#         l = []
         
#         for item in read:
#             b = {item[i]: item[i+1] for i in range(0, len(item), 2)}
#             if name in b:
#                 l.append(b) 
#         return l
            



class Hello(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    def get(self, name):
        def csvfile(name):
            with open('philosophers.csv') as phil:
                read = csv.reader(phil)
                l = []
                for item in read:
                    b = {item[i]: item[i+1] for i in range(0, len(item), 2)}
                    if name in b:
                        l.append(b)
                return json.dumps(l)[1]
        csvfile(name)
api = Api(app)

api.add_resource(Hello, '/home/<string:name>')

if __name__ == '__main__':
    app.run(port=5000,debug=True)