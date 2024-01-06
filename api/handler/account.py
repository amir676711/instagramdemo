from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database import models
from sqlalchemy.orm import Session
from database.crud import account
from api.request.account import  CreateAccountRequest,EditAccountRequest,LoginUserRequest
from api.respones.account import CreateAccountRespones,LoginRespones,LoginRespones
from datetime import datetime
from datetime import timedelta



router = APIRouter(prefix="/api/v1/account")
access_security = JwtAccessBearer(secret_key=jwt.SECRET, auto_error=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def GetAccount(db:Session=Depends(get_db)):
    return account.get_account(db)


@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewUser(req : CreateAccountRequest,db: Session = Depends(get_db)):
    # accountCheck = account.get_account_BYID(db,req.UserName)
    # if accountCheck is not None:
    #     raise HTTPException(status_code=400,detail="کاربر با این یوزرنیم قبلا ثبت شده است")
    #     #grftn values az request
    newUser= account.create_account(db,req)
    if newUser is None :
        raise HTTPException(status_code=400,detail="در ثبت اطلاعات کاربر جدید خطا رخ داده است")

    return BaseMessage(message="کاربر جدید با موفقیت ثبت شد")


@router.post("/login",status_code=200,response_model=LoginRespones)
def LoginUser(req:LoginUserRequest,db:Session=Depends(get_db)):
    user = account.login(db,req.UserName,req.Password)
    user.lastLogin=datetime.now()
    db.commit()
    subject={'id':str(user.id),'username':str(user.UserName),'password':str(user.Password)}
    token=jwt.CreateToken(subject)
    token=access_security.create_access_token(subject=subject,expires_delta=timedelta(hours=1))
    return UserLoginResponse(UserName=user.UserName,Password=user.Password,Token=token,id=user.id)


@router.patch("/",status_code=201,response_model=BaseMessage)
def EditAccount(req :EditAccountRequest,db: Session = Depends(get_db)):
    if len(req.UserName) < 1:
        raise HTTPException(status_code=400,detail=" یوزرنیم را وارد کنید")
    if len(req.Password) < 1:
        raise HTTPException(status_code=400,detail=" گذرواژه را وارد کنید")
    if req is None:
        raise HTTPException(status_code=400,detail="درخواست با مشکل روبرو شده است")
    # repo=report.get_report(db,req.id)
    # if repo is None:
    #     raise HTTPException(status_code=404,detail="هایلایت مورد نظر یافت نشد")
    gtaccount = account.get_account_BYID(db,req.id)
    gtaccount.id=req.id
    gtaccount.UserName=req.UserName
    gtaccount.Password=req.Password
    db.commit()

    return BaseMessage(message="حساب باموفقیت ویرایش شد")


@router.delete("/{id}",response_model=BaseMessage)
def Delete_account(id:int,db:Session=Depends(get_db)):
    deleteaccount=account.get_account_BYID(db,id)
    if deleteaccount is None :
        raise HTTPException(status_code=404,detail=" حساب مورد نظر یافت نشد")
    if not account.delete_account(db,id) :
        raise HTTPException(status_code=400,detail="در حذف حساب کاربر خطا رخ داده است")
    return BaseMessage(message="حساب کاربر مورد نظر با موفقیت حذف شد")

