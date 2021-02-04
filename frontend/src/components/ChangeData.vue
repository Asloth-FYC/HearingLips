<template>
    <el-dialog
            title="修改密码"
            :visible.sync="dialogVisible"
            :lock-scroll="false"
            width="800px"
            ref="ChangeData">
        <el-form :model="form" ref="form" size="medium" label-width="80px" :rules="rules">
            <el-form-item label="用户名" prop="username">
                <el-input placeholder="请输入用户名" v-model="form.username"
                          oninput="value=value.replace(/[^\dA-Za-z@.]/g,'')"></el-input>
            </el-form-item>
            <el-form-item label="原密码" prop="inputOpassword" >
                <el-input placeholder="请输入原密码" type="password" maxlength="8"
                          v-model="form.inputOpassword"  ></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="inputPassword" :error="errorText">
                <el-input placeholder="请输入密码" type="password" maxlength="8"
                          v-model="form.inputPassword"  @input="onPasswordInput"></el-input>
            </el-form-item>
            <el-form-item label="确认" prop="confirmPassword" :error="errorText">
                <el-input placeholder="请再次输入密码" type="password" maxlength="8"
                          v-model="form.confirmPassword"  @input="onPasswordInput"></el-input>
            </el-form-item>
            <el-form-item class="text-center">
                <el-button type="primary" @click="onConfirm" style="width: 200px">{{btnText2}}</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
    import dialogmixin from "../assets/js/dialogMixin";
    import { apiAdminForgetMail, apiAdminForgetPassword} from "../api/admin";
    import md5 from 'js-md5'
    import {updata} from "../api/user"
    export default {
        mixins: [dialogmixin],
        data() {
            return {
                form: {},
                enform:{},
                errorText: '',
                btnText2:'确认',
                rules,
            }
        },
        methods:{
            onPasswordInput(val) {
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
                            this.message({
                                message: '两次密码不一致',
                                type: 'warning'
                            });
                            return;
                        } else {
                            this.errorText = '';
                        }
                        this.enform.username=this.form.username
                        this.enform.Opsw = md5(this.form.inputOpassword)
                        this.enform.Npsw = md5(this.form.inputPassword)
                        updata(this.enform).then(resp => {
                            let data = resp.data;
                            if(data.code==200){
                                this.$notify({
                                    title: data.msg,
                                    message: '修改成功!  '+data.name,
                                    type: 'success'
                                });
                                this.$router.push({name:'home'});
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
        username: [emptyValid("用户名")],
        inputOpassword:[emptyValid("原密码")],
        inputPassword: [emptyValid("密码")],
        confirmPassword: [emptyValid("确认密码")],
    }
</script>

<style scoped>

</style>