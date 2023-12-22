from sqlalchemy import  Column,Integer, String
from .database import Base

class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, index=True)
    article = Column(String)
