# Rock Paper Scissors Lisard Spock
#
# https://www.youtube.com/watch?v=R0pUbct9WgI
from collections import namedtuple
from typing import Dict, List, Union, NewType
from flask import Flask, jsonify, request
from flask_restful import reqparse, Resource, Api, fields, marshal, marshal_with, marshal_with_field
import lizardspock
import random
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('player_choice', type=int)

class Choices(Resource):

    def get(self):
        #return jsonify(choices)
        return lizardspock.choices


class Choice(Resource):

    def get(self):
        #return jsonify(get_random_choice())
        return lizardspock.get_random_choice()


class Play(Resource):

    def post(self):
        args = parser.parse_args()
        player_choice = int(args['player_choice'])
        computer_choice = lizardspock.get_random_choice()['id']
        result = lizardspock.play(player_choice, computer_choice)
        return result
        #return jsonify(result)


api.add_resource(Choices, '/choices')
api.add_resource(Choice, '/choice')
api.add_resource(Play, '/play')

if __name__ == '__main__':
    app.run(debug=True)
