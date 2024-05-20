import { ref } from 'vue'
import { fetchRoomTypes } from './plugins/api'

export interface ReservationGeneralInfo{
  startDate: string,
  days: number
}

export interface ReservationObject extends ReservationGeneralInfo{
  id: number
  email: string,
  roomID: number
}

export interface RoomTypeObject{
  id: number
  title: string,
  description: string,
  features: string,
  price: number,
  imagePath: string,
  capacity: number,
}

export interface RoomObject{
  id: number,
  room_type_id: number
}

export interface Message{
  id: number | null,
  name: string,
  email: string,
  message: string,
  sentDate: string
}


export const links = ref([
  { id: 1, title: "Начало", path: "/" },
  { id: 2, title: "За нас", path: "/about" },
  { id: 3, title: "Стаи", path: "/room_types" },
  { id: 4, title: "Зали", path: "/halls" },
  { id: 5, title: "Контакти", path: "/contact" },
])

export const hotelName = "Хотел Лазур"

export const imagePath = "/rooms/"

export const room_types = ref(await fetchRoomTypes())

const imagePhotosPath = "/halls/"
export const halls = ref([
  { 
    id: 1, 
    name: "Конферентна зала", 
    description: "Предназначена за провеждане на конференции, семинари, срещи и други бизнес събития. Оборудвана е със звукова и видео техника, прожекционен екран, Wi-Fi връзка и комфортни седалки", 
    imagePath: imagePhotosPath + "business-room.jpg" 
  },
  { 
    id: 2, 
    name: "Спа център", 
    description: "Място за отдих и релаксация, където гостите могат да се насладят на различни процедури за красота, масажи, сауни, джакузи, фитнес зали и други удобства за подобряване на здравето и благополучието си.", 
    imagePath: imagePhotosPath + "spa.jpg" 
  },
  { 
    id: 3, 
    name: "Басейни", 
    description: "Вътрешни и външни басейни за отдих и забавление през летните месеци.", 
    imagePath: imagePhotosPath + "pool.jpg" 
  },
  { 
    id: 4, 
    name: "Детска зона", 
    description: "Детски клуб, където децата могат да се забавляват и играят под наблюдението на опитен персонал.", 
    imagePath: imagePhotosPath + "children-zone.jpg" 
  },
  { 
    id: 5, 
    name: "Бизнес кът", 
    description: "Включват бизнес център с компютри, принтери и други средства за работа, както и услуги като факс и копирни машини.", 
    imagePath: imagePhotosPath + "business-room.jpg" 
  }
])