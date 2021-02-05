<template>
  <el-dialog
      title="找回密码"
      :visible.sync="dialogVisible"
      :lock-scroll="false"
      width="800px"
      ref="forgetpswDialog"
      center>
    <el-form :model="form" ref="form" size="medium" label-width="80px" :rules="rules">
      <el-form-item label="邮箱" prop="email">
        <el-input placeholder="请输入邮箱地址" v-model="form.email"
                  oninput="value=value.replace(/[^\dA-Za-z@.]/g,'')"></el-input>
      </el-form-item>
      <el-form-item label="验证码" prop="code">
        <div class="code">
          <el-input placeholder="请输入验证码" v-model="form.code"
                    class="margin-right-xs"></el-input>
          <el-button type="primary" @click="onSendCode" size="mini" :disabled="disabled">{{btnText1}}</el-button>
        </div>
      </el-form-item>
      <el-form-item label="密码" prop="inputPassword" :error="errorText">
        <el-input placeholder="请输入新密码" type="password"
                  v-model="form.inputPassword" ></el-input>
      </el-form-item>
      <el-form-item label="确认" prop="confirmPassword" :error="errorText">
        <el-input placeholder="请再次输入密码" type="password"
                  v-model="form.confirmPassword"></el-input>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="onConfirm">{{btnText2}}</el-button>
    </span>
    
  </el-dialog>
</template>

<script>
import dialogmixin from "@/assets/js/dialogMixin";
import {apiAdminMail,apiAdminForgotPassword} from "@/api/admin";

export default {
  mixins: [dialogmixin],
  data() {
    return {
      form: {},
      errorText: '',
      btnText1:'发送验证码',
      btnText2:'确认',
      disabled: false,
      ts: 60,
      rules,
    }
  },
  methods:{
    onPasswordInput() {
      if (this.form.inputPassword !== this.form.confirmPassword) {
        this.errorText = '两次密码不一致';
      } else {
        this.errorText = '';
      }
    },
    onConfirm() {
      this.$refs.form.validate(valid => {
        if (valid) {
          if (this.form.inputPassword !== this.form.confirmPassword) {
            this.errorText = '两次密码不一致';
            return;
          } else {
            this.errorText = '';
          }
          apiAdminForgotPassword(this.form).then((resp) => {
            let data = resp.data;
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
          })
        }
      })
    },
    //发送验证码
    onSendCode() {
      if (this.form.email) {
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