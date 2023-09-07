from flask import Flask, request, jsonify
from gizmo.db.models import db, Example, ExampleCreate, ExampleRead, ExampleUpdate
import os
from gizmo.config.config import Config
from flask_pydantic import validate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/api/v1/example", methods=["POST"])
def create():
    data = request.json
    example_data = ExampleCreate(**data)
    new_example = Example(name=example_data.name)
    db.session.add(new_example)
    db.session.commit()
    return jsonify(ExampleRead.model_validate(new_example).model_dump()), 201


@app.route("/api/v1/example/<int:id>", methods=["GET"])
def read_example(id: int):
    example = db.session.get(Example, id)
    if not example:
        return jsonify({"message": "Not Found"}), 404
    return jsonify(ExampleRead.model_validate(example).model_dump())


@app.route("/api/v1/example/<int:id>", methods=["PUT"])
def update_example(id: int):
    data = request.json
    example_data = ExampleUpdate(**data)
    example = db.session.get(Example, id)
    if not example:
        return jsonify({"message": "Not Found"}), 404
    example.name = example_data.name
    db.session.commit()
    return jsonify(ExampleRead.model_validate(example).model_dump())


@app.route("/api/v1/example/<int:id>", methods=["DELETE"])
def delete_example(id):
    example = db.session.get(Example, id)
    if not example:
        return jsonify({"message": "Not Found"}), 404
    db.session.delete(example)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 200
