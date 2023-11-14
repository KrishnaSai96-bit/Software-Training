# contains all connection strings for app to connect to my sql

from sqlalchemy import create_engine #for db to connect with app
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 
#base class that allows to create other 
#classes in the model

URL_DATABASE = 'mysql+pymysql://root:Krishna@localhost:3306/recipe'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
