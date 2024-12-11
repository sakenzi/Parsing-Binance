from sqlalchemy import create_engine
from decouple import config
from parser_models import Base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = config('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session = Session()

