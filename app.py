from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)



class Hello(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    def get(self, name):
        return name
api = Api(app)

api.add_resource(Hello, '/home/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)