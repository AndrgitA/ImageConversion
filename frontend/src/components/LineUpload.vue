<template>
  <div class="im-line">
    <template v-if="!file">
      <input-file
        label="Click for choose file"
        @input="handleInputFile"/>
      <span
        v-text="'Загрузите архив формата zip'"/>
    </template>
    <div v-else>
      <span>File: {{ file.name }}</span>

      <option-type
        class="im-line__option"
        v-for="(option, index) in options"
        :key="index"
        :options="optionsList"
        @remove="handleRemove(index)"
        :value="options[index]"
        @input="handleInputOption(index, $event)"/>
      <button
        class="im-line__button-add"
        @click="handleClickAdd">Add option</button>
    </div>
  </div>
</template>

<script>
import InputFile from './elements/inputFile.vue';
import OptionType from './elements/optionType.vue';

export default {
  name: 'LineUpload',
  
  components: {
    InputFile,
    OptionType
  },

  data() {
    return {

      file: null,
      options: [],
      optionsList: [
        {
          id: 0,
          label: 'Оттенками серого цвета',
          value: {
            mode: 'shade_gray'
          },
        },
        {
          id: 1,
          label: 'Изображений к заданному размеру',
          value: {
            mode: 'resize',
            w: 1,
            h: 1
          },
        },
        {
          id: 2,
          label: 'Искажение изображения текстом «ОБРАЗЕЦ»',
          value: {
            mode: 'sample'
          },
        },
        {
          id: 3,
          label: 'Изменение размеров изображений в заданное число раз',
          value: {
            mode: 'scale',
            value: 1
          },
        },
      ]
    }
  },

  methods: {
    handleInputFile(value) {
      this.file = value;
      this.updateFormData()
    },

    updateFormData() {
      const formData = this.file === null ? null : new FormData();
      if (formData !== null) {
        const options = this.options
          .filter((option) => option.value.mode !== '')
          .map((option) => option.value);
        formData.append("images", this.file);
        formData.append("options", JSON.stringify(options));
      }
      this.$emit('input', formData);
    },

    handleClickAdd() {
      this.options.push({});
    },

    handleRemove(index) {
      this.options.splice(index, 1);
    },

    handleInputOption(index, value) {
      this.options.splice(index, 1, value)
      this.updateFormData();
    }
  }
}
</script>

<style lang="stylus">
.im-line
  height 100%
  width 100%
  > span
    margin-top: 5px
  &__button
    &-add
      border 1px solid black
      border-radius 4px
      margin-top 30px
      height 25px
  &__option
    margin-top: 10px
</style>