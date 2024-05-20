<script setup>
import { ref } from 'vue'
import {useToast} from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
import { createMessage } from '../plugins/api.ts'
import { AxiosError } from 'axios';
const nameText = ref('')
const emailText = ref('')
const messageText = ref('')

async function sendMessage() {
    const $toast = useToast();

    if(validateEmail(emailText.value) && nameText.value != "" && messageText.value != "") {
        const result = await createMessage(nameText.value, emailText.value, messageText.value, new Date())
        
        console.log(result)
        if (result instanceof AxiosError){
            $toast.open({
                message: 'Error! ' + result.message + ' ' + result.message,
                type: 'error',
                position: 'top'
            })
            return
        }

        $toast.open({
            message: 'Съобщението е изпратено',
            type: 'success',
            position: 'top'
        });

        nameText.value = ""
        emailText.value = ""
        messageText.value = ""
    } else {
        $toast.open({
            message: 'Съобщението не е валидно',
            type: 'error',
            position: 'top'
        });
    }
}

function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}
</script>

<template>
    <section id="contact-form" class="py-3">
        <div class="container">
            <h1 class="l-heading"><span class="primary-text">Свържете </span> се с нас</h1>
            <p>Моля, попълнете всички полета</p>
                <div class="form-group">
                    <label for="name">Име</label>
                    <input v-model="nameText" type="text" name="Name" id="Name">
               </div>
               <div class="form-group">
                    <label for="email">Имейл</label>
                    <input v-model="emailText" type="email" name="email" id="email">
               </div>
               <div class="form-group">
                    <label for="message">Съобщение</label>
                    <textarea v-model="messageText" type="email" name="message" id="message"></textarea>
               </div>
               <button @click="sendMessage()" class="btn">Изпращане</button>
        </div>
    </section>
</template>

<style scoped>
#contact-form .form-group{
    /* TODO: decide what to do with this typo */
    mairgin-bottom:20px;
}
#contact-form label{
    display:block;
    margin-bottom:5px;
}

#contact-form input, #contact-form textarea {
    width:100%;
    padding:10px;
    border:1px #ddd slod;
}

#contact-form textarea{
    height:200px;
}
#contact-form input:focus, #contact-form textarea:focus {
    outline:none;
    border-color:#f7c08a
}
</style>