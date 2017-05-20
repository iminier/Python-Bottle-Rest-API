from bottle import run, get, post, request
from peopleModel import *

@get('/people')
def getAll():
    return {'people' : people }

@get('people/<name>')
def getAge(name):
    peopleOfAge = []
    personAge = [someone for someone in people if someone['age'] == age]

    return {'person' : people[0]}

run(host='localhost', port=8080)
