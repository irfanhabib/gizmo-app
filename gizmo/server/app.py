from flask import Flask, request, jsonify
from gizmo.db.models import db, Example, ExampleCreate, ExampleRead, ExampleUpdate
import os
from gizmo.config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/api/v1/example", methods=["POST"])
def create_example():
    data = request.json
    example_data = ExampleCreate(**data)
    new_example = Example(name=example_data.name)
    db.session.add(new_example)
    db.session.commit()
    return jsonify(ExampleRead.from_orm(new_example).dict()), 201


@app.route("/api/v1/example/<int:id>", methods=["GET"])
def read_example(id):
    example = Example.query.get(id)
    if not example:
        return jsonify({"message": "Not Found"}), 404
    return jsonify(ExampleRead.from_orm(example).dict())


@app.route("/api/v1/example/<int:id>", methods=["PUT"])
def update_example(id):
    data = request.json
    example_data = ExampleUpdate(**data)
    example = Example.query.get(id)
    if not example:
        return jsonify({"message": "Not Found"}), 404
    example.name = example_data.name
    db.session.commit()
    return jsonify(ExampleRead.from_orm(example).dict())


@app.route("/api/v1/example/<int:id>", methods=["DELETE"])
def delete_example(id):
    example = Example.query.get(id)
    if not example:
        return jsonify({"message": "Not Found"}), 404
    db.session.delete(example)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 200
