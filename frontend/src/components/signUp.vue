<template>
<div>
  <el-form :model="form" ref="form" size="medium"  :rules="rules" class="forms_fieldset">
    <el-form-item  prop="username" class="forms_field">
      <el-input placeholder="请输入用户名" v-model="form.username"
                oninput="value=value.replace(/[^\dA-Za-z@.]/g,'')"></el-input>
    </el-form-item>
    <el-form-item  prop="email" class="forms_field">
      <el-input placeholder="请输入邮箱地址" v-model="form.email"
                oninput="value=value.replace(/[^\dA-Za-z@.]/g,'')"></el-input>
    </el-form-item>
    <el-form-item  prop="code" class="forms_field">
      <div class="code">
        <el-input placeholder="请输入验证码" v-model="form.code"
                  class="margin-right-xs"></el-input>
        <el-button  @click="onSendCode" size="mini" :disabled="disabled">{{btnText1}}
        </el-button>
      </div>
    </el-form-item>
    <el-form-item  prop="inputPassword" :error="errorText" class="forms_field">
      <el-input placeholder="设置密码" type="password"
                v-model="form.inputPassword" ></el-input>
    </el-form-item>
    <el-form-item  prop="confirmPassword" :error="errorText" class="forms_field">
      <el-input placeholder="确认密码" type="password"
                v-model="form.confirmPassword" @input="onPasswordInput"></el-input>
    </el-form-item>
  </el-form>
</div>
</template>

<script>
import {apiAdminMail} from "@/api/admin"

export default {
  name: "signUp",
  data() {
    return {
      form: {},
      errorText: '',
      btnText1:'发送验证码',
      disabled: false,
      ts: 60,
      rules,
    }
  },
  watch:{
    form:function (){
      this.form.valid=this.$refs.form.validate
      this.toParent()
    }
  },
  methods:{
    toParent() {
      this.$emit('uploadForm', this.form)
    },
    onPasswordInput() {
      if (this.form.inputPassword !== this.form.confirmPassword) {
        this.errorText = '两次密码不一致';
      } else {
        this.errorText = '';
      }
    },
    //发送验证码
    onSendCode() {
      if (this.form.username && this.form.email) {
        this.disabled = true;
        let interval = setInterval(() => {
          this.ts -= 1;
          if (this.ts === 0) {
            clearInterval(interval)
            this.btnText1 = '发送验证码';
            this.disabled = false;
            this.ts = 60;
          } else {
            this.btnText1 = this.ts + 's'+'重发';
          }
        }, 1000)
        apiAdminMail({email: this.form.email}).then((resp) => {
            let data = resp.data;
            console.log(data.code);
            if(data.code==200){
              this.$notify({
                title: '成功',
                message: data.msg,
                type: 'success'
              });
            }else{
              this.$notify({
                title: '错误',
                message: data.msg,
                type: 'error'
              });
            }
        }).catch(()=>{
          clearInterval(interval)
          this.btnText = '发送验证码';
          this.disabled = false;
          this.ts = 60;
        })
      } else {
        this.$message.error('用户名和邮箱不能为空')
      }
    }
  }
}

const emptyText="不能为空";
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
const rules = {
  code: [emptyValid("验证码")],
  username: [emptyValid("用户名")],
  inputPassword: [emptyValid("密码")],
  confirmPassword: [emptyValid("确认密码")],
  email: [emptyValid("邮箱"), {validator: validateEmail, trigger: 'blur'}],
}

</script>

<style scoped>
.code{
  display: flex;
  align-items: center;
}
.margin-right-xs{
  margin-right: 10px;
}

</style>