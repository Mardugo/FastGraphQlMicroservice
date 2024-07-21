import strawberry
from typing import List
from app.model.models import Compra
from app.model.database import SessionLocal
from strawberry.fastapi import GraphQLRouter
from datetime import datetime


@strawberry.type
class CompraType:
    id: int
    name: str
    price: int
    quantity: int
    createdAt: datetime
    updatedAt: datetime


@strawberry.type
class Query:
    @strawberry.field
    def compras(self) -> List[CompraType]:
        db = SessionLocal()
        items = db.query(Compra).all()
        return items

    @strawberry.field
    def compra(self,id:int) -> CompraType:
        db = SessionLocal()
        item = db.query(Compra).filter(Compra.id == id).first()
        if item is None:
            raise Exception(f"Compra with ID {id} not found.")
        return item

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_compra(self, name: str, price: int, quantity: int) -> CompraType:
        db = SessionLocal()
        item = Compra(name=name, price=price, quantity=quantity, createdAt=datetime.utcnow(), updatedAt=datetime.utcnow())
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @strawberry.mutation
    def update_compra(self, id:int, name: str, price: int, quantity: int) -> CompraType:
        db = SessionLocal()
        db_item = db.query(Compra).filter(Compra.id == id).first()
        if db_item is None:
            raise Exception(f"Compra with ID {id} not found.")
        for key, value in [("name",name),("price",price),("quantity",quantity),("updatedAt",datetime.utcnow())]:
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
 
    @strawberry.mutation
    def delete_compra(self, id:int) -> CompraType:
        db = SessionLocal()
        db_item = db.query(Compra).filter(Compra.id == id).first()
        if db_item is None:
            raise Exception(f"Compra with ID {id} not found.")
        db.delete(db_item)
        db.commit()
        return db_item

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)
