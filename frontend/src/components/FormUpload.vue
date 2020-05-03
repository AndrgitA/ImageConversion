<template>
  <div
    class="im-form-upload"
    :class="{
      'im-form-upload__hidden': !isShow
    }">
    <header>
      <span v-text="'FORM UPLOAD'" />
      <button
        class="im-form-upload__button im-form-upload__button-hide"
        @click="handleClickHide"/>
    </header>
    <div class="im-form-upload__body">
      <div
        v-if="uploadInformation"
        class="im-form-upload__body-info">
        <span>All files in archive: {{ uploadInformation.count }}</span>
        <span>Changed files: {{ uploadInformation.countConversion }}</span>
        <a :href="uploadInformation.file" target="_black">Click for download</a>
      </div>
      <line-upload
        v-else
        @input="handleInputUpload"
        :key="keyReset"
        class="im-form-upload__body-line"/>
    </div>
    <footer>
      <button
        v-if="formData"
        class="im-form-upload__button im-form-upload__button-reset"
        @click="handleClickReset"
        v-text="'Reset'"/>
      <button
        v-if="showUpload"
        class="im-form-upload__button im-form-upload__button-upload"
        @click="handleClickUpload"
        v-text="'Upload'"/>
    </footer>
  </div>
</template>

<script>
import LineUpload from './LineUpload.vue';

export default {
  name: 'FormUpload',
  
  components: {
    LineUpload
  },

  data() {
    return {
      locked: false,
      isShow: true,
      keyReset: true,
      showUpload: false,
      formData: null,
      uploadInformation: null
    };
  },

  methods: {
    handleClickHide() {
      if (!this.locked) {
        this.locked = true;
        this.isShow = !this.isShow;
        setTimeout(() => {
          this.locked = false;
        }, 1000);
      }
    },

    handleClickReset() {
      this.locked = false;
      this.isShow = true;
      this.keyReset = !this.keyReset;
      this.showUpload = false;
      this.formData = null;
      this.uploadInformation = null;
    },

    handleClickUpload() {
      this.upload(this.formData);
    },

    handleInputUpload(value) {
      this.showUpload = value !== null;
      this.formData = value;
    },

    upload(postData) {
      this.$axios.post('/upload', postData).then((response) => {
        if (response.status === 200) {
          this.uploadInformation = response.data;
          this.showUpload = false;
        }
      });
    },
  }
}
</script>

<style lang="stylus">
.im-form-upload
  display flex
  flex-direction column
  transition all 1s ease-out
  &__hidden
    transition all 1s ease-out
    width 40px !important
    height 40px !important
    min-height 40px !important
    margin-left: calc(40px - 100%)
    .im-form-upload
      &__body
      &__body * 
        height 0 !important
        padding 0 !important
        margin 0 !important
        opacity 0 !important
        line-height 0 !important 
    & header
      border-radius 4px !important
      span 
        display none !important
    footer,
    footer *
      height 0 !important
      padding 0 !important
      margin 0 !important
      opacity 0 !important
      
  &__body
    opacity 1
    transition all 1s ease-out
    flex 1
    display block
    overflow auto
    height 100%
    padding 20px 10px
    &-info
      background-color rgba(white, .4)
      border-radius 4px
      padding 5px
      a
        margin-top 10px
        padding 10px
        color white
        border-radius 4px
        background-color black
        border 1px solid white
        position relative
        display inline-block
        &:hover
          background-color lighten(black, 10)
        &:active
          background-color lighten(black, 20)
    &-line
      background-color rgba(white, .7)
      height calc(100% - 40px)
      padding 5px
      border-radius 4px
      box-sizing border-box
      min-height 80px
      position relative
  & header 
    border-radius 4px 4px 0 0
    background-color black 
    color white
    height 40px
    box-sizing border-box
    padding 10px
    display flex
    span 
      font-weight 500
      flex 1
      width 100%
      white-space nowrap 
      text-overflow ellipsis
      overflow hidden
      display block

  & footer
    border-radius 0 0 4px 4px
    transition all 1s ease-out
    opacity 1
    background-color black 
    height 40px
    box-sizing border-box
    padding 7.5px
    display flex

  &__button
    border-radius 4px
    &-hide
      height 20px
      color white
      background-color black
      border 1px solid white
      width 20px
      position relative
      &::after
        position absolute
        content '-'
        display block
        font-weight 700
        font-size 22px
        top -5px
      &:hover
        background-color lighten(black, 10)
      &:active
        background-color lighten(black, 20)

    &-reset,
    &-upload
      height 25px
      color white
      background-color black
      border 1px solid white
      position relative
      &:hover
        background-color lighten(black, 10)
      &:active
        background-color lighten(black, 20)

    &-upload
      margin-left auto
</style>