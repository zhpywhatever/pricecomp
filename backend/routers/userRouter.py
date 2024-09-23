from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import userController
from schemas.userSchema import UserCreate, UserUpdate, User
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from utils.utils import get_current_user

router = APIRouter()

# 注册新用户
@router.post("/api/users")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return userController.register_user(user, db)


# 登录路由
@router.post("/api/users/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return userController.auth_user(db, form_data)

# 获取当前用户资料
@router.get("/api/users/profile")
def get_profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return userController.get_user_profile(db, current_user)

# 更新当前用户资料
@router.put("/api/users/profile")
def update_profile(user_update: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return userController.update_user_profile(user_update, db, current_user)

# 获取用户信息
@router.get("/api/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return userController.get_user_by_id(user_id, db)


# 关注用户
@router.put("/api/users/{id}/follow")
def follow_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return userController.follow_user(id, db, current_user)

# 取消关注
@router.put("/api/users/{id}/unfollow")
def unfollow_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return userController.unfollow_user(id, db, current_user)
