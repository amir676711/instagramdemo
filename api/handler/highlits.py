from fastapi import APIRouter,Depends,Security,HTTPException
import services.jwt as jwt
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from database.database import SessionLocal
from api.respones.BaseMessage import BaseMessage
from database import models
from sqlalchemy.orm import Session
from database.crud import highlits
from api.request.highlits import CreateHighlitsRequest,EditHighlitsRequest
from api.respones.highlits import CreateHighlitsRespones
from datetime import datetime



router = APIRouter(prefix="/api/v1/highlits")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def Gethighlits(db:Session=Depends(get_db)):
    return highlits.get_Highlits(db)

@router.get("/{id}",status_code=200,response_model=CreateHighlitsRespones)
def GetHighlits_ByID(db:Session=Depends(get_db)):
    HighlitDtail=highlits.get_Highlits_ByID(db,id)
    response=[]
    for item in HighlitDtail:
        response.append(CreateHighlitsRespones(
            id=item.id,
            PicUrl=item.PicUrl,
            Name=item.Name
        ))
    return response

@router.post("/",status_code=200,response_model=BaseMessage)
def create_Highlits(req :CreateHighlitsRequest,db: Session = Depends(get_db)):
    if len(req.Name) < 1:
            raise HTTPException(status_code=400,detail=" نام هایلایت را وارد کنید")
    if len(req.PicUrl) < 1:
            raise HTTPException(status_code=400,detail=" عکس هایلایت را وارد کنید")
    if req is None:
            raise HTTPException(status_code=400,detail=" درخواست با مشکلی روبرو شده است")
  
    UserHighlits=highlits.create_Highlits(db=db,PicUrl=req.PicUrl,Name=req.Name)
    return BaseMessage(message=" هایلایت باموفقیت ثبت شد")

# @router.patch("/",status_code=201,response_model=BaseMessage)
# def EditHighlit(req :EditHighlitsRequest,db: Session = Depends(get_db)):
#     if len(req.id) is None:
#         raise HTTPException(status_code=404,detail="هایلایت مورد نظر یافت نشد")
#     if len(req.PicUrl) < 1:
#         raise HTTPException(status_code=400,detail=" عنوان را وارد کنید")
#     if len(req.Name) < 1:
#         raise HTTPException(status_code=400,detail="عکس هایلایت را وارد کنید")
#     if req is None:
#         raise HTTPException(status_code=400,detail="درخواست با مشکل روبرو شده است")
#     gthighlit = highlits.get_Highlits(db)
#     gthighlit.id=req.id
#     gthighlit.Name=req.Name
#     gthighlit.PicUrl=req.PicUrl
#     db.commit()

#     return BaseMessage(message="هایلایت باموفقیت ویرایش شد")

@router.delete("/{id}",response_model=BaseMessage)
def DeleteUserHighlits(id:int,db:Session=Depends(get_db)):
    delete_UserHiglit=highlits.get_Highlits_ByID(db,id)
    if delete_UserHiglit is None :
        raise HTTPException(status_code=404,detail=" هایلایت مورد نظر یافت نشد")
    if not highlits.delete_Highlits(db,id) :
        raise HTTPException(status_code=400,detail="در حذف  هایلایت خطا رخ داده است")
    return BaseMessage(message=" هایلایت مورد نظر با موفقیت حذف شد")

