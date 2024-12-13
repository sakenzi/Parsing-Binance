from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


Base = declarative_base()

class EntityCrypto(Base):
    __tablename__ = 'entity_crypto'  

    id = Column(Integer, primary_key=True)
    short_name = Column(String(150), nullable=False)
    full_name = Column(String(150), nullable=False)

    values = relationship('ValuesCrypto', back_populates='entity')


class AttributeCrypto(Base):
    __tablename__ = 'attribute_crypto'  

    id = Column(Integer, primary_key=True)
    name_attribute = Column(String(100), nullable=False)

    values = relationship('ValuesCrypto', back_populates='attribute')


class ValuesCrypto(Base):
    __tablename__ = 'values_crypto'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    values = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=func.now())

    entity_id = Column(Integer, ForeignKey('entity_crypto.id'), nullable=False)
    attribute_id = Column(Integer, ForeignKey('attribute_crypto.id'), nullable=False)

    entity = relationship('EntityCrypto', back_populates='values')
    attribute = relationship('AttributeCrypto', back_populates='values')
