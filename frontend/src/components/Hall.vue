<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    hall: {
        type: Object,
        required: true
    }
})

</script>

<template>
    <section id="about-info" class="py-3">
        <div class="container">
            <div class="info-left">
                <h1 class="l-heading"> {{hall.name}} </h1>
                <p>{{hall.description}}</p>
            </div>
            <div class="info-right">
                <img :src="hall.imagePath" :alt="hall.name">
            </div>
        </div>
    </section>
</template>

<style scoped>
.container:hover {
    background-color: #f7f8f3;
}

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

    border-radius: 20%;
}

img {
    height: 25vh;
    width: 40vh;
    border-style: solid;
    border-width: 1px;
}

.container {
    border-bottom-style: solid;
    border-bottom-width: 0.2px;
    border-bottom-color: rgb(156, 156, 160);

}
</style>