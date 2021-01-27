<template>
  <div class="login">
    <section class="user">
      <div class="user_options-container">
        <div class="user_options-text">
          <div class="user_options-unregistered">
            <h2 class="user_unregistered-title">Don't have an account?</h2>
            <p class="user_unregistered-text">welcome to lip reading!</p>
            <button  class="user_unregistered-signup" id="signup-button" @click="choose_signup">Sign up</button>
          </div>

          <div class="user_options-registered">
            <h2 class="user_registered-title">Have an account?</h2>
            <p class="user_registered-text">try out now!</p>
            <button  class="user_registered-login" id="login-button" @click="choose_login">Login</button>
          </div>
        </div>

        <div class="user_options-forms" id="user_options-forms">
          <div class="user_forms-login">
            <h2 class="forms_title">Login</h2>
            <form class="forms_form">
              <fieldset class="forms_fieldset">
                <div class="forms_field">
                  <input type="email" v-model="user.email" placeholder="Email" class="forms_field-input" required autofocus />
                </div>
                <div class="forms_field">
                  <input type="password" v-model="user.psw" placeholder="Password" class="forms_field-input" required />
                </div>
              </fieldset>
              <div class="forms_buttons">
                <button type="button" class="forms_buttons-forgot">Forgot password?</button>
              <input type="submit" value="Log In" class="forms_buttons-action">
              </div>
            </form>
          </div>
          <div class="user_forms-signup">
            <h2 class="forms_title">Sign Up</h2>
            <form class="forms_form">
              <fieldset class="forms_fieldset">
                <div class="forms_field">
                  <input type="text" v-model="user.name" placeholder="Full Name" class="forms_field-input" required />
                </div>
                <div class="forms_field">
                  <input type="email" v-model="user.email" placeholder="Email" class="forms_field-input" required />
                </div>
                <div class="forms_field">
                  <input type="password" v-model="user.psw" placeholder="Password" class="forms_field-input" required />
                </div>
              </fieldset>
              <div class="forms_buttons">
                <input type="submit" value="Sign up" class="forms_buttons-action">
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>

export default {
  name: 'login',
  data(){
    return{
      user:{
        name:'',
        psw:'',
        email:''//暂时仅支持用邮箱地址登录
      },
    }
  },
  methods:{
    // signup(){
    //   //检查相关信息是否存储进变量中
    //   console.log("sign up!");
    //   console.log(this.user.name);
    //   console.log(this.user.psw);
    // },
    // login(){
    //   //检查相关信息是否存储进变量中
    //   console.log("login!");
    //   console.log(this.user.name);
    //   console.log(this.user.psw);
    // },
    choose_signup(){
      const userForms = document.getElementById('user_options-forms')
      userForms.classList.remove('bounceRight')
      userForms.classList.add('bounceLeft')
    },
    choose_login(){
      const userForms = document.getElementById('user_options-forms')
      userForms.classList.remove('bounceLeft')
      userForms.classList.add('bounceRight')
    }
  }
}
</script>


<style lang="sass" scoped>
  @import "@/assets/styles/login-style"
</style>
