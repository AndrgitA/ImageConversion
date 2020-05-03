<template>
  <div class="im-option">
    <div class="im-option__header">
      <span
        class="im-option__label"
        v-text="'Option for filter image'" />
      <button
        @click="$emit('remove')"
        class="im-option__button-remove"
        v-text="'Remove'"/>
    </div>
    <vue-select
      class="im-option__select"
      :value="currentValue"
      :searchable="false"
      :clearable="false"
      appendToBody
      placeholder="Select some..."
      :options="currentOptions"
      @input="handleInputSelect"
    />
    <template v-if="isOptionMode">
      <div v-if="isResize">
        <div class="im-option__additional">
          <span>Width:</span>
          <input
            type="number"
            v-if="currentValue.value"
            min="1"
            max="555"
            :value="currentValue.value.w"
            @input="handleInputValue('w', $event.target.value)">
        </div>
        <div class="im-option__additional">
          <span>Height:</span>
          <input
            type="number"
            v-if="currentValue.value"
            min="1"
            max="555"
            :value="currentValue.value.h"
            @input="handleInputValue('h', $event.target.value)">
        </div>
      </div>

      <div v-else>
       <div class="im-option__additional">
          <span>Scale:</span>
          <input
            type="number"
            v-if="currentValue.value"
            min="1"
            max="555"
            :value="currentValue.value.value"
            @input="handleInputValue('value', $event.target.value)">
        </div>
      </div>
    </template>
  </div>
</template>

<script>

import VueSelect from "vue-select";

export default {
  name: 'OptionType',

  components: {
    VueSelect
  },
  
  props: {
    value: {
      type: Object,
      default: () => {}
    },
    options: {
      type: Array,
      default: () => []
    }
  },

  data() {
    return {
      currentValue: '',
      currentOptions: []
    };
  },

  watch: {
    value: {
      immediate: true,
      handler(newValue) {
        this.currentValue = newValue || {};
      }
    },

    options: {
      immediate: true,
      handler(newValue) {
        this.currentOptions = newValue || [];
      }
    }
  },

  computed: {
    isOptionMode() {
      return this.currentValue &&
        this.currentValue.value &&
        this.currentValue.value.mode &&
        ['resize', 'scale'].includes(this.currentValue.value.mode);
    },

    isResize() {
      return this.isOptionMode && this.currentValue.value.mode === 'resize';
    }
  },

  methods: {
    handleInputSelect(value = {}) {
      this.$emit('input', { ...value });
    },
    handleInputValue(key, value) {
      const numb = Number.parseInt(value)
      const val = { ...this.currentValue };
      val.value[key] = numb > 0 ? numb : 1
      this.$emit('input', val);
    }
  }
}
</script>

<style lang="stylus">
.im-option
  border 1px solid lighten(black, 30)
  padding: 5px 0
  // background-color rgba(white, .4)
  border-radius 4px
  &__header
    display flex
  &__label
    margin-left 5px
    flex: 1
  &__button
    &-remove
      border-radius 4px 0 0 4px
      background-color black 
      color white
  &__select
    margin-top 10px
  &__additional
    display flex
    margin-left 10px
    margin-top 5px
    span 
      width 80px
    input 
      border 1px solid lighten(black, 30) 
      border-radius 4px
</style>