from database import SessionLocal
from models import UsersModel

db = SessionLocal()


def seed():
    user = UsersModel(
        id=1,
        name='アンパンマン'
    )

    db.add(user)
    db.commit()


if __name__ == '__main__':
    BOS = '\033[92m'
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()
