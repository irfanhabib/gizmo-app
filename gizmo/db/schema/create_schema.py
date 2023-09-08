from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
meta = MetaData()
engine = create_engine('sqlite:///college.db', echo = True)

students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

meta.create_all(engine)
