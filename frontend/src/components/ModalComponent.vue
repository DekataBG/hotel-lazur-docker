<script setup>
import { defineProps, defineEmits, ref } from "vue";
import {onClickOutside} from '@vueuse/core'

const nameText = ref('')
const emailText = ref('')
const phoneText = ref('')

const props = defineProps({
  isOpen: Boolean,
});

const emit = defineEmits(["modal-close", "submit"]);

const target = ref(null)
onClickOutside(target, ()=>emit('modal-close'))

</script>

<template>
  <div v-if="isOpen" class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container" ref="target">
        <div class="text-center">
            Въведи данни 
        </div>
        <div class="modal-body">
            <form>
                <div class="mb-3">
                  <label for="name" class="form-label">Име</label>
                  <input v-model="nameText" type="text" name="Name" id="Name" class="form-control">
                </div>
                <div class="mb-3">
                  <label for="email" class="form-label">Имейл</label>
                  <input v-model="emailText" type="email" name="email" id="email" class="form-control">
                </div>
                <div class="mb-3">
                  <label for="phone" class="form-label">Телефонен номер</label>
                  <input v-model="phoneText" type="text" name="phone" id="phone" class="form-control">
                </div>
              </form>
        </div>
        <div class="text-center">
            <div>
              <button class="btn mb-2" @click.stop="emit('submit', { name: nameText, email: emailText, phoneNumber: phoneText })">Резервирай</button>
              <button class="btn btn-primary" @click.stop="emit('modal-close')">Затвори</button>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}
.modal-container {
  width: 300px;
  margin: 150px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
}

</style>