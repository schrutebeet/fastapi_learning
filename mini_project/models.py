from mini_project.database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


# this Item model (table) stems from the Base class and has its properties 
# named in an object-oriented style
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    price = Column(Integer)
    on_offer = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Item name={self.name}, price={self.price}>"