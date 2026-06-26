from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:ecommerce2026@localhost:5432/ecommerce"
)

with engine.connect() as conn:
    print("Connected successfully!")