from pydantic import BaseModel

class CreateAccountRequest(BaseModel):
    UserName: str
    Password: str
class EditAccountRequest(BaseModel):
    id:int
    UserName:str
    Password:str
class LoginUserRequest(BaseModel):
    UserName: str
    Password: str