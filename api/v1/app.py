#!/usr/bin/python3

'''api status'''
from flask import jsonify
from models import storage
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def return_status():
    '''return status'''
    return jsonify(status='OK')

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def return_stats():
    '''return stats'''
    model_counts = {
        'states': storage.count(State),
        'users': storage.count(User),
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review)
    }
    return jsonify(model_counts), 200

@app_views.errorhandler(404)
def not_found(error):
    '''handle 404 errors'''
    return jsonify(error='Not found'), 404

