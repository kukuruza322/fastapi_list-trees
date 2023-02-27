from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, backref, relationship

Base = declarative_base()


class Node(Base):
    __tablename__ = "node"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), default=f"Object №{id}", nullable=False)
    value = Column(Integer, nullable=True)
    parent = Column(Integer, ForeignKey(id), nullable=True, index=True)
    children = relationship(
        "Node",
        cascade="all, delete-orphan",
        backref=backref("parent_id", remote_side=id, passive_deletes=True),
    )

    # По умолчанию привязываем объекты к корню root с id = 1.
    # При его удалении/инициализации INSERT INTO node (id, name, value, parent) VALUES (1, 'root', null, null);
    def __init__(self, name, value=None, parent=1):
        super().__init__(self)
        self.name = name
        self.value = value
        self.parent = parent

    def __repr__(self):
        return self.name
