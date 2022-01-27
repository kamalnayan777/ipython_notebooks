from flask import Flask
from flask_restful import Resource , Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Hello':'World from LU'}

class Item(Resource):
    def get(self):
        return ['1','2','3','4']
       
api.add_resource(HelloWorld,"/rest")
api.add_resource(Item,'/items')

if __name__ =='__main__':
    app.run(debug=True)

