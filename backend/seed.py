from database import SessionLocal
from models import UsersModel

db = SessionLocal()


def seed():
    user = UsersModel(name='アンパンマン')

    db.add(user)
    db.commit()


if __name__ == '__main__':
    seed()
