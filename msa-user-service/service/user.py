from sqlalchemy.orm import Session

from schema.user import UserBase
from models.user import User


# 회원 가입 처리
# 기본 회원정보 + 번호,가입일
def register(db: Session, user: UserBase):
    user = User(**user.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    print(user)

    return user