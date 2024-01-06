from pydantic import BaseModel

class CreatePDRespones(BaseModel):
    id:int
    Title: str
    Mini_Text: str

