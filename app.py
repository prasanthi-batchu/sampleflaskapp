from flask import Flask, jsonify, request
 

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World..'



@app.route('/gani')
def gani():
   return 'Hello Ganiii..'

@app.route('/new_route')
def new_route():
   return 'Hello This is new Route..'

@app.route('/new_route_last')
def new_route_last():
   return 'Hello This is new Route last..'


if __name__ == '__main__':
   app.run(host='0.0.0.0')