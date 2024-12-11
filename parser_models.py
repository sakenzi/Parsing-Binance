import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, CHAR

Base = declarative_base()

class CryptoCurrency(Base):
    __tablename__ = 'crypto_currency'

    id = Column(Integer, primary_key=True)
    short_name = Column(String(50), nullable=False)
    full_name = Column(String(150), nullable=False)
    price = Column(Integer, nullable=False)
    percentage_change = Column(Integer, nullable=False)