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

class CookingData(BaseModel):
    ID: int
    Title: str
    Ingredients: str
    CookingTime: int
    Category: str
    Steps: str
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)] #db and class

#Query Method
@app.post("/CookBook/CreateRecipe", status_code=status.HTTP_201_CREATED)
async def create_recipe(recipeBO: RecipeBO, db:db_dependency):
    recipeBO = recipeBO.model_dump()
    statement = text("INSERT INTO recipe(idRECIPE, RECIPE_Title, RECIPE_Category, RECIPE_CookingTime) VALUES(:idRECIPE, :RECIPE_Title, :RECIPE_Category, :RECIPE_CookingTime)")
    db.execute(statement, recipeBO)
    db.commit()
    
#ORM Method 
@app.post("/CookBook/CreateRecipeORM", status_code=status.HTTP_201_CREATED)
async def create_recipe(recipeBO: RecipeBO, db:db_dependency):
    #Step1: Set BO with values passed by User Interface (FAst API) By Using "._model dump metod"
    #Stpe2: Create a Database Object by adding BO using models.method
    #Step3: Insert Data into table by adding DAO
    db_recipeDAO = models.Recipe(**recipeBO.model_dump())
    #ToDo: Rasie dupicate exception
    # if db_recipeDAO: 
    #     raise HTTPException(status_code=404, detail='Duplicate Enrty')
    db.add(db_recipeDAO)
    db.commit()
    
#Query Method
@app.post("/CookBook/CreateReciepDetails", status_code=status.HTTP_201_CREATED)
async def create_recipe_detials(recipeDetailsBO: RecipeDetailsBO, db:db_dependency):
    recipeDetailsBO = recipeDetailsBO.model_dump()
    statement = text("INSERT INTO recipe_details(Ingredients, Recipe_Steps, idRECIPE) VALUES(:Ingredients, :Recipe_Steps, :idRECIPE)")
    db.execute(statement, recipeDetailsBO)
    db.commit()

#ORM Method    
@app.post("/CookBook/CreateRecipeDetails_ORM", status_code=status.HTTP_201_CREATED)
async def create_recipe_details(recipeDetailsBO: RecipeDetailsBO, db:db_dependency):
    #Step1: Set BO with values passed by User Interface (FAst API) By Using "._model dump metod"
    #Stpe2: Create a Database Object by adding BO using models.method
    #Step3: Insert Data into table by adding DAO
    db_recipeDetailsDAO = models.Recipe_Details(**recipeDetailsBO.model_dump())
    db.add(db_recipeDetailsDAO)
    db.commit()

#Query Method    
@app.get("/CookBook/GetRecipe{recipe_id}", status_code=status.HTTP_200_OK)
async def get_recipe(recipe_id:int, db:db_dependency):
    statement = text("SELECT * FROM recipe WHERE idRECIPE = :recipe_id")
    result = db.execute(statement, {'recipe_id': recipe_id})
    recipe = result.fetchall()
    recipe_dict = {'idRECIPE':recipe[0][0], 'RECIPE_Title':recipe[0][1], 'RECIPE_Category':recipe[0][2], 'RECIPE_CookingTime':recipe[0][3]}
    return recipe_dict

#ORM Method
@app.get("/CookBook/GetRecipe_ORM/{recipe_id}", status_code=status.HTTP_200_OK)
async def get_recipe(recipe_id:int, db:db_dependency):
    #Step1: Arugument that is entered is recipe_id
    #Step2: ORM equivalent sql is 
            #db.query = SELECT
            #models.Receipe = from table name
            #filter = where class
            #.first = fetch first row
    recipe = db.query(models.Recipe).filter(models.Recipe.idRECIPE == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail='Recipe was not found')
    return recipe
   
#Query Method   
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

#ORM Method (ToDo)
# @app.get("/CookBook/GetListORM", status_code=status.HTTP_200_OK)
# async def get_recipe_details(db:db_dependency):
#     recipes = result.fetchall()
#     recipe_list = []
#     recipe_lists = db.query(models.Recipe).filter(models.Recipe.RECIPE_Category == RECIPE_Categoty).all()
#     return recipe

#Query Method
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

#ORM Method
@app.get("/CookBook/GetListOfCategories_ORM/{RECIPE_Category}", status_code=status.HTTP_200_OK)
async def get_recipe_categories(RECIPE_Categoty: str, db:db_dependency):
    #Step1: Arugument that is entered is recipe_id
    #Step2: ORM equivalent sql is 
            #db.query = SELECT
            #models.Receipe = from table name
            #filter = where class
            #.first = fetch first row
    recipe = db.query(models.Recipe).filter(models.Recipe.RECIPE_Category == RECIPE_Categoty).all()
    if recipe is None:
        raise HTTPException(status_code=404, detail='Recipes are not found')
    return recipe

    #  recipe_dict = {'idRECIPE':recipe[0][0], 'RECIPE_Title':recipe[0][1], 'RECIPE_Category':recipe[0][2], 'RECIPE_CookingTime':recipe[0][3]}
    #  return recipe_dict

#ORM Method
@app.get("/CookBook/GetCookingData/{RecipeID}", status_code=status.HTTP_200_OK)
async def GetCookingDetails(RecipeID : int , db:db_dependency):
    print (RecipeID)
    CookingData = db.query(models.CookingData).filter(models.CookingData.ID == RecipeID).first()
    return CookingData
    
    
    # recipe_dict = {'ID':recipe[0][0], 'Title':recipe[0][1], 'Ingredients':recipe[0][2], 'CookingTime':recipe[0][3], 'Category':recipe[0][4], 'Steps':recipe[0][5]}
    # return recipe_dict




    # if recipe is None:
    #     raise HTTPException(status_code = 404, detail='Recipe was not found')
    # return recipe