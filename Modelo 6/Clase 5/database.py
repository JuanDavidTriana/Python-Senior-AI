from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#DATABASE_URL =  "postgresql://postgres:admin@localhost:5432/tienda"
DATABASE_URL =  "postgresql://tienda_bp6e_user:3k55YTt3UYCk5LY4WMw2jaV4XuER5U2V@dpg-d4jqqn2li9vc73das4tg-a.oregon-postgres.render.com/tienda_bp6e"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
