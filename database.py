from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:rishi@localhost:5432/uber_eats_db"

engine = create_engine(DATABASE_URL)