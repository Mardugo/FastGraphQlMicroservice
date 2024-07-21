# create_db.py
from app.model.models import Base
from app.model.database import engine

Base.metadata.create_all(bind=engine)