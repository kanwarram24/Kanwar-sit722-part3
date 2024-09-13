from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://sit722week72_user:iakl5WLQ0ouglcGFbepRI3Tv4G4ZE78a@dpg-crhutbbv2p9s73bgt410-a.oregon-postgres.render.com/sit722week72"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
