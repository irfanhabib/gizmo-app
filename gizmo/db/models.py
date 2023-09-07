from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel

db = SQLAlchemy()


class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class ExampleBase(BaseModel):
    name: str


class ExampleCreate(ExampleBase):
    pass


class ExampleRead(ExampleBase):
    id: int


class ExampleUpdate(BaseModel):
    name: str
