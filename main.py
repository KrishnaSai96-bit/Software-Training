# main file for fastAPI app

from fastapi import FastAPI, HTTPException, Depends, status, Response
from pydantic import BaseModel #data validation
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

from sqlalchemy.sql import text


# instantiate app
app = FastAPI()
models.Base.metadata.create_all(bind=engine) #creates tables in MySQL database based on the definitions in model.py

class RecipeBase(BaseModel):
    idRECIPE: int
    RECIPE_Title: str
    RECIPE_Category: int
    RECIPE_CookingTime: int
    
     
class RecipeDetailsBase(BaseModel):
    Ingredients: str
    Recipe_Setps: str
    idRECIPE: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)] #db and class

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: RecipeBase, db:db_dependency):
    # db_post = models.Post(**post.model_dump())
    post = post.model_dump()
    # db.add(db_post)
    # db.commit()
    statement = text("INSERT INTO posts(idRECIPE, RECIPE_Title, RECIPE_Category, RECIPE_CookingTime) VALUES(:idRECIPE, :RECIPE_Title, :RECIPE_Category, :RECIPE_CookingTime)")
    #by writing a sql stmt (native sql)
    db.execute(statement, post)
    db.commit()