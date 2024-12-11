import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, CHAR, Float


Base = declarative_base()

class CryptoCurrency(Base):
    __tablename__ = 'crypto_currency'

    id = Column(Integer, primary_key=True)
    short_name = Column(String(50), nullable=False)
    full_name = Column(String(150), nullable=False)
    price = Column(Float, nullable=False)
    percentage_change = Column(Float, nullable=False)
    volume_for_the_period = Column(Float, nullable=False)
    capitalization = Column(Float, nullable=False)

