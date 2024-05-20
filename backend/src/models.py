from sqlmodel import Field, SQLModel
from datetime import date

# dates are represented in YYYY-MM-DD format
class RoomReservation(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    startDate: date
    days: int
    roomID: int = Field(foreign_key="room.id")
    email: str
    phone: str
    name: str

class GeneralReservation(SQLModel, table=False):
    startDate: date
    days: int
    roomID: int
    email: str
    phone: str
    name: str

class RoomType(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    features: str
    price: float
    imagePath: str
    capacity: int

class Room(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    room_type_id: int = Field(foreign_key="roomtype.id")

class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    message: str
    sentDate: date

class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: str | None = None


class User(SQLModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
