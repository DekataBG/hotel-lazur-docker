<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <section id="home-info" class="bg-dark">
        <div class="info-img"></div>
        <div class="info-content">
            <h2><span class="primary-text">Историята</span> на нашия хотел</h2>
            <p>
              Отворен през 1990 година като малък семеен бизнес, хотелът "Лазур" е един от първите туристически комплекси в региона. С годините, с усилията на собствениците си и инвестициите в разширяване и модернизация, той се превръща в иконично място за отдих и развлечения.
            </p>
            <RouterLink to="/about">
              <a class="btn btn-light">Прочетете повече</a>
            </RouterLink>

        </div>
    </section>
</template>

<style scoped>
/* hotel info */

#home-info {
    height: 400px;
  }
  
  #home-info .info-img {
    float: left;
    width: 50%;
    background: url('../assets/img/photo-1.jpg') no-repeat;
    min-height: 100%;
  }
  
  #home-info .info-content {
    float: right;
    width: 50%;
    height: 100%;
    text-align: center;
    padding: 50px 30px;
    overflow: hidden;
  }
  
  #home-info .info-content p {
    padding-bottom: 30px;
  }

</style>