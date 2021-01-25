<template>
   <div id="login-container">
  <div id="account-box" :class="isRegisterActive">
    <div @click="changeRegisterActive" id="show-register-box"  :title="isRegisterActive === '' ? 'Register' : 'Login' ">
      icon
    </div>
    <div id="login-box">
      <div id="login-title">ACCOUNT LOGIN</div>
      <div id="login-form">
        <div id="login-username">
          USERNAME<br/>
          <input type="text">
        </div>
        <div id="login-password">
          PASSWORD<br/>
          <input type="text">
        </div>
        <div id="pw-group" >
          <span>REMEMBER ME</span>
          <span>FORGOT?</span>
        </div>
        <button id="login-button">LOGIN</button>
      </div>
    </div>
    <div :class="isRegisterActive" id="register-box">
      <div id="register-title">REGISTER ACCOUNT</div>
      <div id="register-form">
        <div id="register-username">
          USERNAME<br/>
          <input type="text">
        </div>
        <div id="register-password">
          PASSWORD<br/>
          <input type="text">
        </div>
        <div id="register-email">
          EMAIL<br/>
          <input type="text">
        </div>
      </div>
      <button id="register-button">REGISTER</button>
    </div>
  </div>
</div>
</template>

<style lang="sass" scoped>
$foreground-color: #2196f3
$background-color: #414141
$login-box-padding: 60px
$small-width: 410px
@mixin title
  font-size: 1.6rem
  color: $foreground-color
  margin-bottom: 15px
@mixin input
  $padding: 12px
  border: 0
  outline: none
  padding: $padding
  margin: 10px 0 15px 0
  width: calc(100% - #{$padding * 2})
  background-color: #e0e0e0
  border-radius: 3px
@mixin button
  background-color: $foreground-color
  color: #fff
  outline: none
  margin: 15px auto
  padding: 15px 0
  width: 80%
  border: none
  border-radius: 3px
  display: block
  cursor: pointer
  transition: background-color 0.2s ease-in-out
  &:active
    background-color: darken($foreground-color,5%) !important
  &:hover
    background-color: lighten($foreground-color,5%)

#login-container
  color: $background-color
  background: linear-gradient(45deg, rgba(66, 183, 245, 0.8) 0%, rgba(66, 245, 189, 0.4) 100%)
  width: 100vw
  height: 100vh
  position: absolute
  top: 0
  left: 0
  font-size: 15px
  display: flex
  flex-direction: row
  justify-content: center
  align-items: center
  font-family: sans-serif
  //account container
  #account-box
    width: 600px
    border-radius: 5px
    background-color: white
    overflow: hidden
    position: relative
    height: 420px
    max-height: 90vh
    overflow-y: auto
    transition: height .2s ease-in-out
    max-width: 90vw
    #login-tips
      position: absolute
      display: inline-block
      background-color: $foreground-color
      color: #fff
      &::before
        content: ''
        width: 0
        height: 0
        border-top: 20px solid transparent
        border-bottom: 20px solid transparent
        border-left: 20px solid $foreground-color
    &.register-active
      height: 460px
    #show-register-box
      width: 50px
      height: 50px
      position: absolute
      background-color: $foreground-color
      border-radius: 50%
      right: 20px
      top: 30px
      display: flex
      justify-content: center
      align-items: center
      color: white
      cursor: pointer
      animation: at-ripple 1.5s linear infinite
      z-index: 6
      user-select: none
      &:hover
        animation: at-ripple 0.6s linear infinite, jump 0.2s linear 1 , jump2 0.2s linear 0
      &:active
        animation: at-ripple 0.6s linear infinite, jump2 0.2s linear 1
      &::before
        content: ''
        position: absolute
        height: 40px
        width: 2px
        background-color: $foreground-color
        display: block
        top: -40px
        z-index: 5

  //Login Box
  #login-box
    padding: $login-box-padding $login-box-padding ($login-box-padding - 30) $login-box-padding
    box-sizing: border-box
    #login-title
      @include title
    //login form
    #login-form
      margin: 15px 0
      #login-username, #login-password
        font-size: 0.8rem
        input
          @include input
      #pw-group
        display: flex
        margin-bottom: 35px
        span
          flex: 1
        span:nth-child(2)
          color: $foreground-color
          justify-content: flex-end
          text-align: right
      #login-button
        @include button

  //register Box
  #register-box
    @extend #login-box
    position: absolute
    width: 90vw
    max-width: 600px
    top: -500px
    transition: top .2s ease-in-out
    background-color: white
    z-index: 2
    &.register-active
      top: 0
    #register-title
      @include title
    //register form
    #register-form
      margin: 15px 0
      #register-username, #register-password,#register-email
        font-size: 0.8rem
        input
          @include input
    #register-button
      @include button

@media screen and (max-width: $small-width)
  #account-box
    height: 80vh !important

  #login-box,#register-box
    padding: 120px 20px 30px 20px !important
    #login-title,#register-title
      font-size: 1.2rem !important
      font-weight: bold
    #login-button,#register-button
      width: 90% !important
$ripple-color: rgba(66,133,244,0.1)
@keyframes at-ripple
  0%
    box-shadow: 0 4px 10px rgba($foreground-color,0.1), 0 0 0 0 rgba($foreground-color,0.1), 0 0 0 5px rgba($foreground-color,0.1), 0 0 0 10px rgba($foreground-color,0.1)
  100%
    box-shadow: 0 4px 10px rgba($foreground-color,0.1), 0 0 0 5px rgba($foreground-color,0.1), 0 0 0 10px rgba($foreground-color,0.1), 0 0 0 20px rgba($foreground-color,0)
@keyframes jump
  0%
    transform: translateY(0)
  50%
    transform: translateY(10px)
  100%
    transform: translateY(0)
@keyframes jump2
  0%
    transform: translateY(0)
  50%
    transform: translateY(10px)
  100%
    transform: translateY(0)
</style>

<script>
export default {
    data(){
        return{
            isRegisterActive: ''
        }
    },
    methods: {
    changeRegisterActive() {
      this.isRegisterActive = this.isRegisterActive === '' ? 'register-active' : ''
    }
  }
}
</script>