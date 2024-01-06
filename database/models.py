from sqlalchemy import Boolean, Column, ForeignKey,Double, Integer, String,UUID,DateTime,Double
from sqlalchemy.orm import relationship
import uuid
from .database import Base
from .Types import BinaryUUID
from datetime import datetime

# class Account(Base):
#     __tablename__ = "Account"
#     id = Column(Integer,primary_key=True, index=True)
#     UserName = Column(String(30))
#     Password = Column(String(3000))
class ccount(Base):
    __tablename__ = "ccount"
    id = Column(Integer,primary_key=True, index=True)
    UserName = Column(String(30))
    Password = Column(String(3000))
    lastlogin = Column(DateTime)
class IdName(Base):
    __tablename__ = "IdName"
    id = Column(Integer,primary_key=True, index=True)
    Name = Column(String(15))

class ProfilePicture(Base):
    __tablename__ = "ProfilePicture"
    id = Column(Integer,primary_key=True, index=True)
    PictureUrl = Column(String(3000))

# class Bio(Base):
#     __tablename__ = "Bio"
#     idid = Column(Integer,primary_key=True,index=True)
#     Name= Column(String(50))
#     Family= Column(String(50))
#     Trend= Column(String(50))
#     Job= Column(String(50))
#     Description= Column(String(50))

class ProfessionalDash(Base):
    __tablename__ = "ProfessionalDash"
    id = Column(Integer,primary_key=True,index=True)
    Title= Column(String(50))
    Mini_Text = Column(String(50))

class Highlits(Base):
    __tablename__ = "Highlits"
    id= Column(Integer,primary_key=True, index=True)
    PicUrl = Column(String(3000))
    Name = Column(String(3000))

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer,primary_key=True,index=True)
    PostPicUrl = Column(String(3000))
    TypePost = Column(Integer)

class Clock(Base):
    __tablename__ = "clock"
    id = Column(Integer,primary_key=True,index=True)
    Time = Column(String(12))


