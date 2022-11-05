from fastapi import APIRouter
from controllers.user import users


router = APIRouter()

router.add_route("/users", users, methods=['GET'])
