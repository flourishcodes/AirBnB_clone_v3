#!/usr/bin/python3
'''
API for City
'''
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from api.v1 import app
import models


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def all_state_cities(state_id=None):
    '''Returns all ciities in state object'''
    json_list = []

    try:
        city_list = storage.get('State', state_id).cities
        for city in city_list:
            json_list.append(city.to_dict())
        return jsonify(json_list)
    except Exception:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    '''Retrieves a City from storage'''
    try:
        city = storage.get('City', city_id).to_dict()
        return jsonify(city)
    except Exception:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    '''Deletes a City from storage'''
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    else:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200


def attrib_update(obj, **args):
    '''Helper function to update objects attributes to correct types'''
    for key, value in args.items():
        if hasattr(obj, key):
            value = value.replace("_", " ")
            try:
                value = eval(value)
            except Exception:
                pass
            setattr(obj, key, value)


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    '''Creates a new City'''
    form = request.get_json(force=True)
    if storage.get('State', state_id) is None:
        abort(404)
    if 'name' not in request.json:
        return jsonify({"error": "Missing name"}), 400
    city_class = models.classes['City']
    new_city = city_class()
    attrib_update(new_city, **form)
    setattr(new_city, 'state_id', state_id)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    '''Updates attribute information of a City'''
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404)
    form = request.get_json(force=True)
    for k, v in form.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(city_obj, k, v)
    city_obj.save()
    return jsonify(city_obj.to_dict()), 200
