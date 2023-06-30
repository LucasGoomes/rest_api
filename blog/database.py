from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False}) # this is the path to the database file

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base() # this is the base class for all the models we will create