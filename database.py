from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()
ENVIRONMENT_DEVELOPMENT = True

if ENVIRONMENT_DEVELOPMENT:
    DB_USER = "development"
    DB_PASSWORD = "root"
    DB_HOST = "Localhost"
    DB_NAME = "jumia-scraper"
else:
    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_HOST = os.environ["DB_HOST"]
    DB_NAME = os.environ["DB_NAME"]

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
