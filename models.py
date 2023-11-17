# what sqlalchemy (orm) uses to create tables we need in my sql database
# ddl - data definition language

from sqlalchemy import Boolean, Column, Integer, String
from database import Base 

class Recipe(Base):
    __tablename__ = 'recipe'

    idRECIPE = Column(Integer, primary_key=True, index=True) #first column in db, want to be able to index (faster performance)
    RECIPE_Title = Column(String(50), unique=True) #instantiate string with varchar 50
    RECIPE_Category = Column(String(50), unique=True)
    RECIPE_CookingTime = Column(Integer, unique=True)

class Recipe_Details(Base):
    __tablename__ = 'recipe_details'

    id = Column(Integer, primary_key=True, index=True)
    Ingredients = Column(String(1000))
    Recipe_Setps = Column(String(1000))
    idRECIPE = Column(Integer) #foreign key
 
#Updated on 11th
