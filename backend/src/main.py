from fastapi import FastAPI, HTTPException, status, Depends, File, UploadFile
from models import GeneralReservation, Room, RoomReservation, RoomType, Message, User, UserInDB, Token
import DBOperations
import authentication
from fastapi.middleware.cors import CORSMiddleware
from datetime import date, timedelta
from typing import List, Annotated

from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

origins = [
    "http://192.168.0.104:5173",
    "http://192.168.0.92:5173",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000",
    "http://localhost:5000",
    "http://localhost:9199"
    "http://0.0.0.0:3000",
    "http://0.0.0.0:5000",
    "http://0.0.0.0:9199",
    "http://172.19.0.2:3000",
    "http://172.20.0.2:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"

@app.get('/room_types/{room_type_ID}', status_code=status.HTTP_200_OK)
def getRoomType(room_type_ID: int) -> RoomType:
    type = DBOperations.getRoomTypeByID(room_type_ID)
    if type == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return type

@app.get('/room_types', status_code=status.HTTP_200_OK)
def getAllRoomTypes() -> List[RoomType]:
    rooms = DBOperations.getAllRoomTypes()
    return rooms

@app.post('/room_types', status_code=status.HTTP_201_CREATED)
def postRoomType(roomType: RoomType) -> RoomType:
    room = DBOperations.createRoomType(roomType)
    return room

@app.delete('/room_types/{room_type_ID}', status_code=status.HTTP_204_NO_CONTENT)
def deleteRoomTypes(room_type_ID) -> None:
    DBOperations.deleteRoomTypeByID(room_type_ID)
    return
    
@app.get('/room_types/{room_type_ID}/rooms')
def getRoomsByType(room_type_ID: int) -> List[Room]:
    rooms = DBOperations.getRoomsByType(room_type_ID)
    return rooms
    
@app.get('/room_types/{room_type_ID}/reservations')
def getRoomTypeReservations(room_type_ID: int) -> List[GeneralReservation]:
    rooms = DBOperations.getRoomsByType(room_type_ID)
    room_IDs = [room.id for room in rooms]
    reservations = [
        [
            GeneralReservation(startDate=reservation.startDate, days=reservation.days, roomID=-1, email="", phone="", name="")
            if reservation.startDate >= date.today()
            else GeneralReservation(startDate=date.today(), days=reservation.days - (date.today() - reservation.startDate).days, roomID=-1, email="", phone="", name="")
            for reservation
            in reservationList
            if reservation.startDate + timedelta(days=reservation.days) >= date.today()
        ]
        for reservationList
        in DBOperations.getReservationsFromRoomIDs(room_IDs)
    ]
    
    if reservations:
        room_type_reservations = reservations[0]

        for room in reservations[1:]:
            if room_type_reservations:
                new_room_type_reservations = []
                for global_reservation in room_type_reservations:
                    for local_reservation in room:
                        _max_startDate = max(global_reservation.startDate, local_reservation.startDate)
                        _min_endDate = min(
                            global_reservation.startDate + timedelta(global_reservation.days),
                            local_reservation.startDate + timedelta(local_reservation.days)    
                        )
                        intersection_days = (_min_endDate - _max_startDate).days
                        if intersection_days > 0:
                            new_room_type_reservations.append(GeneralReservation(startDate=_max_startDate, days=intersection_days, roomID=-1, email="", phone="", name=""))
                room_type_reservations = new_room_type_reservations
            else:
                break

        return room_type_reservations
    return []

@app.post('/room_types/{room_type_ID}/reservations', status_code=status.HTTP_201_CREATED)
def postReservation(room_type_ID: int, reservationInfo: GeneralReservation) -> RoomReservation:
    reservation = DBOperations.createReservationForType(room_type_ID, reservationInfo)
    return reservation

@app.put('/room_types/{room_type_ID}')
def putRoom(room_type_ID: int, room_type: RoomType):
    DBOperations.changeRoomType(room_type_ID, room_type)

@app.get('/rooms/{room_ID}')
def getRoom(room_ID: int) -> Room:
    room = DBOperations.getRoomByID(room_ID)
    if room == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return room

@app.get('/rooms')
def getRoom() -> List[Room]:
    return DBOperations.getAllRooms()

@app.post('/rooms', status_code=status.HTTP_201_CREATED)
def postRoom(room_type_ID: int) -> Room:
    room = DBOperations.addRoom(room_type_ID)
    return room
    
@app.delete('/rooms/{room_ID}', status_code=status.HTTP_204_NO_CONTENT)
def deleteRoom(room_ID: int) -> None:
    DBOperations.deleteRoom(room_ID)
    return

@app.get('/rooms/{room_ID}/reservations')
def getRoomReservations(room_ID: int) -> List[RoomReservation]:
    reservations = DBOperations.getReservationsFromRoom(room_ID)
    return reservations 

@app.post('/messages', status_code=status.HTTP_201_CREATED)
def postMessage(message: Message):
    DBOperations.createMessage(message)

@app.get('/messages', status_code=status.HTTP_200_OK)
def getAllMessages():
    return DBOperations.getAllMessages()

@app.delete('/messages/{message_ID}', status_code=status.HTTP_204_NO_CONTENT)
def deleteMessage(message_ID: int):
    DBOperations.deleteMessage(message_ID)

@app.get('/reservations', status_code=status.HTTP_200_OK)
def getReservations() -> List[RoomReservation]:
    return DBOperations.getAllReservations()

@app.post('/reservations')
def postReservation(reservation: RoomReservation):
    DBOperations.addReservation(reservation)

@app.put('/reservations/{reservation_id}')
def putReservation(reservation_id: int, reservation: RoomReservation):
    DBOperations.changeReservation(reservation_id, reservation)

@app.delete('/reservations/{reservation_id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteReservatopm(reservation_id: int):
    DBOperations.deleteReservation(reservation_id)
@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    return await authentication.login_for_access_token(form_data)

@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(authentication.get_current_active_user)],
):
    return current_user

@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(authentication.get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f'../../HotelLazur/public/rooms/{file.filename}'
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {
        'success': True,
        'file_path': file_path,
        'message': 'File uploaded successfully'
    }
    