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
            <h2 class="forms_title">Sign in</h2>
              <fieldset class="forms_fieldset">
                <div class="forms_field">
                  <input type="email" v-model="postParams.email" placeholder="Email" class="forms_field-input" required autofocus />
                </div>
                <div class="forms_field">
                  <input type="password" v-model="ruleForm.psw" placeholder="Password" class="forms_field-input" required />
                </div>
              </fieldset>
              <div class="forms_buttons">
                <button type="button" class="forms_buttons-forgot" @click="forgetpsw">Forgot password?</button>
              <button class="forms_buttons-action" @click="sign_in">Sign In</button>
              </div>
          </div>
          <div class="user_forms-signup">
            <h2 class="forms_title">Sign Up</h2>
              <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" class="forms_fieldset">
                <el-form-item class="forms_field">
                  <input type="text" v-model="postParams.name" placeholder="Username" class="forms_field-input" required />
                </el-form-item>
                <el-form-item class="forms_field">
                  <input type="email" v-model="postParams.email" placeholder="Email" class="forms_field-input" required />
                </el-form-item>
                <el-form-item class="forms_field" prop="psw">
                  <input type="password" v-model="ruleForm.psw" placeholder="Password" class="forms_field-input" required />
                </el-form-item>
                <el-form-item class="forms_field" prop="psw_check">
                  <input type="password" v-model="ruleForm.psw_check" placeholder="Check Password" class="forms_field-input" required />
                </el-form-item>
              </el-form>
              <div class="forms_buttons">
                <button class="forms_buttons-action" @click="sign_up('ruleForm')">Sign up</button>
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
import md5 from 'js-md5'
import forgetpswDialog from "@/components/forgetpswDialog";

export default {
  name: 'login',
  components:{
    forgetpswDialog
  },
  data(){
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        if (this.ruleForm.psw_check !== '') {
          this.$refs.ruleForm.validateField('psw_check');
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.psw) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return{
      postParams:{
        name:'',
        email:'',
        psw_md5:''
      },
      ruleForm:{
        psw:'',
        psw_check:''
      },
      rules: {
        psw: [
          { validator: validatePass, trigger: 'blur' }
        ],
        psw_check: [
          { validator: validatePass2, trigger: 'blur' }
        ]
      }
    };
  },
  methods:{
    choose_signup(){
      this.psw=''
      const userForms = document.getElementById('user_options-forms')
      userForms.classList.remove('bounceRight')
      userForms.classList.add('bounceLeft')
    },
    choose_login(){
      const userForms = document.getElementById('user_options-forms')
      userForms.classList.remove('bounceLeft')
      userForms.classList.add('bounceRight')
    },
    sign_in(){
      this.postParams.psw_md5 = md5(this.ruleForm.psw)
      login(this.postParams).then(resp => {
        let data = resp.data;
        if(data.code==200){
          this.$notify({
            title: data.msg,
            message: 'Welcome!  '+data.name,
            type: 'success'
          });
          localStorage.setItem('Authorization',data.token);
          this.$router.push({name:'home',params:{id:data.id}});
        }else{
          this.$notify({
            title: '错误',
            message: data.msg,
            type: 'error'
          });
        }
      })
    },
    sign_up(formName){
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.postParams.psw_md5 = md5(this.ruleForm.psw)
          register(this.postParams).then(resp => {
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
      });
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
