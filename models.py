from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, backref, relationship
from sqlalchemy.orm.collections import column_mapped_collection

Base = declarative_base()


class Node(Base):
    """
    Tree_name - specify name of data group and allow to store more than one data-trees.
    """
    __tablename__ = "node"

    children = relationship("Node")

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    value = Column(Integer, nullable=False)
    tree_name = Column(String(50), nullable=False)
    parent_id = Column(Integer, ForeignKey(id))

    def __init__(self, name, value, tree_name="Default table", parent=None):
        self.name = name
        self.value = value
        self.tree_name = tree_name
        self.parent = parent

