#!/usr/bin/python3
'''
API for Place
'''
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from api.v1 import app
import models


@app_views.route('/cities/<city_id>/places', methods=['GET'])
@app_views.route('/cities/<city_id>/places/', methods=['GET'])
def all_city_places(city_id=None):
    '''Returns all place object by city_id in json format'''
    json_list = []
    try:
        place_list = storage.get('City', city_id).places
        for place in place_list:
            json_list.append(place.to_dict())
        return jsonify(json_list)
    except Exception:
        abort(404)


@app_views.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    '''Retrieves a Place from storage'''
    try:
        place = storage.get('Place', place_id).to_dict()
        return jsonify(place)
    except Exception:
        abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    '''Deletes a City from storage'''
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    else:
        storage.delete(place)
        storage.save()
        return (jsonify({}), 200)


def attrib_update(obj, **args):
    '''Helper function to update objects attributes to correct types'''
    for key, value in args.items():
        if key not in ['id', 'created_at', 'updated_at', 'user_id', 'city_id']:
            if hasattr(obj, key):
                value = value.replace("_", " ")
                try:
                    value = eval(value)
                except Exception:
                    pass
                setattr(obj, key, value)


@app_views.route('/places/<place_id>/places', methods=['POST'])
def create_place(place_id):
    '''Creates an instance of Amenity and save it to storage'''
    form = request.get_json(force=True)
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    if 'user_id' not in request.json:
        abort(400, 'Missing user_id')
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    if 'name' not in request.json:
        abort(400, 'Missing name')
    place_class = models.classes['Place']
    new_place = place_class()
    attrib_update(new_place, **form)
    setattr(new_place, 'city_id', city_id)
    new_place.save()
    return jsonify(new_place.to_dict())


@app_views.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    '''Updates Amenity object attribute'''
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    form = request.get_json(force=True)
    attrib_update(place, **form)
    place.save()
    return jsonify(place.to_dict()), 200
