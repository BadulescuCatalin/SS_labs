# from flask import Blueprint, request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_jwt_extended import create_access_token, jwt_required
# from app import mongo

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/register", methods=["POST"])
# def register():
#     data = request.json
#     if mongo.db.users.find_one({"username": data["username"]}):
#         return jsonify({"message": "Username already exists"}), 400

#     hashed_password = generate_password_hash(data["password"], method="sha256")
#     user = {"username": data["username"], "password_hash": hashed_password, "role": "user"}
#     mongo.db.users.insert_one(user)

#     return jsonify({"message": "User created successfully"}), 201

# @auth_bp.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     user = mongo.db.users.find_one({"username": data["username"]})

#     if user and check_password_hash(user["password_hash"], data["password"]):
#         access_token = create_access_token(identity=str(user["_id"]))
#         return jsonify({"access_token": access_token}), 200

#     return jsonify({"message": "Invalid credentials"}), 401

# @auth_bp.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     return jsonify({"message": "Access granted!"}), 200
