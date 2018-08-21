#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from api.v1 import app

@app_views.route('/states/', methods=['GET'])
@app_views.route('/states/<state_id>', methods=['GET'])
def all_states(state_id=None):
    '''Returns all states object in json format'''
    json_list = []
    try:
        if state_id is None:
            for v in storage.all('State').values():
                json_list.append(v.to_dict())
        else:
            json_list = storage.get('State', state_id).to_dict()
        return jsonify(json_list)
    except:
        abort(404)
