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

class RecipeBO(BaseModel):
    idRECIPE: int
    RECIPE_Title: str
    RECIPE_Category: str
    RECIPE_CookingTime: str
    
     
class RecipeDetailsBO(BaseModel):
    Ingredients: str
    Recipe_Steps: str
    idRECIPE: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)] #db and class

@app.post("/recipe/", status_code=status.HTTP_201_CREATED)
async def create_recipe(post: RecipeBO, db:db_dependency):
    post = post.model_dump()
    statement = text("INSERT INTO recipe(idRECIPE, RECIPE_Title, RECIPE_Category, RECIPE_CookingTime) VALUES(:idRECIPE, :RECIPE_Title, :RECIPE_Category, :RECIPE_CookingTime)")
    db.execute(statement, post)
    db.commit()
    
@app.post("/recipe_details/", status_code=status.HTTP_201_CREATED)
async def create_recipe_detials(post: RecipeDetailsBO, db:db_dependency):
    post = post.model_dump()
    statement = text("INSERT INTO recipe_details(Ingredients, Recipe_Steps, idRECIPE) VALUES(:Ingredients, :Recipe_Steps, :idRECIPE)")
    db.execute(statement, post)
    db.commit()
    
@app.get("/cookbook/{recipe_id}", status_code=status.HTTP_200_OK) #get menthod
async def get_recipe(recipe_id:int, db:db_dependency):
    statement = text("SELECT * FROM recipe WHERE idRECIPE = :recipe_id")
    result = db.execute(statement, {'recipe_id': recipe_id})
    recipe = result.fetchall()
    recipe_dict = {'idRECIPE':[0][0], 'RECIPE_Title':recipe[0][1], 'RECIPE_Category':recipe[0][2], 'RECIPE_CookingTime':recipe[0][3]}
    return recipe_dict

@app.get("/cookbook_details/", status_code=status.HTTP_200_OK) 
async def get_recipe_details(db:db_dependency):
    statement = text("select * from recipe, recipe_details where recipe.idRECIPE = recipe_details.idRECIPE")
    result = db.execute(statement)
    recipe = result.fetchall()
    recipe_dict = { 'idRECIPE':[0][0], 'RECIPE_Title':recipe[0][1], 'RECIPE_Category':recipe[0][2], 
                    'RECIPE_CookingTime':recipe[0][3], 'Ingredients':recipe[0][4], 
                    'Recipe_Steps':recipe[0][5], 'idRECIPE':recipe[0][6]}
    return recipe_dict