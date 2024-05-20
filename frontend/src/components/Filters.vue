<script setup>
    import { ref } from 'vue';

    const props = defineProps({
    rooms: {
        type: Array,
        required: true
    }
})

    // Define reactive variables
    const priceNumberInput = ref(null);
    const bedsNumberInput = ref(null);

    const priceComparisonOperator = ref('more');
    const bedsComparisonOperator = ref('less');

    const emits = defineEmits(['filter'])
    const rooms = props.rooms

    const filter = () => {
        var filteredRooms = rooms

        if (!isEmpty(priceNumberInput.value)) {
            if (priceComparisonOperator.value == 'more') {
                filteredRooms = filteredRooms.filter((room => room.price >= priceNumberInput.value))
            } else {
                filteredRooms = filteredRooms.filter((room => room.price <= priceNumberInput.value))
            }
        }

        if (!isEmpty(bedsNumberInput.value)) {
            if (bedsComparisonOperator.value == 'more') {
                filteredRooms = filteredRooms.filter((room => room.capacity >= bedsNumberInput.value))
            } else {
                filteredRooms = filteredRooms.filter((room => room.capacity <= bedsNumberInput.value))
            }
        }

        emits('filter', filteredRooms)
    }

    function removeFilter() {
        
        priceNumberInput.value = null
        bedsNumberInput.value = null
        filter()
    }

    function isEmpty(val){
        return val === undefined || val == null || val.length <= 0;
    }

const validateInput = (event) => {
  const allowedKeys = ['Backspace', 'ArrowLeft', 'ArrowRight', 'Delete', 'Tab', 'Home', 'End'];
  const key = event.key;

  if (!/\d/.test(key) && !allowedKeys.includes(key)) {
    event.preventDefault();
  }
};
</script>

<template>
    <div class="text-center mb-5">
        <vue-collapsible-panel-group>
            <vue-collapsible-panel :expanded="false">
                <template #title>
                    <h5> Филтрирайте стаи </h5>
                </template>
                <template #content>
                    <div id="app" class="container mt-5">
                        <div class="row justify-content-center align-items-center mb-2">
                            <div class="col-md-1">
                                <label for="priceNumberInput">Цена</label>
                            </div>
                          <div class="col-md-1">
                            <div class="form-group">
                                <input type="number" id="priceNumberInput" class="form-control" v-model="priceNumberInput" min="10" step="10" @keydown="validateInput">                            </div>
                          </div>
                          <div class="col-md-2">
                            <div class="form-group">
                              <select class="form-control" v-model="priceComparisonOperator">
                                <option value="more">Повече</option>
                                <option value="less">По-малко</option>
                              </select>
                            </div>
                          </div>
                          <div class="col-md-3 rounded">
                            <button class="btn btn-primary" @click="filter"> Приложи филтър</button>
                          </div>
                        </div>
                        <div class="row justify-content-center align-items-center">
                            <div class="col-md-1">
                                <label for="bedsNumberInput">Легла</label>
                            </div>
                          <div class="col-md-1">
                            <div class="form-group">
                                <input type="number" id="bedsNumberInput" class="form-control" v-model="bedsNumberInput" min="1" step="1" @keydown="validateInput">                            </div>
                          </div>
                          <div class="col-md-2">
                            <div class="form-group">
                              <select class="form-control" v-model="bedsComparisonOperator">
                                <option value="more">Повече</option>
                                <option value="less">По-малко</option>
                              </select>
                            </div>
                          </div>
                          <div class="col-md-3 rounded">
                            <button class="btn btn-primary" @click="removeFilter">Изчисти филтър</button>
                          </div>
                        </div>
                      </div>
                </template>
            </vue-collapsible-panel>
        </vue-collapsible-panel-group>
    </div>
</template>