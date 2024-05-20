<template>
    <div class="roomlist_carats">
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="WiFi"
              ><i
                class="fas fa-wifi vbo-icn-carat vbo-pref-color-text"
              ></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="TV"
              ><i
                class="fas fa-tv vbo-icn-carat vbo-pref-color-text"
              ></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Климатик"
              ><i
                class="fas fa-snowflake vbo-icn-carat vbo-pref-color-text"
              ></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Баня"
              ><i
                class="fas fa-bath vbo-icn-carat vbo-pref-color-text"
              ></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Минибар (не е зареден)"
              ><i
                class="fas fa-beer vbo-icn-carat vbo-pref-color-text"
              ></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Домашни любимци"
              ><i
                class="fas fa-paw vbo-icn-carat vbo-pref-color-text"
              ></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Две единични легла"
              ><i class="fas fa-bed vbo-icn-carat vbo-pref-color-text"></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Разтегателен диван"
              ><i class="fas fa-couch vbo-icn-carat vbo-pref-color-text"></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Телефон"
              ><i class="fas fa-phone vbo-icn-carat vbo-pref-color-text"></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Аксесоари за баня"
              ><i class="fas fa-gift vbo-icn-carat vbo-pref-color-text"></i></span
          ></span>
          <span class="vbo-room-carat"
            ><span class="vbo-expl" data-vbo-expl="Балкон"
              ><i class="fas fa-image vbo-icn-carat vbo-pref-color-text"></i></span
          ></span>
      </div>
</template>

<style scoped>
.roomlist_carats .vbo-room-carat, .room_carats {
    display: inline-block;
    margin: 4px 10px 0 var(--margin-size, 0); /* Default margin size */;
}


/* Show the entire tooltip on hover and focus */
[data-vbo-expl]:hover:before,
[data-vbo-expl]:hover:after,
[data-vbo-expl]:focus:before,
[data-vbo-expl]:focus:after {
	visibility: visible;
	-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
	filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=100);
	opacity: 1;
}

/* Base styles for the tooltip's directional arrow */
[data-vbo-expl]:before {
	z-index: 10001;
	border: 6px solid transparent;
	background: transparent;
	content: "";
}
[data-vbo-expl]::after {
	margin-left: -70px;
}

/* Base styles for the tooltip's content area */
[data-vbo-expl]:after {
	text-align: center;
	z-index: 10000;
	padding: 8px;
	width: 160px;
	background-color: #000;
	background-color: hsla(0, 0%, 20%, 0.9);
	color: #fff;
	content: attr(data-vbo-expl);
	font-size: 12px;
	line-height: 1.2;
}
/* Bottom */
.vbo-expl:before,
.vbo-expl:after {
	top: 100%;
	bottom: auto;
	left: 34%;
}

[data-vbo-expl]::before {
	margin-top: -12px;
	margin-bottom: 0;
	border-top-color: transparent;
	border-bottom-color: #000;
	border-bottom-color: hsla(0, 0%, 20%, 0.9);
}

.vbo-expl:hover:before,
.vbo-expl:hover:after,
.vbo-expl:focus:before,
.vbo-expl:focus:after {
	-webkit-transform: translateY(12px);
	-moz-transform: translateY(12px);
	transform: translateY(12px); 
}

/* Tooltip Charateristics - End */

.vbo-icn-carat {
    font-size: var(--font-size, 16px); /* Default font size */
}
.vbo-pref-color-text {
    color: #033f59 !important;
}

/* Tooltip Charateristics */
[data-vbo-expl] {
	position: relative;
	cursor: pointer;
}
[data-vbo-expl]:before,
[data-vbo-expl]:after {
	position: absolute;
	visibility: hidden;
	-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
	filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=0);
	opacity: 0;
	-webkit-transition:
		opacity 0.2s ease-in-out,
		visibility 0.2s ease-in-out,
		-webkit-transform 0.2s cubic-bezier(0.71, 1.7, 0.77, 1.24);
	-moz-transition:
		opacity 0.2s ease-in-out,
		visibility 0.2s ease-in-out,
		-moz-transform 0.2s cubic-bezier(0.71, 1.7, 0.77, 1.24);
	transition:
		opacity 0.2s ease-in-out,
		visibility 0.2s ease-in-out,
		transform 0.2s cubic-bezier(0.71, 1.7, 0.77, 1.24);
	-webkit-transform: translate3d(0, 0, 0);
	-moz-transform: translate3d(0, 0, 0);
	transform: translate3d(0, 0, 0);
	pointer-events: none;
}
</style>