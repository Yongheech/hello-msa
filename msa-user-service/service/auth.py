import bcrypt
from sqlalchemy.orm import Session
from schema.user import UserLogin, Token
from models.user import User

# JWT 로그인 처리
def userlogin (login: UserLogin, db: Session):
    loginuser = db.query(User).filter(
        User.userid == login.userid,
                User.passwd == login.passwd).first()
    print(loginuser)

    if loginuser is None:
        token = None
    else:
        # token = "{'access_token':'hello,world', 'token_type':'bearer'}"
        token = Token(access_token='hello', token_type='bearer')

    return token

# 비밀번호 암호화 함수
# bcrypt : 비밀번호 단방향 암호화에 자주 사용하는 패키지
# 암호화 방법 : 사용자의 비밀번호 + bcrypt의 고유한 솔트
def hashed_password(passwd):
    SALT = bcrypt.gensalt() # 솔트 생성
    hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), SALT)
    print(hashed_password)

    return hashed_password