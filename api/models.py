from pydantic import BaseModel

class URLink(BaseModel):
    sublink:str
    redirectTo: str
    