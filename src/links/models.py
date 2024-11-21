from flask          import current_app
from sqlalchemy.orm import DeclarativeBase,MappedAsDataclass,Mapped,mapped_column

class Base(DeclarativeBase, MappedAsDataclass):
    pass

class Link(current_app.database.Model):
    __tablename__ = "links"
    name: Mapped[str] = mapped_column(unique=True,nullable=False,primary_key=True)
    url:  Mapped[str] = mapped_column(unique=True,nullable=False)

current_app.database.create_all()
