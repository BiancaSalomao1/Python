# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"msg": "ok"}

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.config import APP_NAME, VERSION
from app.database.db import engine, SessionLocal, Base
from app.database import crud

from app.routes import upload

app = FastAPI(
    title=APP_NAME,
    version=VERSION
)


Base.metadata.create_all(bind=engine)

#p/banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "DocExtract API rodando 🚀"}

@app.post("/users")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    return crud.create_user(db, username, password)

@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

app.include_router(upload.router)
