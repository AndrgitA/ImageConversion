<template>
  <div class="ig-input-file">
    <label
      :for="ObjectID"
      v-text="'INPUT FILE'"/>
    <input
      :id="ObjectID"
      @input="handleInput"
      :disabled="disabled"
      type="file"
      accept=".zip"
      hidden/>
  </div>
</template>

<script>
export default {
  name: 'InputFile',

  props: {
    disabled: {
      type: Boolean,
      default: false
    }
  },

  data() {
    return {
      ObjectID: this.$state.newObjectID
    }
  },

  methods: {
    handleInput(event) {
      const file = event.target.files.length ? event.target.files[0] : null;
      event.target.value = null;
      this.$emit('input', file);
    }
  }
}
</script>

<style lang="stylus">
.ig-input-file
  color green
  label 
    cursor pointer
</style>