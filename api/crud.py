import pandas as pd
from io import StringIO
from fastapi import APIRouter, Depends, Body
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, StreamingResponse
from data.database import get_session
from data.models import Node


router = APIRouter(
    prefix='/api',
    tags=['api'],
)


@router.get("/nodes/{id}")
def get_nodes(id: int = 1, db: Session = Depends(get_session), offset: int = 0, limit: int = 10):
    """
    Возвращает список узлов постранично, по умолчанию - 10 объектов (limit).
    Для отображения следующих 10 объектов - необходимо увеличить offset на величину limit.
    По умолчанию возвращает список узлов, привязанных к корню (id = 1).
    Для получения списка дочерних объектов другого узла - передать значение его id как параметр в GET запросе.
    """
    nodes = db.execute(select(Node).where(Node.parent == id).offset(offset).limit(limit)).all()
    if not nodes and id == 1:
        return JSONResponse(status_code=404, content={"message": "Дерево пустое."})
    if not nodes:
        return JSONResponse(status_code=404, content={"message": "Такой узел отсутствует."})
    return nodes


@router.post("/nodes")
def create_node(data=Body(), db: Session = Depends(get_session)):
    if "value" not in data:
        data["value"] = -999
    if "parent" not in data:
        data["parent"] = 1
    node = Node(name=data["name"], value=data["value"], parent=data["parent"])
    db.add(node)
    db.commit()
    db.refresh(node)
    return node


@router.put("/nodes/{id}")
def edit_node(id, data=Body(), db: Session = Depends(get_session)):
    node = db.execute(select(Node).where(Node.id == id)).first()
    if not node:
        return JSONResponse(status_code=404, content={"message": "Такой узел отсутствует"})
    if data["name"]:
        node.name = data["name"]
    if data["value"]:
        node.value = data["value"]
    if data["parent"]:
        node.parent = data["parent"]
    db.commit()
    db.refresh(node)
    return node


@router.delete("/nodes/{id}")
def delete_node(id, db: Session = Depends(get_session)):
    """
    Удаляет объект по id, включая дочерние узлы.
    """
    node = db.execute(select(Node).where(Node.id == id)).first()[0]
    if not node:
        return JSONResponse(status_code=404, content={"message": "Такой узел отсутствует"})
    db.delete(node)
    db.commit()
    return node


@router.get("/deletes_many/{str_list}")
def deletes_many(str_list: str, db: Session = Depends(get_session)):
    """
    Удаляет узлы вместе с дочерними элементами.
    Передача параметра в формате /deletes_many/id1-id2-...-idN
    """
    id_list = [int(x) for x in str_list.split("-")]
    for id in id_list:
        node = db.execute(select(Node).where(Node.id == id)).first()
        if node:
            db.delete(node)
            db.commit()
    return id_list


@router.get("/download")
def xls_download(db: Session = Depends(get_session)):
    nodes = db.execute('SELECT id, name, value, parent FROM node').all()
    buffer = StringIO()
    pd.DataFrame(nodes).to_csv(buffer)
    buffer.seek(0)
    response = StreamingResponse(buffer, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=full_tree.csv"
    return response
