<script setup>
import ServicesIcons from './ServicesIcons.vue'
import Filters from './Filters.vue'

import { defineProps, watchEffect, ref } from 'vue';
import { RouterLink } from 'vue-router';

import { imagePath } from '@/constants.ts';

const props = defineProps({
    rooms: {
        type: Array,
        required: true
    }
})

const currentRooms = ref(props.rooms)
</script>
<template>
  <div class="text-center mt-2">
    <h2>Разгледайте нашите</h2>
    <h1 class="primary-text">Стаи</h1>
  </div>
  <Filters :rooms="rooms" @filter="currentRooms = $event" />
  <ul class="vblist">
    <li 
        class="room_result" 
        v-for="room in currentRooms" 
        :key="room.id"
    >
      <div class="room_result-inner">
        <div class="vblistroomblock">
          <div class="vbimglistdiv">
            <RouterLink 
                :to="`rooms/${room.id}`"
                class="vbo-roomslist-imglink"
            > 
              <img
                decoding="async"
                :src="`${imagePath}${room.imagePath}`"
                :alt="room.title"
                class="vblistimg"
              />
          </RouterLink>
            <div class="vbmodalrdetails vbo-roomslist-opengallery-cont">
              <a
                href="javascript: void(0);"
                class="vbo-roomslist-opengallery"
                data-roomid="1"
                ></a>
            </div>
          </div>
          <div class="vbo-info-room">
            <div class="vbdescrlistdiv">
              <h4 class="vbrowcname">
                <RouterLink :to="`rooms/${room.id}`">
                    <a>{{room.title}}</a>  
                </RouterLink>
              </h4>
              <span class="vblistroomcat"></span>
              <div class="vbrowcdescr">
                {{room.description}}
              </div>
            </div>
            <ServicesIcons />
          </div>
        </div>
        <div class="vbcontdivtot">
          <div class="vbdivtot">
            <div class="vbdivtotinline">
              <div class="vbsrowprice">
                <div class="vbrowroomcapacity">
                  <i v-for="index in room.capacity" :key="index" class="fas fa-male vbo-pref-color-text"></i>
                </div>
                <div class="vbsrowpricediv">
                  <span class="room_cost">{{room.price}} лв. за нощувка</span>
                </div>
              </div>
              <div class="vbselectordiv">
                <div class="vbselectr">
                  <RouterLink 
                    :to="`rooms/${room.id}`" 
                    class="btn vbo-pref-color-btn"
                  >
                    Детайли
                  </RouterLink>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </li>
  </ul>
</template>

<style scoped>
.elementor-container {
  max-width: 1920px;
}

.vblist {
	list-style-type: none;
	margin:0;
	padding:0;
    display: flex;
    flex-wrap: wrap;
}

.room_result-inner {
	display: flex;
	flex-wrap: wrap;
	width: 100%;
}

.vblistroomblock {
	display: flex;
	-ms-flex-wrap: wrap;
	-webkit-flex-wrap: wrap;
	flex-wrap: wrap;
	width: 80%;
	min-height: 162px;
	float: left;
	border-right: 0.5px solid #ddd;
	position: relative;
}
.vblistroomblock .vbimglistdiv {
	-ms-flex: 0 0 35%;
	-webkit-flex: 0 0 35%;
	flex: 0 0 35%;
	position: relative;
}
.vblistroomblock .vbo-info-room {
	flex: 1;
	padding: 0 20px 10px;
}

.vbimglistdiv {
	width: 35%;
	float: left;
	margin: 0;
	display: inline-block;
}

.vbo-roomslist-imglink {
    border-radius: 15px;
}

img.vblistimg {
    border-style: solid;
    border-radius: 15px;
    border-width: 1px;
    height: 33vh;
    width: 50vh;
	margin:0 15px 0 0;
}

.vbmodalrdetails a i {
	line-height: 25px;
}
.vbimglistdiv:hover .vbmodalrdetails a {
	text-decoration: none;
	color: #999;
	opacity: 1;
}
.vbimglistdiv .vbmodalrdetails a:hover {
	color: #444;
}

.vbdescrlistdiv {
	padding: 14px 0 8px 0;
	overflow: hidden;
}

.vbrowcname {
    display: block;
    border-radius: 15px;
    color: #033f59;
    font-family: "Oswald", Sans-serif !important;
    font-weight: 900 !important;
    text-transform: uppercase;
    font-size: 23px;    
}

.vblistroomcat {
	display: block;
	margin:0;
	text-transform: uppercase;
    font-size: .9em;
	text-transform: initial;
}

.vbrowcdescr {
    margin: 5px 0 0;
	display:block;
    color: #033f59;
}

.roomlist_carats, .room_carats {
	display: inline-block;
	margin: 4px 10px 0 0;
}

.vbo-pref-color-text {
    color: #033f59 !important;
}

.vbrowroomcapacity {
	display: block;
	text-align: center;
    font-size: 20px;
}

.room_result {
    width: 100%;
    border: 1px solid #eee;
    border-radius: 20px;
}

ul.vblist .room_result {
    list-style-type: none;
    line-height: 25px;
    margin-bottom: 15px;
    margin-left: 15px;
    color: #033f59;
    font-family: "Oswald", Sans-serif !important;
    font-weight: normal !important;
}

.room_result:hover {
    background-color: #f7f8f3;
}

.vbselectr {
	text-align: center;
}
.vbselectr a {
	background: #cb5951;
	border-radius:30px;
	color: #fff;
	margin: 8px 0 0;
	padding: 8px;
	width: 75%;
}
.vbselectr a:focus {
	color: #fff;
	text-decoration: none;
}
.vbselectr a:hover {
	color: #fff;
	background: #4B7B92;
}

.vbo-pref-color-btn {
    color: #ffffff!important;
}

.vbo-pref-color-btn:hover {
    background-color: #033f59 !important;
    color: #ffffff !important;
}

.vbselectordiv {
	border-top:1px solid #eee;
	padding:0 0 10px;
	display: table;
	margin: 0 auto;
	width: 65%;
    box-sizing: border-box;
    width: 100%;
    padding: 0 10px 10px;
    padding: 0 10px 10px;
    width: 100%;
}

.vblistcontainer-grid .vbselectordiv {
	width: 100%;
	display: block;
	padding: 10px 20px 0;
	border-top: 0;
}

.vbcontdivtot {
	position:relative;
	float:right;
	margin:0;
	left: -2px;
	padding: 0;
	flex: 1;
}

.vbdivtot {
	float:right;
	width:100%;
}

.vbsrowprice {
	text-align:center;
	padding: 20px 10px 0;
}
</style>
