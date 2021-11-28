import json
from datetime import datetime

import bson
import flask
from flask import Flask, jsonify
from flask import request
from elasticsearch import Elasticsearch
from flask_jwt_extended import JWTManager, jwt_required
from flask_pymongo import PyMongo
from bson import json_util
from JWT import *
from JSONEncoder import JSONEncoder

# es = Elasticsearch()

app = Flask(__name__)

app.config[
    'MONGO_URI'] = 'mongodb+srv://vaderrama:vaderrama11@cluster0.lxc64.mongodb.net/Material?retryWrites=true&w=majority'

app.config["JWT_SECRET_KEY"] = "material-key"

jwt = JWTManager(app)
mongo = PyMongo(app)

materials = mongo.db.Materials
users = mongo.db.Users
materials.create_index([("name", 1)])


# ---------------- GET -------------------

# Print all the objects on collection Materials ( OK )
@app.route('/material/get_all', methods=['GET'])
@jwt_required()
def get_all():
    items = materials.find({}, {'_id': 0})
    if items.count() > 0:
        return jsonify(list(items))
    else:
        return jsonify({
            "message": "Materials not found",
        })


# Print one object for "name" attribute
@app.route('/material/get_one/<name>', methods=['GET'])
@jwt_required()
def get_one(name):
    material = materials.find_one({'name': name})
    if material is None:
        return jsonify({
            "message": "Material not found",
        })
    else:
        # Error TypeError: ObjectId('') is not JSON serializable solved
        return json.loads((json_util.dumps(material)))


# Search by json attributes
@app.route('/material/search', methods=['POST'])
@jwt_required()
def search():
    array = []
    material = materials.find(request.json, {"_id": 0})

    if material.count() == 0:
        return jsonify({"message": "No material found"})
    else:
        for x in material:
            array.append(x)
        return json.dumps(array)


# ---------------- INSERT -------------------

# Insert only one JSON ( OK )
@app.route("/material/insert_one", methods=['POST'])
def insert_one():
    material = materials.find_one(request.json, {"_id": 0})
    if material is not None:
        return jsonify({
            "message": "Material already exists",
        })
    else:
        materials.insert_one(request.json)
        return jsonify({"message": "Insert success", "material": json.loads((json_util.dumps(request.json)))})


@app.route("/material/insert", methods=['POST'])
def insert_many():
    already_exists = []
    insert = []
    inserts = request.json
    for x in inserts["Materials"]:
        material = materials.find(x)
        if material.count() > 0:
            already_exists.append(x)
        else:
            materials.insert_one(x)
            insert.append(x)

    return jsonify({"material inserts success": json.loads((json_util.dumps(insert))),
                    "material not insert": json.loads((json_util.dumps(already_exists)))})


# ---------------------- UPDATE ------------------------
# Update materials for "name" attribute with JSON data
@app.route("/material/update/<name>", methods=["PUT"])
@jwt_required()
def update(name):
    material = materials.find_one({"name": name}, {"_id": 0})
    if material is None:
        return jsonify({
            "message": "No material found for update",
        })
    else:
        materials.update_one({"name": name}, {"$set": request.json})
        return jsonify({
            "message": "Material Updated",
            "material": material
        })


# ---------------- DELETE -------------------

# Delete material for "name" attribute ( OK )
@app.route("/material/delete_one/<name>", methods=["POST"])
@jwt_required()
def delete_one(name):
    material = materials.find_one({"name": name}, {"_id": 0})
    if material is None:
        return jsonify({
            "message": "No material found for delete",
        })
    else:
        materials.delete_one({"name": name})
        return jsonify({
            "message": "Material deleted",
            "material": material
        })


# Delete all materials
@app.route("/material/delete_all", methods=["POST"])
@jwt_required()
def delete_all():
    x = materials.delete_many({})
    return jsonify({
        "message": "All Material deleted",
    })


# --------------------- TOKEN -------------------
@app.route("/login", methods=["POST"])
def token():
    ret = create_token(users, request.json)
    return ret
