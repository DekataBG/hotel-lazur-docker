from models import RoomType, RoomReservation, Room, Message
from sqlmodel import create_engine, SQLModel, Session
from datetime import date, timedelta, datetime
import random
import string


def generate_random_date():
    start_datetime = datetime.now() - timedelta(weeks=2)
    end_datetime = datetime.now() + timedelta(weeks=2)
    random_datetime = start_datetime + timedelta(seconds=random.randint(0, int((end_datetime - start_datetime).total_seconds())))
    return random_datetime


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)





with Session(engine) as session:
    session.add(RoomType(
        id= 1,
        title= "Двойна стая с изглед градина 3 възрастни",
        description= "Подходяща за настаняване на до 3 възрастни",
        features= "Стаята разполага с гледка към градината, две единични легла, разтегателен диван, сейф, телевизор, телефон, баня, аксесоари за баня, балкон. Стаята разполага с малък хладилник, тип минибар.",
        price= 80,
        imagePath= "3beds.jpg",
        capacity= 3
        )),
    session.add(RoomType(
        id= 2,
        title= "Двойна стая с изглед градина 2+1",
        description= "Подходяща за настаняване на 2 възрастни или 2 възрастни с дете",
        features= "Стаята разполага с гледка към градината, две единични легла, разтегателен диван, сейф, телевизор, телефон, баня, аксесоари за баня, балкон. Стаята разполага с малък хладилник, тип минибар. Деца над 12 години се таксуват като възрастен.",
        price= 60,
        imagePath= "beds2+1.jpg",
        capacity= 2
        )),
    session.add(RoomType(
        id= 3,
        title= "Двойна стая с изглед градина",
        description= "Подходяща за настаняване на 1 възрастен или 1 възрастен с дете",
        features= "Стаята разполага с гледка към градината, две единични легла, разтегателен диван, сейф, телевизор, телефон, баня, аксесоари за баня, балкон. Стаята разполага с малък хладилник, тип минибар.",
        price= 40,
        imagePath= "beds2.jpg",
        capacity= 1
        )),
    session.add(RoomType(
        id= 4,
        title= "Двойна стая с изглед басейн 3 възрастни",
        description= "Подходяща за настаняване на до 3 възрастни",
        features= "Стаята разполага с гледка към басейна, две единични легла, разтегателен диван, сейф, телевизор, телефон, баня, аксесоари за баня, балкон. Стаята разполага с малък хладилник, тип минибар. Деца над 12 години се таксуват като възрастен.",
        price= 80,
        imagePath= "3beds.jpg",
        capacity= 3
        )),
    session.add(RoomType(
        id= 5,
        title= "Двойна стая с изглед басейн 2+1",
        description= "Подходяща за настаняване на 2 възрастни или 2 възрастни с дете",
        features= "Стаята разполага с гледка към басейна, две единични легла, разтегателен диван, сейф, телевизор, телефон, баня, аксесоари за баня, балкон. Стаята разполага с малък хладилник, тип минибар. Деца над 12 години се таксуват като възрастен.",
        price= 60,
        imagePath= "beds2+1.jpg",
        capacity= 2
        )),
    session.add(RoomType(
        id= 6,
        title= "Двойна стая с изглед басейн",
        description= "Подходяща за настаняване на 1 възрастен с 1 дете",
        features= "Стаята разполага с гледка към басейна, две единични легла, разтегателен диван, сейф, телевизор, телефон, баня, аксесоари за баня, балкон. Стаята разполага с малък хладилник, тип минибар. Деца над 12г. .се таксуват като възрастен.",
        price= 40,
        imagePath= "beds2.jpg",
        capacity= 1
        )),
    session.add(RoomType(
        id= 7,
        title= "Апартамент",
        description= "Подходяща за настаняване на 4 възрастни или 2 възрастни с 2 деца",
        features= "Апартаментът разполага с 2 стаи с две единични легла, свързваща врата, 1 баня, аксесоари за баня, разтегателен диван, сейф, телевизор, телефон, балкон. Стаята разполага с малък хладилник, тип минибар.",
        price= 140,
        imagePath= "apartment.jpg",
        capacity= 4
        )),
    session.add(RoomType(
        id= 8,
        title= "Фамилна стая",
        description= "Подходяща за настаняване на 2 възрастни с 2 деца",
        features= "Фамилната стая разполага с 2 стаи с две единични легла, БЕЗ свързваща врата, 2 бани, аксесоари за баня, разтегателен диван, сейф, телевизор, телефон, балкон. Стаята разполага с малък хладилник, тип минибар.",
        price= 140,
        imagePath= "family.jpg",
        capacity= 4
        ))

    session.commit()

    session.add(Room(room_type_id=1))
    session.add(Room(room_type_id=1))
    session.add(Room(room_type_id=1))
    session.add(Room(room_type_id=2))
    session.add(Room(room_type_id=2))
    session.add(Room(room_type_id=2))
    session.add(Room(room_type_id=3))
    session.add(Room(room_type_id=3))
    session.add(Room(room_type_id=3))
    session.add(Room(room_type_id=4))
    session.add(Room(room_type_id=4))
    session.add(Room(room_type_id=4))
    session.add(Room(room_type_id=4))
    session.add(Room(room_type_id=5))
    session.add(Room(room_type_id=5))
    session.add(Room(room_type_id=5))
    session.add(Room(room_type_id=5))
    session.add(Room(room_type_id=5))
    session.add(Room(room_type_id=6))
    session.add(Room(room_type_id=6))
    session.add(Room(room_type_id=6))
    session.add(Room(room_type_id=6))
    session.add(Room(room_type_id=6))
    session.add(Room(room_type_id=6))
    session.add(Room(room_type_id=7))
    session.add(Room(room_type_id=7))
    session.add(Room(room_type_id=7))
    session.add(Room(room_type_id=7))
    session.add(Room(room_type_id=7))
    session.add(Room(room_type_id=7))
    session.add(Room(room_type_id=7))
    session.add(Room(room_type_id=8))
    session.add(Room(room_type_id=8))
    session.add(Room(room_type_id=8))
    session.add(Room(room_type_id=8))
    session.add(Room(room_type_id=8))
    session.add(Room(room_type_id=8))
    session.add(Room(room_type_id=8))
    session.add(Room(room_type_id=8))

    session.commit()

    session.add(RoomReservation(startDate=date.today(), days='7', roomID=1, email="person1@email.com", phone="0987654321", name="person1"))
    session.add(RoomReservation(startDate=date.today() + timedelta(days=1), days='2', roomID=2, email="person2@email.com", phone="0987654321", name="person2"))
    session.add(RoomReservation(startDate=date.today() + timedelta(days=4), days='1', roomID=2, email="person3@email.com", phone="0987654321", name="person3"))
    session.add(RoomReservation(startDate=date.today() + timedelta(days=6), days='2', roomID=2, email="person4@email.com", phone="0987654321", name="person4"))
    session.add(RoomReservation(startDate=date.today() + timedelta(days=2), days='5', roomID=3, email="person5@email.com", phone="0987654321", name="person5"))

    session.commit()

    for i in range(100):
        session.add(Message(name=f'name{i}', email=f'email{i}@example.com', message="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum", sentDate=generate_random_date()))
    session.commit()