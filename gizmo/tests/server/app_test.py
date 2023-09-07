import pytest
from gizmo.server.app import app
from gizmo.db.models import db, Example, ExampleCreate
from flask_testing import TestCase
from gizmo.config.config import TestConfig


class AppTest(TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_example(self):
        response = self.client.post("/api/v1/example", json={"name": "test"})
        data = response.get_json()
        assert response.status_code == 201
        assert data["name"] == "test"

    def test_read_example(self):
        example = Example(name="test")
        db.session.add(example)
        db.session.commit()

        response = self.client.get(f"/api/v1/example/{example.id}")
        data = response.get_json()
        assert response.status_code == 200
        assert data["name"] == "test"

    def test_update_example(self):
        example = Example(name="test")
        db.session.add(example)
        db.session.commit()

        response = self.client.put(f"/api/v1/example/{example.id}", json={"name": "updated"})
        data = response.get_json()
        assert response.status_code == 200
        assert data["name"] == "updated"

    def test_delete_example(self):
        example = Example(name="test")
        db.session.add(example)
        db.session.commit()

        response = self.client.delete(f"/api/v1/example/{example.id}")
        data = response.get_json()
        assert response.status_code == 200
        assert data["message"] == "Deleted successfully"
