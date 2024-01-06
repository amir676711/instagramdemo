from pydantic import BaseModel

class CreatePDRequest(BaseModel):
    Title: str
    Mini_Text: str

class EditPDRequest(BaseModel):
    id:int
    Title: str
    Mini_Text: str