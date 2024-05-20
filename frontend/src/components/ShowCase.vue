<script setup>
import { RouterLink } from 'vue-router';

</script>

<template>
    <div id="showcase">
        <div class="container">
            <div class="showcase-content">
                <h1><span class="primary-text">Насладете се</span> на престоя си</h1>
                <p class="lead"> Заповядяйте в хотел Лазур. Надяваме се да се насладите на престоя си и да се чувствате като у дома си</p>
                <RouterLink to="/about">
                    <a class="btn">За хотела</a>
                </RouterLink>
            </div>
        </div>
    </div>    
</template>

<style scoped>
/* showcase */

#showcase{
    background-image: url('../assets/img/showcase.jpg');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    height: 1050px;
}

#showcase .showcase-content{
    color:#fff;
    text-align:center;
    padding-top:500px;
}

#showcase .showcase-content h1{
    font-size:75px;
    line-height:1.2em;
}

#showcase .showcase-content p {
    padding-bottom:20px;
    line-height: 1.7em;
}
</style>