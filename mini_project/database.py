from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from mini_project.config import settings

# used to construct the database connection URL
__DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:"\
                              f"{settings.POSTGRES_PASSWORD}@"\
                              f"{settings.POSTGRES_HOST}/"\
                              f"{settings.POSTGRES_DATABASE}"

# used to create a database engine
# the engine manages the database connection.
# The echo=True argument is optional and is often used for debugging purposes
engine = create_engine(__DATABASE_URL, echo=True)

# used to create a models (tables) based on an object-oriented approach
Base = declarative_base()

# used to manage database sessions for your application
SessionLocal = sessionmaker(bind=engine)


