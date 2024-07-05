from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = 'sqlite:///skeevy.sqlite3'

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
