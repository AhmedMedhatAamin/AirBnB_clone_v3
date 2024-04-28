#!/usr/bin/python3xx
'''api status'''
import models
from models import storage
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def api_status():
    return jsonify({"status": "OK"})
