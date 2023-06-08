from typing import Optional

from sqlmodel import Field, SQLModel


class Items(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    model: str
    controller: str
    number: int