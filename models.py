# what sqlalchemy (orm) uses to create tables we need in my sql database
# ddl - data definition language

from sqlalchemy import Boolean, Column, Integer, String
from database import Base 

class Recipe(Base):
    __tablename__ = 'recipe'

    idRECIPE = Column(Integer, primary_key=True, index=True) #first column in db, want to be able to index (faster performance)
    RECIPE_Title = Column(String(50)) #instantiate string with varchar 50
    RECIPE_Category = Column(String(50))
    RECIPE_CookingTime = Column(String(50))

class Recipe_Details(Base):
    __tablename__ = 'recipe_details'

    id = Column(Integer, primary_key=True, index=True)
    Ingredients = Column(String(1000))
    Recipe_Steps = Column(String(1000))
    idRECIPE = Column(Integer) #foreign key
    
class CookingData(Base):
    __tablename__ = 'CookingData'
    
    ID = Column(Integer, primary_key= True, index= True)
    Title = Column(String(500))
    Ingredients = Column(String(5000))
    CookingTime = Column(Integer)
    Category = Column(String(500))
    Steps = Column(String(5000))
 
#Updated on 18th
