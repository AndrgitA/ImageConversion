<template>
  <div id="app">
    MY APPLICATION PAGE
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
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
</style>
