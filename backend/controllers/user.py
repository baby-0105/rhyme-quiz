from models import UsersModel


class UsersController:
    @classmethod
    def get_name(cls, db):
        try:
            user = db.query(UsersModel).filter(UsersModel.id == 1).first()
            return user
        except:
            return {"error"}
