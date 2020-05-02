<template>
  <div id="app">
    <input-file
      @input="handleInputFile"/>
  </div>
</template>

<script>
import InputFile from './components/elements/inputFile.vue';

export default {
  name: 'App',
  
  components: {
    InputFile
  },

  data() {
    return {
      file: null
    };
  },

  methods: {
    handleInputFile(value) {
      console.log("HANDLE INPUT FILE: ", value);
      this.file = value;

      const formData = new FormData();
      formData.append("images", value);
      this.upload(formData);
    },

    upload(postData) {
      this.$axios.post('/upload', postData, {
        onUploadProgress: this.uploadProgress
      }).then((response) => {
        console.log("RESPONSE: ", response);
      }).catch((error) => {
        console.log("ERROR: ", error);
      })
    },

    uploadProgress(event) {
      console.log("PROGRESS EVENT: ", event);
    }
  }
}
</script>

<style lang="stylus">
html
  overflow-x hidden
  overflow-y hidden
  padding 0
  border 0
  margin 0

body
  overflow auto
  padding 0
  border 0
  margin 0
  &::-webkit-scrollbar
    height: 10px

  &::-webkit-scrollbar-thumb
    border-radius 5
    -webkit-box-shadow none
    background-color $grey33
  width 100vw
  height 100vh


#app
  font-family Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50
  margin-top 60px
  width 100vw
  height 100vh

*[hidden]
  display none
</style>
