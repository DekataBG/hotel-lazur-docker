<script setup>

</script>

<template>
    <section id="about-info" class="bg-light py-3">
        <div class="container">
            <div class="info-left">
                <h1 class="l-heading"> За хотел <span class="primary-text">Лазур</span> </h1>
                <p>Отворен през 1990 година като малък семеен бизнес, хотелът "Лазур" е един от първите туристически комплекси в региона. С годините, с усилията на собствениците си и инвестициите в разширяване и модернизация, той се превръща в иконично място за отдих и развлечения.</p>
                <p>Днес, "Лазур" продължава да бъде едно от най-любимите места за почивка и развлечение за хора от различни части на света. С модернизирани удобства, висококачествено обслужване и безкрайни възможности за забавления, той продължава да вдъхновява спомени и да създава незабравими преживявания за своите гости.</p>
            </div>
            <div class="info-right">
                <img src="../assets/img/photo-2.jpg" alt="Hotel">
            </div>
        </div>
    </section>
</template>

<style scoped>
/* About Info */
#about-info .info-right{
    float:right;
    width:50%;
    min-height:100%;
}
#about-info .info-left{
    float:left;
    width:50%;
    min-height: 100%;
}

#about-info .info-right img{
    display:block;
    margin:auto;
    width:70%;
    border-radius:50%;
}
</style>