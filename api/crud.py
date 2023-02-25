from fastapi import APIRouter, Depends, Response, status, Body
from sqlalchemy.orm import Session
from starlette.responses import FileResponse, JSONResponse
from data.database import get_db
from data.models import Node


router = APIRouter(
    prefix='/api',
    tags=['api'],
)


@router.get("/nodes")
def get_all_nodes(db: Session = Depends(get_db)):
    return db.query(Node).all()


@router.post("/nodes")
def create_person(data=Body(), db: Session = Depends(get_db)):
    node = Node(name=data["name"])
    db.add(node)
    db.commit()
    db.refresh(node)
    return node


@router.put("/nodes")
def edit_person(data=Body(), db: Session = Depends(get_db)):
    node = db.query(Node).filter(Node.id == data["id"]).first()
    if not node:
        return JSONResponse(status_code=404, content={"message": "Такой узел отсутствует"})
    node.name = data["name"]
    db.commit()
    # db.refresh(node)
    return node


@router.delete("/nodes/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    node = db.query(Node).filter(Node.id == id).first()
    if not node:
        return JSONResponse(status_code=404, content={"message": "Такой узел отсутствует"})
    db.delete(node)
    db.commit()
    return node


@router.get("/download")
def root():
    filepath = 'api/crud.py'
    return FileResponse(filepath,
                        filename="full_tree.xls",
                        media_type="application/vnd.ms-excel")
