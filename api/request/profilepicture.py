from pydantic import BaseModel

class CreateProfilePictureRequest(BaseModel):
    PictureUrl: str