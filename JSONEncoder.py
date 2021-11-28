import json
from datetime import datetime

import flask
from flask import Flask, jsonify
from flask import request
from elasticsearch import Elasticsearch
from flask_pymongo import PyMongo
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
