from database import Database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date

class muebles(Database):
    __tablename__ = 'muebles'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20))
    dimensiones = Column(String(30))
    material = Column(String(30))
    precio = Column(String(10))
    