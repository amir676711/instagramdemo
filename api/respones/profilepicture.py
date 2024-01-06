from pydantic import BaseModel

class CreateProfilePictureRespones(BaseModel):
    id: int
    IdName: str