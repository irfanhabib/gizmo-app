from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel, ConfigDict

db = SQLAlchemy()


class Example(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(255), nullable=False)


class ExampleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str


class ExampleCreate(ExampleBase):
    pass


class ExampleRead(ExampleBase):
    id: int


class ExampleUpdate(BaseModel):
    name: str
