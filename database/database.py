from sqlalchemy import create_engine,URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="arian",
    password="@Rian82!!_#",
    host="188.121.112.234",#frb251672_test,159.69.146.36
    database="instagram"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
