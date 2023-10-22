from mini_project.database import Base, engine
from mini_project.models import Item

print("Creating database")

Base.metadata.create_all(engine)
# Base.matadata --> contains all the maodels (tables) you created inheriting from Base.
# Base.metadata.create_all --> crates all the specified models (tables) in the database.
# the engine is the database connection we have already estalished.