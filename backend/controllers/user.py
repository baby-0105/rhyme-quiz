from models import UsersModel


class UsersController:
    @classmethod
    def get_name(cls, db):
        return db.query(UsersModel).filter(UsersModel.id == 1).first()
