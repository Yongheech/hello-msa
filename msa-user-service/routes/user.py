from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from schema.user import UserBase, User
from service.database import get_db
from service.user import register

router = APIRouter()

@router.post('/user', response_model=User)
async def new_user(user: UserBase, db:Session=Depends(get_db)):
    print(user)

    return register(db, user)
