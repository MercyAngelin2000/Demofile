from Database.database import Base
from sqlalchemy import Column,Integer,String

class sample(Base):
    __tablename__ = "demo"
    id = Column(Integer,nullable=False,primary_key=True)
    name = Column(String,nullable=True)
    age = Column(Integer,nullable=True)