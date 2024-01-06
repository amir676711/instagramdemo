from pydantic import BaseModel

class CreateAccountRespones(BaseModel):
    id: int
    UserName: str
    Password:str
class LoginRespones(BaseModel):
    UserName: str
    password: str
    Token:str