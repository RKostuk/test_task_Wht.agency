from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import register_models

engine = create_engine(f"sqlite:///db/test.db")
Session = sessionmaker(bind=engine)
register_models(engine=engine)


class Base_method():
    def __init__(self):
        self.session = Session()
