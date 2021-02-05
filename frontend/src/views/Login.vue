<template>
  <div class="login">
    <section class="user">
      <div class="user_options-container">
        <div class="user_options-text">
          <div class="user_options-unregistered">
            <h2 class="user_unregistered-title">Don't have an account?</h2>
            <p class="user_unregistered-text">Welcome to HearingLips!</p>
            <button  class="user_unregistered-signup" id="signup-button" @click="choose_signup">Sign up</button>
          </div>

          <div class="user_options-registered">
            <h2 class="user_registered-title">Have an account?</h2>
            <p class="user_registered-text">Try out now!</p>
            <button  class="user_registered-login" id="login-button" @click="choose_login">Sign in</button>
          </div>
        </div>

        <div class="user_options-forms" id="user_options-forms">
          <div class="user_forms-login">
            <h2 class="forms_SItitle">Sign in</h2>
            <el-form :model="form" ref="Aform" size="medium" :rules="rules" class="forms_fieldset" >
              <el-form-item  prop="email" class="forms_field">
                <el-input placeholder="请输入邮箱地址" v-model="form.email"
                          oninput="value=value.replace(/[^\dA-Za-z@.]/g,'')"></el-input>
              </el-form-item>
              <el-form-item  prop="psw"  class="forms_field">
                <el-input placeholder="请输入密码" type="password" v-model="form.psw" ></el-input>
              </el-form-item>
            </el-form>
              <div class="forms_buttons">
                <button type="button" class="forms_buttons-forgot" @click="forgetpsw">Forgot password?</button>
              <button class="forms_buttons-action" @click="sign_in('Aform')">Sign In</button>
              </div>
          </div>
          <div class="user_forms-signup">
            <h2 class="forms_SUtitle">Sign Up</h2>
              <sign-up @uploadForm="uploadForm"></sign-up>
              <div class="forms_buttons">
                <button class="forms_buttons-action" @click="sign_up">Sign up</button>
              </div>
          </div>
        </div>
      </div>
    </section>
    <forgetpswDialog ref="forgetPasswordDialog"></forgetpswDialog>
  </div>
</template>

<script>
import {login,register} from '@/api/user'
import forgetpswDialog from "@/components/forgetpswDialog";
import signUp from "@/components/signUp";

const emptyText="不能为空";

export default {
  name: 'login',
  components:{
    forgetpswDialog,
    signUp
  },
  data(){
    var emptyValid = msg => {
      return {required: true, message: msg + emptyText, trigger: "blur"};
    };
    var validateEmail = (rule, value, callback) => {
      if (value) {
        let reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
        if (!reg.test(value)) {
          callback(new Error("邮箱地址不合法！"));
        }
      }
      callback();
    };
    return{
      form:{
        name:'',
        email:'',
        psw:'',
        captcha:''
      },
        psw_check:'',
        SUvalid:'',//从signup子组件传回的表单校验值
      rules :{
        psw: [emptyValid("密码")],
        email: [emptyValid("邮箱"), {validator: validateEmail, trigger: 'blur'}],
      }
    };
  },
  methods:{
    uploadForm(form){
      this.form.name=form.username
      this.form.email=form.email
      this.form.captcha=form.code
      this.form.psw=form.inputPassword
      this.psw_check=form.confirmPassword
      this.SUvalid=form.valid
    },
    choose_signup(){
      this.form.psw=''
      const userForms = document.getElementById('user_options-forms')
      userForms.classList.remove('bounceRight')
      userForms.classList.add('bounceLeft')
    },
    choose_login(){
      const userForms = document.getElementById('user_options-forms')
      userForms.classList.remove('bounceLeft')
      userForms.classList.add('bounceRight')
    },
    sign_in(formName){
      this.$refs[formName].validate((valid) => {
        if (valid){
          login(this.form).then(resp => {
            let data = resp.data;
            if (data.code == 200) {
              this.$notify({
                title: data.msg,
                message: 'Welcome!  ' + data.name,
                type: 'success'
              });
              localStorage.setItem('Authorization', data.token);
              this.$router.push({name: 'home'});
            } else {
              this.$notify({
                title: '错误',
                message: data.msg,
                type: 'error'
              });
            }
          })
        } else {
          console.log('error submit!!');
          return false;
        }
      })
    },
    sign_up(){
        if (this.SUvalid) {
          register(this.form).then(resp => {
            let data = resp.data;
            if(data.code==200){
              this.$notify({
                title: '注册成功',
                message: data.msg,
                type: 'success'
              });
              this.choose_login()
            }else{
              this.$notify({
                title: '错误',
                message: data.msg,
                type: 'error'
              });
            }
          })
        } else {
          console.log('error submit!!');
          return false;
        }
    },
    forgetpsw(){
      this.$refs.forgetPasswordDialog.onShow();
    }
  },
}
</script>


<style lang="sass" scoped>
  @import "@/assets/styles/login-style"
</style>
