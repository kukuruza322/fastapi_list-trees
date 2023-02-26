from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Node(Base):
    __tablename__ = "node"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), default=f"Object №{id}", nullable=False)
    value = Column(Integer, nullable=True)
    parent = Column(Integer, ForeignKey(id), nullable=False, index=True)

    def __init__(self, name, value=None, parent=0):
        self.name = name
        self.value = value
        self.parent = parent

    def __repr__(self):
        return self.name