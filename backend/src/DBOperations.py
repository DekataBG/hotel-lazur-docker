from models import Room, RoomReservation, RoomType, GeneralReservation, Message
from sqlmodel import create_engine, Session, select
from typing import List, Optional
from datetime import date, timedelta, datetime
from fastapi.exceptions import HTTPException
from fastapi import status

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def getRoomTypeByID(room_type_ID) -> RoomType:
    with Session(engine) as session:
        return session.get(RoomType, room_type_ID)

def getAllRoomTypes() -> List[RoomType]:
    with Session(engine) as session:
        statement = select(RoomType)
        types = session.exec(statement)
        return types.all()
    
def createRoomType(roomType: RoomType) -> RoomType:
    with Session(engine) as session:
        roomType.id = None
        session.add(roomType)
        session.commit()
        session.refresh(roomType)
        return roomType
    
def deleteRoomTypeByID(room_type_ID) -> None: 
    with Session(engine) as session:
        type = session.get(RoomType, room_type_ID)
        session.delete(type)
        session.commit()

# def createReservation(roomID: int, startDate: str, days: int, email: str) -> RoomReservation:
#     with Session(engine) as session:
#         reservation = RoomReservation(startDate=startDate, days=days, email=email, roomID=roomID)
#         session.add(reservation)
#         session.commit()
#         session.refresh(reservation)
#         return reservation
    
def getAllRooms() -> List[Room]:
    with Session(engine) as session:
        statement = select(Room)
        result = session.exec(statement)
        return result.all()

def getRoomByID(room_ID: int) -> Optional[Room]:
    with Session(engine) as session:
        return session.get(Room, room_ID)
    
def getRoomsByType(room_type_ID: int) -> List[Room]:
    with Session(engine) as session:
        statement = select(Room).where(Room.room_type_id == room_type_ID)
        rooms = session.exec(statement)
        return rooms.all()

def addRoom(room_type_ID: int) -> Room:
    with Session(engine) as session:
        room = Room(room_type_id=room_type_ID)
        session.add(room)
        session.commit()
        session.refresh(room)
        return room
    
def deleteRoom(room_ID: int) -> None:
    with Session(engine) as session:
        room = session.get(Room, room_ID)
        print('\n\n\n\n\n\n\n\n')
        print(room, room_ID)
        print('\n\n\n\n\n\n\n\n')
        session.delete(room)
        session.commit()

def getReservationsFromRoomIDs(room_IDs: List[int]) -> List[List[RoomReservation]]:
    with Session(engine) as session:
        reservations = []
        for ID in room_IDs:
            statement = select(RoomReservation).where(RoomReservation.roomID == ID)
            ScalarReservations = session.exec(statement)
            reservations.append(ScalarReservations.all())
        return reservations

def getReservationsFromRoom(room_ID: int) -> List[RoomReservation]:
    with Session(engine) as session:
        statement = select(RoomReservation).where(RoomReservation.roomID == room_ID)
        return session.exec(statement).all()

def createReservationForType(room_type_ID: int, reservationInfo: GeneralReservation) -> RoomReservation:
    with Session(engine) as session:
        statement = select(Room).where(Room.room_type_id == room_type_ID)
        rooms = session.exec(statement).all()

        if not rooms:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no rooms available under this type!')


        for ID in [room.id for room in rooms]:
            statement = select(RoomReservation).where(RoomReservation.roomID == ID)
            reservations = session.exec(statement).all()
            flag = False
            print('\n\n\n\n\n\n\n\n\n\n\n\n')
            print(reservationInfo)
            print(reservations)
            print('\n\n\n\n\n\n\n\n\n\n\n\n')
            for reservation in reservations:
                if reservationInfo.startDate >= reservation.startDate and reservationInfo.startDate <= reservation.startDate + timedelta(reservation.days - 1):
                    flag = True
                    break
                if reservationInfo.startDate + timedelta(reservationInfo.days - 1) >= reservation.startDate and reservationInfo.startDate + timedelta(reservationInfo.days - 1) <= reservation.startDate + timedelta(reservation.days - 1):
                    flag = True
                    break
            if flag:
                continue



            dbReservation = RoomReservation(startDate=reservationInfo.startDate, days=reservationInfo.days, roomID=ID, email = reservationInfo.email, name = reservationInfo.name, phone = reservationInfo.phone)
            session.add(dbReservation)
            session.commit()
            session.refresh(dbReservation)
            return dbReservation
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='There are no available rooms left for the selected date!')
        
        
def createMessage(message: Message) -> None:
    with Session(engine) as session:
        print('\n\n\n\n\n\n\n\n')
        print(message)
        print('\n\n\n\n\n\n\n\n')
        message.sentDate = datetime.strptime(message.sentDate, "%Y-%m-%d")
        session.add(message)
        session.commit()

def getAllMessages() -> List[Message]:
    with Session(engine) as session:
        statement = select(Message)
        messages = session.exec(statement)
        return messages.all()

def deleteMessage(message_ID: int):
    with Session(engine) as session:
        statement = session.get(Message, message_ID)
        session.delete(statement)
        session.commit()

def changeRoomType(room_type_ID: int, room_type: RoomType):
    with Session(engine) as session:
        current_room_type = session.get(RoomType, room_type_ID)
        if not current_room_type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='A room with the given id does not exist')
        if current_room_type.id == room_type.id:
            current_room_type.id = room_type.id
            current_room_type.title = room_type.title
            current_room_type.description = room_type.description
            current_room_type.features = room_type.features
            current_room_type.capacity = room_type.capacity
            current_room_type.price = room_type.price
            current_room_type.imagePath = room_type.imagePath
            session.add(current_room_type)
        else:
            conflictingRoomType = session.get(RoomType, room_type.id)
            if conflictingRoomType:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Given id conflicts with existing room!')
            session.delete(current_room_type)
            session.add(room_type)
        session.commit()

def getAllReservations() -> List[RoomReservation]:
    with Session(engine) as session:
        statement = select(RoomReservation)
        result = session.exec(statement)
        return result.all()
    
def addReservation(reservation: RoomReservation):
    with Session(engine) as session:
        reservation.id = None
        session.add(reservation)
        session.commit()

# def changeReservation(reservation_id: int, reservation: RoomReservation):
#     with Session(engine) as session:
#         print(reservation_id)
#         current_reservation = session.get(RoomReservation, reservation_id)
#         if not current_reservation:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='A room with the given id does not exist')
#         if current_reservation.id == reservation.id:
#             current_reservation.id = reservation.id
#             current_reservation.roomID = reservation.roomID
#             current_reservation.startDate = datetime.strptime(reservation.startDate, "%Y-%m-%d")
#             current_reservation.days = reservation.days
#             session.add(current_reservation)
#         else:
#             conflictingReservation = session.get(RoomReservation, reservation.id)
#             if conflictingReservation:
#                 raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Given id conflicts with existing room!')
#             session.delete(current_reservation)
#             session.add(reservation)
#         session.commit()
        
def deleteReservation(reservation_id: int):
    with Session(engine) as session:
        reservation = session.get(RoomReservation, reservation_id)
        print('\n\n\n\n\n\n')
        print(reservation, reservation_id)
        print('\n\n\n\n\n\n')
        session.delete(reservation)
        session.commit()