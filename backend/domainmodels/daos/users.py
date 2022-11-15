from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class UsersModel(Base):
    __tablename__ = "users"

    id = Column(
        'id',
        Integer(),
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
    )
    name = Column('name', String(32), nullable=False)
    deleted_at = Column('deleted', DateTime)
