# main file for fastAPI app

from fastapi import FastAPI, HTTPException, Depends, status, Response
from pydantic import BaseModel #data validation
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

from sqlalchemy.sql import text

from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException



# instantiate app
app = FastAPI()
models.Base.metadata.create_all(bind=engine) #creates tables in MySQL database based on the definitions in model.py

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

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

@app.post("/CookBook/CreateRecipe", status_code=status.HTTP_201_CREATED)
async def create_recipe(recipeBO: RecipeBO, db:db_dependency):
    recipeBO = recipeBO.model_dump()
    statement = text("INSERT INTO recipe(idRECIPE, RECIPE_Title, RECIPE_Category, RECIPE_CookingTime) VALUES(:idRECIPE, :RECIPE_Title, :RECIPE_Category, :RECIPE_CookingTime)")
    db.execute(statement, recipeBO)
    db.commit()
    
@app.post("/CookBook/CreateReciepDetails", status_code=status.HTTP_201_CREATED)
async def create_recipe_detials(recipeDetailsBO: RecipeDetailsBO, db:db_dependency):
    recipeDetailsBO = recipeDetailsBO.model_dump()
    statement = text("INSERT INTO recipe_details(Ingredients, Recipe_Steps, idRECIPE) VALUES(:Ingredients, :Recipe_Steps, :idRECIPE)")
    db.execute(statement, recipeDetailsBO)
    db.commit()
    
@app.get("/CookBook/GetRecipe{recipe_id}", status_code=status.HTTP_200_OK)
async def get_recipe(recipe_id:int, db:db_dependency):
    statement = text("SELECT * FROM recipe WHERE idRECIPE = :recipe_id")
    result = db.execute(statement, {'recipe_id': recipe_id})
    recipe = result.fetchall()
    recipe_dict = {'idRECIPE':recipe[0][0], 'RECIPE_Title':recipe[0][1], 'RECIPE_Category':recipe[0][2], 'RECIPE_CookingTime':recipe[0][3]}
    return recipe_dict

#@app.get("/CookBook/GetRecipeDetails{recipe_id}", status_code=status.HTTP_200_OK) 
@app.get("/CookBook/GetList", status_code=status.HTTP_200_OK)
async def get_recipe_details(db:db_dependency):
    statement = text("SELECT recipe.idRECIPE, recipe.RECIPE_Title, recipe.RECIPE_Category, recipe.RECIPE_CookingTime, recipe_details.Ingredients, recipe_details.Recipe_Steps FROM recipe, recipe_details WHERE recipe.idRECIPE = recipe_details.idRECIPE")
    result = db.execute(statement)
    recipes = result.fetchall()
    # recipe_dict = { 'idRECIPE':recipe[0][0], 'RECIPE_Title':recipe[0][1], 'RECIPE_Category':recipe[0][2], 
    #                 'RECIPE_CookingTime':recipe[0][3], 'Ingredients':recipe[0][4], 
    #                 'Recipe_Steps':recipe[0][5], 'idRECIPE':recipe[0][6]}
    # return recipe_dict
    recipe_list = []
    for i in range(len(recipes)):
        recipe_dict = {'idRECIPE':recipes[i][0], 'RECIPE_Title':recipes[i][1], 'RECIPE_Category':recipes[i][2], 
                     'RECIPE_CookingTime':recipes[i][3], 'Ingredients':recipes[i][4], 
                     'Recipe_Steps':recipes[i][5]}
        recipe_list.append(recipe_dict)
    return recipe_list

@app.get("/CookBook/GetListOfCategories{RECIPE_Category}", status_code=status.HTTP_200_OK)
async def get_recipe_categories(RECIPE_Category: str, db:db_dependency):
    statement = text("Select * from recipe where RECIPE_Category = :RECIPE_Category") 
    result = db.execute(statement, {'RECIPE_Category': RECIPE_Category})
    recipe = result.fetchall()
    if len(recipe) == 0:
        raise HTTPException(status_code=404, detail='No Recipe is Found')
    categories = []
    for i in range(len(recipe)):
        recipe_dict = {'idRECIPE':recipe[i][0], 'RECIPE_Title':recipe[i][1], 'RECIPE_CookingTime':recipe[i][3]}
        categories.append(recipe_dict)
    return categories

    #  recipe_dict = {'idRECIPE':recipe[0][0], 'RECIPE_Title':recipe[0][1], 'RECIPE_Category':recipe[0][2], 'RECIPE_CookingTime':recipe[0][3]}
    #  return recipe_dict
     
     
     

# @app.get("/posts/", status_code=status.HTTP_200_OK)
# async def get_all_posts(db:db_dependency):
#     statement = text("SELECT * FROM posts")
#     result = db.execute(statement)
#     post = result.fetchall()
#     all_posts = []
#     for i in range(len(post)):
#         post_dict = {'id':post[i][0], 'title':post[i][1], 'content':post[i][2], 'user_id':post[i][3]}
#         all_posts.append(post_dict)
#     return all_posts