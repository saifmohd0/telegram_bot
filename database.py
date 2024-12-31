from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


DATABASE_URI = "mysql+pymysql://root:Saif12345@localhost:3306/telegram_bot_db"
engine = create_engine(DATABASE_URI, echo=True)  # Enable detailed logging
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

def init_db():
   
    try:
        print("Initializing database...")
        import models
        meta = Base.metadata
        meta.create_all(engine)
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")

if __name__ == "__main__":
    init_db()
