<template>
  <div class="ig-input-file">
    <label
      :for="ObjectID"
      v-text="label"/>
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
    },

    label: {
      type: String,
      default: 'click'
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
  color black
  label
    display block
    position relative
    text-align center
    cursor pointer
    padding 10px
    border 1px solid black
    border-radius 4px
    &:active
      background-color rgba(white, .2)
</style>