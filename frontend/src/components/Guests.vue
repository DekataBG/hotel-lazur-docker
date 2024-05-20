<template>
    <section id="testimonials" class="py-3">
        <div class="container">
            <h2 class="l-heading ">Какво казват нашите гости</h2>
            <div class="testimonial primary-background">
                <img src="../assets/img/person-1.jpg" alt="Samanta">
                <p>"Прекарахме невероятна почивка в хотел Лазур! Обслужването беше изключително внимателно, персоналът беше много любезен и отзивчив. Стаите бяха просторни и уютни, а гледката към басейна беше невероятна. С удоволствие бих посетил този хотел отново!"</p>
            </div>
            <div class="testimonial primary-background">
                <img src="../assets/img/person-2.jpg" alt="Jen">
                <p>Прекрасен престой в хотел Лазур! Обстановката в градината беше просто вълнуваща, с уютни кътчета за отпускане и релаксация. Персоналът беше изключително внимателен и отзивчив, а стаите бяха комфортни и добре обзаведени. Бихме се върнали отново с удоволствие!</p>
            </div>
    </div>
    </section>
</template>

<style scoped>
#testimonials{
    height:600px;
    background:url('../assets/img/guests-bg.jpg') no-repeat center center/cover;
    padding-top:100px;
}

#testimonials .testimonial img{
    width:100px;
    float:left;
    margin-right:40px;
    border-radius:50%;
}

#testimonials h2{
    color:#fff;
    text-align:center;
    padding-bottom:55px;
}

#testimonials .testimonial{
    padding:20px;
    margin-bottom:40px;
    border-radius:5px;
    opacity: 0.85;
}
</style>