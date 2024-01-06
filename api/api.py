from fastapi import FastAPI
from api.handler import idname,highlits,profilepicture,post,clock,professionaldash,account


from sqlalchemy.orm import Session#used for the Object Relationship Management (ORM) aspect of SQLAlchemy 

from database import crud, models
from database.database import SessionLocal, engine #a connection pool and a Dialect
from fastapi.middleware.cors import CORSMiddleware#CORS allows you to configure the web API's security


models.Base.metadata.create_all(bind=engine)
def create_app():
    app = FastAPI(docs_url="/api/docs")
    origins = [
    "http://localhost",
    "http://localhost:3306",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    #rout hayi ke injad kardim
    app.include_router(router=account.router)
    app.include_router(router=profilepicture.router)
    app.include_router(router=idname.router)
    app.include_router(router=profilepicture.router)
    app.include_router(router=post.router)
    app.include_router(router=clock.router)
    app.include_router(router=professionaldash.router)
    app.include_router(router=highlits.router)
    return app