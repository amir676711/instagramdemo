from pydantic import BaseModel

class CreatePostRequest(BaseModel):
    PostPicUrl: str
    TypePost: int

class EditPostRequest(BaseModel):
    id:int
    PostPicUrl: str
    TypePost: int
