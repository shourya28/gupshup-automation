from pydantic import BaseModel


class MessageEvent(BaseModel):
    number: str
    chosen_option: int

    # class Config:
    #     orm_mode = True
